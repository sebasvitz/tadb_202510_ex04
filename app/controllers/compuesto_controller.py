import logging
from fastapi import APIRouter, HTTPException, status
from app.services.compuesto_service import CompuestoService
from app.models.compuesto import Compuesto, CompuestoCreate
from app.models.medicamento import Medicamento
from typing import List

# Configuración del logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/compuestos", tags=["Compuestos"])
service = CompuestoService()

@router.get("", response_model=List[Compuesto])
def get_all_compuestos():
    """Listar todos los compuestos"""
    logger.info("Solicitud para obtener todos los compuestos.")
    try:
        compuestos = service.get_all_compuestos()
        logger.info(f"Se encontraron {len(compuestos)} compuestos.")
        return compuestos
    except Exception as e:
        logger.error(f"Error al obtener compuestos: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error al obtener compuestos."
        )

@router.get("/{compuesto_id}", response_model=Compuesto)
def get_compuesto_by_id(compuesto_id: str):
    """Listar un compuesto por Id"""
    logger.info(f"Solicitud para obtener el compuesto con ID {compuesto_id}.")
    try:
        compuesto = service.get_compuesto_by_id(compuesto_id)
        if not compuesto:
            logger.warning(f"Compuesto con ID {compuesto_id} no encontrado.")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Compuesto con ID {compuesto_id} no encontrado"
            )
        logger.info(f"Compuesto con ID {compuesto_id} encontrado: {compuesto}.")
        return compuesto
    except Exception as e:
        logger.error(f"Error al obtener compuesto con ID {compuesto_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error al procesar la solicitud."
        )

@router.get("/{compuesto_id}/medicamentos", response_model=List[Medicamento])
def get_medicamentos_by_compuesto(compuesto_id: str):
    """Listar Medicamentos que tienen un compuesto por Id"""
    logger.info(f"Solicitud para obtener medicamentos del compuesto con ID {compuesto_id}.")
    try:
        medicamentos = service.get_medicamentos_by_compuesto(compuesto_id)
        logger.info(f"Se encontraron {len(medicamentos)} medicamentos para el compuesto con ID {compuesto_id}.")
        return medicamentos
    except Exception as e:
        logger.error(f"Error al obtener medicamentos para el compuesto con ID {compuesto_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error al obtener medicamentos."
        )

@router.post("", response_model=Compuesto, status_code=status.HTTP_201_CREATED)
def create_compuesto(compuesto: CompuestoCreate):
    """Agregar un compuesto"""
    logger.info(f"Solicitud para crear un compuesto: {compuesto}.")
    try:
        new_compuesto = service.create_compuesto(compuesto)
        # Línea corregida para usar .id en lugar de ._id
        logger.info(f"Compuesto creado exitosamente con ID {new_compuesto.id}.")
        return new_compuesto
    except Exception as e:
        logger.error(f"Error al crear compuesto: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error al crear compuesto."
        )

@router.put("/{compuesto_id}", response_model=Compuesto)
def update_compuesto(compuesto_id: str, compuesto: CompuestoCreate):
    """Actualizar un compuesto"""
    logger.info(f"Solicitud para actualizar el compuesto con ID {compuesto_id}: {compuesto}.")
    try:
        updated_compuesto = service.update_compuesto(compuesto_id, compuesto)
        if not updated_compuesto:
            logger.warning(f"Compuesto con ID {compuesto_id} no encontrado para actualizar.")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Compuesto con ID {compuesto_id} no encontrado"
            )
        logger.info(f"Compuesto con ID {compuesto_id} actualizado exitosamente.")
        return updated_compuesto
    except Exception as e:
        logger.error(f"Error al actualizar compuesto con ID {compuesto_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error al actualizar compuesto."
        )

@router.delete("/{compuesto_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_compuesto(compuesto_id: str):
    """Eliminar un compuesto"""
    logger.info(f"Solicitud para eliminar el compuesto con ID {compuesto_id}.")
    try:
        deleted = service.delete_compuesto(compuesto_id)
        if not deleted:
            logger.warning(f"Compuesto con ID {compuesto_id} no encontrado para eliminar.")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Compuesto con ID {compuesto_id} no encontrado"
            )
        logger.info(f"Compuesto con ID {compuesto_id} eliminado exitosamente.")
        return None
    except Exception as e:
        logger.error(f"Error al eliminar compuesto con ID {compuesto_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error al eliminar compuesto."
        )