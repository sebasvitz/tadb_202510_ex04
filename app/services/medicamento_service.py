from app.repositories.medicamento_repository import MedicamentoRepository
from app.models.medicamento import Medicamento, MedicamentoCreate
from app.models.compuesto_medicamento import CompuestoMedicamentoCreate, CompuestoConConcentracion
from typing import List, Optional

class MedicamentoService:
    def __init__(self):
        self.repository = MedicamentoRepository()
    
    def get_all_medicamentos(self) -> List[Medicamento]:
        """Obtener todos los medicamentos"""
        return self.repository.get_all()
    
    def get_medicamento_by_id(self, medicamento_id: str) -> Optional[Medicamento]:
        """Obtener un medicamento por su ID"""
        return self.repository.get_by_id(medicamento_id)
    
    def create_medicamento(self, medicamento: MedicamentoCreate) -> Medicamento:
        """Crear un nuevo medicamento"""
        return self.repository.create(medicamento)
    
    def update_medicamento(self, medicamento_id: str, medicamento: MedicamentoCreate) -> Optional[Medicamento]:
        """Actualizar un medicamento existente"""
        existing_medicamento = self.repository.get_by_id(medicamento_id)
        if not existing_medicamento:
            return None
        return self.repository.update(medicamento_id, medicamento)
    
    def delete_medicamento(self, medicamento_id: str) -> bool:
        """Eliminar un medicamento"""
        existing_medicamento = self.repository.get_by_id(medicamento_id)
        if not existing_medicamento:
            return False
        return self.repository.delete(medicamento_id)
    
    def get_compuestos_by_medicamento(self, medicamento_id: str) -> List[CompuestoConConcentracion]:
        """Obtener todos los compuestos de un medicamento específico"""
        existing_medicamento = self.repository.get_by_id(medicamento_id)
        if not existing_medicamento:
            return []
        return self.repository.get_compuestos_by_medicamento(medicamento_id)
    
    def add_compuesto_to_medicamento(self, compuesto_medicamento: CompuestoMedicamentoCreate):
        """Agregar un compuesto a un medicamento con su concentración"""
        return self.repository.add_compuesto_to_medicamento(compuesto_medicamento)