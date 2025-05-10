from pymongo import MongoClient
from bson import ObjectId
import os
from dotenv import load_dotenv

class DbContext:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DbContext, cls).__new__(cls)
            load_dotenv()

            # Conexión a la base de datos MongoDB
            mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
            cls._instance.client = MongoClient(mongo_uri)
            cls._instance.db = cls._instance.client["medicamentos_db"]

            # Inicializar las colecciones
            cls._instance.compuestos = cls._instance.db["compuestos"]
            cls._instance.medicamentos = cls._instance.db["medicamentos"]
            cls._instance.compuestos_medicamentos = cls._instance.db["compuestos_medicamentos"]

        return cls._instance