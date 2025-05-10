from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Optional

class MedicamentoBase(BaseModel):
    nombre: str
    fabricante: str
    
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }

class MedicamentoCreate(MedicamentoBase):
    pass

class Medicamento(MedicamentoBase):
    id: Optional[str] = Field(None, alias="_id")

    class Config:
        populate_by_name = True