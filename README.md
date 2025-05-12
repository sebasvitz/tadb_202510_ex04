

# Estructura basica del proyecto a nivel de carpetas y archivos:
tadb_202510_ex04/
│
├── app/
│   ├── __init__.py
│   ├── main.py                  # Punto de entrada de la aplicación
│   │
│   ├── controllers/             # Capa de controladores
│   │   ├── __init__.py
│   │   ├── compuesto_controller.py
│   │   └── medicamento_controller.py
│   │
│   ├── services/                # Capa de servicios
│   │   ├── __init__.py
│   │   ├── compuesto_service.py
│   │   └── medicamento_service.py
│   │
│   ├── repositories/            # Capa de repositorios
│   │   ├── __init__.py
│   │   ├── compuesto_repository.py
│   │   └── medicamento_repository.py
│   │
│   ├── models/                  # Modelos de datos
│   │   ├── __init__.py
│   │   ├── compuesto.py
│   │   ├── medicamento.py
│   │   └── compuesto_medicamento.py
│   │
│   └── context/                 # Contexto de base de datos
│       ├── __init__.py
│       └── db_context.py
│
├── Datos/                       # Carpeta para datos de ejemplo
│   ├── compuestos.json
│   ├── medicamentos.json
│   └── compuestos_medicamentos.json
│
├── requirements.txt             # Dependencias del proyecto
└── README.md                    # Documentación del proyecto


# Proyecto Medicamentos y Compuestos

API REST que implementa el patrón repositorio para la gestión de medicamentos y sus compuestos.

## Estructura del Proyecto

El proyecto sigue una arquitectura de capas implementando el patrón repositorio:

- **Controlador**: Manejo de peticiones y respuestas asociadas a verbos HTTP
- **Servicio**: Implementación de las validaciones de las reglas del negocio
- **Repositorio**: Ejecución de acciones CRUD asociadas a cada operación
- **Modelo**: Clases que definen el estado y comportamiento de las entidades
- **Contexto**: Conexión a la base de datos

## Requisitos

- Python 3.8 o superior
- MongoDB

## Instalación

1. Clone el repositorio:
```bash
git clone https://github.com/sebasvitz/tadb_202510_ex04.git
cd tadb_202510_ex04
```

2. Cree un entorno virtual:
```bash
python -m venv venv
```

3. Active el entorno virtual:

En Windows:
```bash
venv\Scripts\activate
```

En macOS/Linux:
```bash
source venv/bin/activate
```

4. Instale las dependencias:
```bash
pip install -r requirements.txt
```


## Ejecución

Para iniciar la aplicación, ejecute:

```bash
python -m app.main
```

La API estará disponible en http://localhost:8000

La documentación de la API estará disponible en:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Carga de Datos Iniciales
Para la carga de datos e implementacion del modelo revisar el archivo de abastecimineto Mongo

## Endpoints de la API

### Compuestos

- **GET /api/compuestos**: Listar todos los compuestos
- **GET /api/compuestos/{compuesto_id}**: Listar un compuesto por Id
- **GET /api/compuestos/{compuesto_id}/medicamentos**: Listar medicamentos que tienen un compuesto por Id
- **POST /api/compuestos**: Agregar un compuesto
- **PUT /api/compuestos/{compuesto_id}**: Actualizar un compuesto
- **DELETE /api/compuestos/{compuesto_id}**: Eliminar un compuesto

### Medicamentos

- **GET /api/medicamentos**: Listar todos los medicamentos
- **GET /api/medicamentos/{medicamento_id}**: Listar un medicamento por Id
- **GET /api/medicamentos/{medicamento_id}/compuestos**: Listar compuestos de un medicamento por Id
- **POST /api/medicamentos**: Agregar un medicamento
- **PUT /api/medicamentos/{medicamento_id}**: Actualizar un medicamento
- **DELETE /api/medicamentos/{medicamento_id}**: Eliminar un medicamento
- **POST /api/medicamentos/compuesto**: Agregar un compuesto a un medicamento

## Autores

- Sebastian Villa 
- Natalia Urrego
  