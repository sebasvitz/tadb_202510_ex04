from bson import ObjectId, errors as bson_errors
from app.context.db_context import DbContext
from app.models.compuesto import Compuesto, CompuestoCreate
from app.models.medicamento import Medicamento
from app.models.compuesto_medicamento import CompuestoConConcentracion
from typing import List, Dict, Any


class CompuestoRepository:
    def __init__(self):
        context = DbContext()
        self.compuestos = context.compuestos
        self.medicamentos = context.medicamentos
        self.compuestos_medicamentos = context.compuestos_medicamentos

    def get_all(self) -> List[Compuesto]:
        """Obtener todos los compuestos"""
        compuestos = list(self.compuestos.find())
        return [Compuesto(_id=str(c["_id"]), nombre=c["nombre"]) for c in compuestos]

    def get_by_id(self, compuesto_id: str) -> Compuesto:
        """Obtener un compuesto por su ID"""
        try:
            compuesto = self.compuestos.find_one({"_id": ObjectId(compuesto_id)})
            if compuesto:
                return Compuesto(_id=str(compuesto["_id"]), nombre=compuesto["nombre"])
            return None
        except bson_errors.InvalidId as e:
            print(f"ID inválido: {e}")
            return None
        except Exception as e:
            print(f"Error al obtener compuesto por ID: {e}")
            return None

    def create(self, compuesto_dict: Dict[str, Any]) -> Compuesto:
        """Crear un nuevo compuesto"""
        # Convertir el objeto en un diccionario si es una instancia de Pydantic
        if isinstance(compuesto_dict, CompuestoCreate):
            compuesto_dict = compuesto_dict.model_dump()  # Cambia a dict() si usas Pydantic v1

        # Asegurarse de que no haya un _id en el diccionario
        if "_id" in compuesto_dict:
            del compuesto_dict["_id"]

        # Insertar en la base de datos
        result = self.compuestos.insert_one(compuesto_dict)

        # Retornar el compuesto creado - usar una copia para evitar modificar el original
        return Compuesto(_id=str(result.inserted_id), nombre=compuesto_dict["nombre"])

    def update(self, compuesto_id: str, compuesto: CompuestoCreate) -> Compuesto:
        """Actualizar un compuesto existente"""
        compuesto_dict = compuesto.model_dump()  # Cambia a dict() si usas Pydantic v1
        
        # Asegurarse de que no haya un _id en el diccionario
        if "_id" in compuesto_dict:
            del compuesto_dict["_id"]
            
        self.compuestos.update_one(
            {"_id": ObjectId(compuesto_id)},
            {"$set": compuesto_dict}
        )
        return self.get_by_id(compuesto_id)

    def delete(self, compuesto_id: str) -> bool:
        """Eliminar un compuesto por su ID"""
        result = self.compuestos.delete_one({"_id": ObjectId(compuesto_id)})
        # También eliminamos las relaciones con medicamentos
        self.compuestos_medicamentos.delete_many({"compuesto_id": ObjectId(compuesto_id)})
        return result.deleted_count > 0

    def get_medicamentos_by_compuesto(self, compuesto_id: str) -> List[Medicamento]:
        """Obtener todos los medicamentos que contienen un compuesto específico"""
        try:
            # Encontrar todas las relaciones para este compuesto
            relaciones = list(self.compuestos_medicamentos.find({"compuesto_id": ObjectId(compuesto_id)}))

            # Obtener los IDs de medicamentos
            medicamento_ids = [rel["medicamento_id"] for rel in relaciones]

            # Buscar los medicamentos correspondientes
            medicamentos = list(self.medicamentos.find({"_id": {"$in": medicamento_ids}}))

            return [Medicamento(_id=str(m["_id"]), nombre=m["nombre"], fabricante=m["fabricante"])
                    for m in medicamentos]
        except Exception as e:
            print(f"Error al obtener medicamentos por compuesto: {e}")
            return []