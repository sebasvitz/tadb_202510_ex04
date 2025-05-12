from app.context.db_context import DbContext

def test_connection():
    db_context = DbContext()  # Inicializa la conexión
    print("Probando conexión a MongoDB...")
    
    # Verificar acceso a la colección "compuestos"
    compuestos = list(db_context.compuestos.find())
    print(f"Conexión exitosa. Se encontraron {len(compuestos)} compuestos en la base de datos.")

if __name__ == "__main__":
    test_connection()