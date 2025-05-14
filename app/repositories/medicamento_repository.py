from bson import ObjectId
from app.context.db_context import DbContext
from app.models.medicamento import Medicamento, MedicamentoCreate
from app.models.compuesto import Compuesto
from app.models.compuesto_medicamento import CompuestoMedicamento, CompuestoMedicamentoCreate, CompuestoConConcentracion
from typing import List, Dict, Any

class MedicamentoRepository:
    def __init__(self):
        context = DbContext()
        self.medicamentos = context.medicamentos
        self.compuestos = context.compuestos
        self.compuestos_medicamentos = context.compuestos_medicamentos

    def get_all(self) -> List[Medicamento]:
        """Obtener todos los medicamentos"""
        medicamentos = list(self.medicamentos.find())
        return [Medicamento(_id=str(m["_id"]), nombre=m["nombre"], fabricante=m["fabricante"]) 
                for m in medicamentos]

    def get_by_id(self, medicamento_id: str) -> Medicamento:
        """Obtener un medicamento por su ID"""
        try:
            medicamento = self.medicamentos.find_one({"_id": ObjectId(medicamento_id)})
            if medicamento:
                return Medicamento(
                    _id=str(medicamento["_id"]), 
                    nombre=medicamento["nombre"], 
                    fabricante=medicamento["fabricante"]
                )
            return None
        except Exception:
            return None

    def create(self, medicamento: MedicamentoCreate) -> Medicamento:
        try:
            # Obtener diccionario del modelo Pydantic
            medicamento_dict = medicamento.model_dump()
            
            # Remover _id si existe en el diccionario
            if '_id' in medicamento_dict:
                del medicamento_dict['_id']
            
            # Insertar en la base de datos
            result = self.medicamentos.insert_one(medicamento_dict)
            
            # Crear el objeto con campos explícitos (evita conflictos)
            return Medicamento(
                id=str(result.inserted_id),
                nombre=medicamento_dict["nombre"],
                fabricante=medicamento_dict["fabricante"]
            )
        except Exception as e:
            # Si ocurre algún error, intentar hacer rollback manualmente
            if 'result' in locals() and hasattr(result, 'inserted_id'):
                self.medicamentos.delete_one({"_id": result.inserted_id})
            raise e  # Re-lanzar la excepción para que sea manejada en capas superiores

    def update(self, medicamento_id: str, medicamento: MedicamentoCreate) -> Medicamento:
        """Actualizar un medicamento existente"""
        medicamento_dict = medicamento.model_dump()
        self.medicamentos.update_one(
            {"_id": ObjectId(medicamento_id)},
            {"$set": medicamento_dict}
        )
        return self.get_by_id(medicamento_id)

    def delete(self, medicamento_id: str) -> bool:
        """Eliminar un medicamento por su ID"""
        result = self.medicamentos.delete_one({"_id": ObjectId(medicamento_id)})
        # También eliminamos las relaciones con compuestos
        self.compuestos_medicamentos.delete_many({"medicamento_id": ObjectId(medicamento_id)})
        return result.deleted_count > 0
    
    def get_compuestos_by_medicamento(self, medicamento_id: str) -> List[CompuestoConConcentracion]:
        """Obtener todos los compuestos de un medicamento específico con su concentración"""
        try:
            # Encontrar todas las relaciones para este medicamento
            pipeline = [
                {"$match": {"medicamento_id": ObjectId(medicamento_id)}},
                {"$lookup": {
                    "from": "compuestos",
                    "localField": "compuesto_id",
                    "foreignField": "_id",
                    "as": "compuesto"
                }},
                {"$unwind": "$compuesto"}
            ]
            
            relaciones = list(self.compuestos_medicamentos.aggregate(pipeline))
            
            # Convertir a modelo CompuestoConConcentracion
            return [CompuestoConConcentracion(
                id=str(rel["compuesto"]["_id"]),
                nombre=rel["compuesto"]["nombre"],
                concentracion=rel["concentracion"],
                unidad_medida=rel["unidad_medida"]
            ) for rel in relaciones]
        except Exception as e:
            print(f"Error al obtener compuestos por medicamento: {e}")
            return []
            
    def add_compuesto_to_medicamento(self, rel: CompuestoMedicamentoCreate) -> CompuestoMedicamento:
        """Agregar un compuesto a un medicamento con su concentración"""
        # Obtener el compuesto para conseguir su nombre
        compuesto = self.compuestos.find_one({"_id": ObjectId(rel.compuesto_id)})
        
        if not compuesto:
            raise ValueError(f"Compuesto con ID {rel.compuesto_id} no encontrado")
        
        rel_dict = {
            "compuesto_id": ObjectId(rel.compuesto_id),
            "medicamento_id": ObjectId(rel.medicamento_id),
            "concentracion": rel.concentracion,
            "unidad_medida": rel.unidad_medida,
            "elemento": compuesto["nombre"]  # Usar el nombre real del compuesto
        }
        
        result = self.compuestos_medicamentos.insert_one(rel_dict)
        return CompuestoMedicamento(
            _id=str(result.inserted_id),
            **rel.model_dump()
        )