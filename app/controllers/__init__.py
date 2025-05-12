"""Controladores para la API de Medicamentos y Compuestos"""

from app.controllers.compuesto_controller import router as compuesto_router
from app.controllers.medicamento_controller import router as medicamento_router

__all__ = ['compuesto_router', 'medicamento_router']