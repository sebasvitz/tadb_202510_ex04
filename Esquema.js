// Paso 1: Creación de usuarios para la base de datos
// Aquí se crean dos usuarios:
// - "admin_modelos" con permisos de propietario sobre la base de datos "medicamentos_db".
// - "api_user" con permisos de lectura y escritura para interactuar con la base de datos a través de una API.

// use medicamentos_db;

db.createUser({
    user: "admin_modelos",
    pwd: "contraseña_segura123",
    roles: [
        { role: "dbOwner", db: "medicamentos_db" }
    ]
});

db.createUser({
    user: "api_user",
    pwd: "contraseña_segura456",
    roles: [
        { role: "readWrite", db: "medicamentos_db" }
    ]
});

// Paso 2: Creación de la colección "compuestos_medicamentos"
// Esta colección almacena los compuestos de cada medicamento con validaciones estrictas para garantizar la integridad de los datos.



db.createCollection("compuestos_medicamentos", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["compuesto_id", "medicamento_id", "elemento", "concentracion", "unidad_medida"],
            properties: {
                compuesto_id: {
                    bsonType: "objectId",
                    description: "Debe ser un ObjectId que referencia un compuesto existente"
                },
                medicamento_id: {
                    bsonType: "objectId",
                    description: "Debe ser un ObjectId que referencia un medicamento existente"
                },
                elemento: {
                    bsonType: "string",
                    description: "Debe ser una cadena que coincida con el nombre del compuesto"
                },
                concentracion: {
                    bsonType: "string",
                    pattern: "^[0-9]+$",
                    description: "Debe ser una cadena que represente un número (ejemplo: '500')"
                },
                unidad_medida: {
                    bsonType: "string",
                    enum: ["mg", "g", "mcg"],
                    description: "Debe ser una de las unidades de medida permitidas: 'mg', 'g', 'mcg'"
                }
            }
        }
    },
    validationLevel: "strict",  // Rechazar documentos que no cumplan con las validaciones
    validationAction: "error"   // Lanzar error si el documento no es válido
});

// Paso 3: Inserción de datos en la colección "compuestos_medicamentos"
// Aquí se insertan ejemplos de compuestos asociados a medicamentos específicos para ilustrar cómo funciona la estructura de la colección.

db.compuestos_medicamentos.insertOne({
    compuesto_id: ObjectId("681a37b87d76855ca6732d98"), // Acetaminofén
    medicamento_id: ObjectId("681a388f7d76855ca6732da1"), // Noxpirin
    elemento: "Acetaminofén",
    concentracion: "500",
    unidad_medida: "mg"
});

// (Repetir para cada compuesto/medicamento según el ejemplo anterior)

// Paso 4: Creación de la colección "compuestos"
// Esta colección almacena los datos maestros de los compuestos, con validaciones estrictas para garantizar que cada compuesto tenga un nombre.

db.createCollection("compuestos", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["nombre"],
            properties: {
                nombre: {
                    bsonType: "string",
                    description: "Debe ser una cadena que representa el nombre del compuesto"
                }
            }
        }
    },
    validationLevel: "strict",
    validationAction: "error"
});

// Inserción de datos en "compuestos"
// Aquí se agregan ejemplos de compuestos para ilustrar cómo se llena la colección con datos maestros.

db.compuestos.insertMany([
    { _id: ObjectId("681a37b87d76855ca6732d98"), nombre: "Acetaminofén" },
    { _id: ObjectId("681a37b87d76855ca6732d99"), nombre: "Cetirizina" },
    // (Agregar más compuestos según el ejemplo anterior)
]);

// Paso 5: Creación de la colección "medicamentos"
// Esta colección almacena los datos maestros de los medicamentos, incluyendo su nombre y fabricante.

db.createCollection("medicamentos", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["nombre", "fabricante"],
            properties: {
                nombre: {
                    bsonType: "string",
                    description: "Debe ser una cadena que representa el nombre del medicamento"
                },
                fabricante: {
                    bsonType: "string",
                    description: "Debe ser una cadena que representa el fabricante del medicamento"
                }
            }
        }
    },
    validationLevel: "strict",
    validationAction: "error"
});

// Inserción de datos en "medicamentos"
// Aquí se agregan ejemplos de medicamentos con sus fabricantes.

db.medicamentos.insertMany([
    { _id: ObjectId("681a388f7d76855ca6732da1"), nombre: "Noxpirin", fabricante: "Laboratorios Siegried" },
    { _id: ObjectId("681a388f7d76855ca6732da2"), nombre: "Dolex", fabricante: "GlaxoSmithKline" },
    { _id: ObjectId("681a388f7d76855ca6732da3"), nombre: "Advil", fabricante: "Pfizer" }
]);

// Nota final: Este script incluye la creación de usuarios, colecciones y la inserción de datos iniciales para facilitar la administración y consulta de medicamentos y sus compuestos.