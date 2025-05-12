from fastapi import FastAPI
from app.controllers import compuesto_controller, medicamento_controller
import uvicorn

app = FastAPI(
    title="API de Medicamentos y Compuestos",
    description="API REST para gestionar medicamentos y sus compuestos",
    version="1.0.0"
)

# Registrar rutas
app.include_router(compuesto_controller.router)
app.include_router(medicamento_controller.router)

@app.get("/")
def read_root():
    return {
        "message": "API de Medicamentos y Compuestos",
        "docs": "/docs",
        "redoc": "/redoc"
    }

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)