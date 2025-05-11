from fastapi import APIRouter, HTTPException, status
from app.services.medicamento_service import MedicamentoService
from app.models.medicamento import Medicamento, MedicamentoCreate
from app.models.compuesto_medicamento import CompuestoMedicamentoCreate, CompuestoConConcentracion
from typing import List

router = APIRouter(prefix="/api/medicamentos", tags=["Medicamentos"])
service = MedicamentoService()

@router.get("", response_model=List[Medicamento])
def get_all_medicamentos():
    """Listar todos los medicamentos"""
    return service.get_all_medicamentos()

@router.get("/{medicamento_id}", response_model=Medicamento)
def get_medicamento_by_id(medicamento_id: str):
    """Listar un medicamento por Id"""
    medicamento = service.get_medicamento_by_id(medicamento_id)
    if not medicamento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Medicamento con ID {medicamento_id} no encontrado"
        )
    return medicamento

@router.get("/{medicamento_id}/compuestos", response_model=List[CompuestoConConcentracion])
def get_compuestos_by_medicamento(medicamento_id: str):
    """Listar compuestos de un medicamento por Id"""
    compuestos = service.get_compuestos_by_medicamento(medicamento_id)
    return compuestos

@router.post("", response_model=Medicamento, status_code=status.HTTP_201_CREATED)
def create_medicamento(medicamento: MedicamentoCreate):
    """Agregar un medicamento"""
    return service.create_medicamento(medicamento)

@router.put("/{medicamento_id}", response_model=Medicamento)
def update_medicamento(medicamento_id: str, medicamento: MedicamentoCreate):
    """Actualizar un medicamento"""
    updated_medicamento = service.update_medicamento(medicamento_id, medicamento)
    if not updated_medicamento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Medicamento con ID {medicamento_id} no encontrado"
        )
    return updated_medicamento

@router.delete("/{medicamento_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_medicamento(medicamento_id: str):
    """Eliminar un medicamento"""
    deleted = service.delete_medicamento(medicamento_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Medicamento con ID {medicamento_id} no encontrado"
        )
    return None

@router.post("/compuesto", status_code=status.HTTP_201_CREATED)
def add_compuesto_to_medicamento(relacion: CompuestoMedicamentoCreate):
    """Agregar un compuesto a un medicamento"""
    return service.add_compuesto_to_medicamento(relacion)