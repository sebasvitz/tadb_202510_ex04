from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Optional

class CompuestoBase(BaseModel):
    nombre: str
    
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }

class CompuestoCreate(CompuestoBase):
    pass

class Compuesto(CompuestoBase):
    id: Optional[str] = Field(None, alias="_id")

    class Config:
        populate_by_name = True