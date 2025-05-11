import logging
from app.repositories.compuesto_repository import CompuestoRepository
from app.models.compuesto import Compuesto, CompuestoCreate
from app.models.medicamento import Medicamento
from typing import List, Optional

# Configuración del logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CompuestoService:
    def __init__(self):
        self.repository = CompuestoRepository()
    
    def get_all_compuestos(self) -> List[Compuesto]:
        """Obtener todos los compuestos"""
        try:
            logger.info("Obteniendo todos los compuestos.")
            compuestos = self.repository.get_all()
            logger.info(f"Se encontraron {len(compuestos)} compuestos.")
            return compuestos
        except Exception as e:
            logger.error(f"Error al obtener todos los compuestos: {e}")
            raise
    
    def get_compuesto_by_id(self, compuesto_id: str) -> Optional[Compuesto]:
        """Obtener un compuesto por su ID"""
        try:
            logger.info(f"Obteniendo compuesto con ID {compuesto_id}.")
            compuesto = self.repository.get_by_id(compuesto_id)
            if not compuesto:
                logger.warning(f"Compuesto con ID {compuesto_id} no encontrado.")
            return compuesto
        except Exception as e:
            logger.error(f"Error al obtener compuesto con ID {compuesto_id}: {e}")
            raise
    
    def create_compuesto(self, compuesto: CompuestoCreate) -> Compuesto:
        """Crear un nuevo compuesto"""
        try:
            logger.info(f"Creando un nuevo compuesto: nombre='{compuesto.nombre}'.")
            new_compuesto = self.repository.create(compuesto)
            # Línea corregida para usar .id en lugar de ._id
            logger.info(f"Compuesto creado exitosamente con ID {new_compuesto.id}.")
            return new_compuesto
        except Exception as e:
            logger.error(f"Error al crear compuesto: {e}")
            raise
    
    def update_compuesto(self, compuesto_id: str, compuesto: CompuestoCreate) -> Optional[Compuesto]:
        """Actualizar un compuesto existente"""
        try:
            logger.info(f"Actualizando compuesto con ID {compuesto_id}.")
            existing_compuesto = self.repository.get_by_id(compuesto_id)
            if not existing_compuesto:
                logger.warning(f"Compuesto con ID {compuesto_id} no encontrado para actualizar.")
                return None
            updated_compuesto = self.repository.update(compuesto_id, compuesto)
            logger.info(f"Compuesto con ID {compuesto_id} actualizado exitosamente.")
            return updated_compuesto
        except Exception as e:
            logger.error(f"Error al actualizar compuesto con ID {compuesto_id}: {e}")
            raise
    
    def delete_compuesto(self, compuesto_id: str) -> bool:
        """Eliminar un compuesto"""
        try:
            logger.info(f"Eliminando compuesto con ID {compuesto_id}.")
            existing_compuesto = self.repository.get_by_id(compuesto_id)
            if not existing_compuesto:
                logger.warning(f"Compuesto con ID {compuesto_id} no encontrado para eliminar.")
                return False
            result = self.repository.delete(compuesto_id)
            logger.info(f"Compuesto con ID {compuesto_id} eliminado exitosamente.")
            return result
        except Exception as e:
            logger.error(f"Error al eliminar compuesto con ID {compuesto_id}: {e}")
            raise
    
    def get_medicamentos_by_compuesto(self, compuesto_id: str) -> List[Medicamento]:
        """Obtener todos los medicamentos que contienen un compuesto específico"""
        try:
            logger.info(f"Obteniendo medicamentos para el compuesto con ID {compuesto_id}.")
            existing_compuesto = self.repository.get_by_id(compuesto_id)
            if not existing_compuesto:
                logger.warning(f"Compuesto con ID {compuesto_id} no encontrado.")
                return []
            medicamentos = self.repository.get_medicamentos_by_compuesto(compuesto_id)
            logger.info(f"Se encontraron {len(medicamentos)} medicamentos para el compuesto con ID {compuesto_id}.")
            return medicamentos
        except Exception as e:
            logger.error(f"Error al obtener medicamentos para el compuesto con ID {compuesto_id}: {e}")
            raise