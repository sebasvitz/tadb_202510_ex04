from pymongo import MongoClient
from bson import ObjectId
import os
from dotenv import load_dotenv

class DbContext:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DbContext, cls).__new__(cls)
            load_dotenv()  # Cargar las variables de entorno desde el archivo .env

            # Construir la URI de conexión con credenciales desde .env
            mongo_host = os.getenv("MONGO_HOST", "localhost")
            mongo_port = os.getenv("MONGO_PORT", "27017")
            mongo_user = os.getenv("MONGO_USER", "api_user")
            mongo_password = os.getenv("MONGO_PASSWORD", "contraseña_segura")
            mongo_db_name = os.getenv("MONGO_DB", "medicamentos_db")

            mongo_uri = f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/{mongo_db_name}"

            # Conexión a MongoDB
            cls._instance.client = MongoClient(mongo_uri)
            cls._instance.db = cls._instance.client[mongo_db_name]

            # Inicializar las colecciones
            cls._instance.compuestos = cls._instance.db["compuestos"]
            cls._instance.medicamentos = cls._instance.db["medicamentos"]
            cls._instance.compuestos_medicamentos = cls._instance.db["compuestos_medicamentos"]

        return cls._instance