from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Optional

class CompuestoMedicamentoBase(BaseModel):
    compuesto_id: str
    medicamento_id: str
    concentracion: str
    unidad_medida: str
    
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }

class CompuestoMedicamentoCreate(CompuestoMedicamentoBase):
    pass

class CompuestoMedicamento(CompuestoMedicamentoBase):
    id: Optional[str] = Field(None, alias="_id")
    
    class Config:
        populate_by_name = True

# Modelo para representar un compuesto con su información de concentración
class CompuestoConConcentracion(BaseModel):
    id: str
    nombre: str
    concentracion: str
    unidad_medida: str