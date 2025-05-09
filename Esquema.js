db.createUser({
    user: "nombre_de_usuario", // Reemplaza por el nombre del usuario
    pwd: "contraseña_segura",  // Reemplaza por una contraseña segura
    roles: [
        {
            role: "readWrite",     // Permisos CRUD (lectura y escritura)
            db: "tu_base_de_datos" // Base de datos específica
        }
    ]
});


db.getUsers();

db.dropUser("nombre_de_usuario");

mongosh - u "nombre_de_usuario" - p "contraseña_segura" --authenticationDatabase "tu_base_de_datos"


use tu_base_de_datos;

db.updateUser("sebasvitz", {
    roles: [
        { role: "dbOwner", db: "tu_base_de_datos" } // Otorga control total sobre esta base de datos
    ]
});













// Creacion de Collecion de compuestos_medicamentos con validaciones.

use medicamentos_db;

// Crear la colección con validaciones
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

//  Abastecimiento de compuestos_medicamentos

db.compuestos_medicamentos.insertOne({
    compuesto_id: ObjectId("681a37b87d76855ca6732d98"), // Acetaminofén
    medicamento_id: ObjectId("681a388f7d76855ca6732da1"), // Noxpirin
    elemento: "Acetaminofén",
    concentracion: "500",
    unidad_medida: "mg"
});

db.compuestos_medicamentos.insertOne({
    compuesto_id: ObjectId("681a37b87d76855ca6732d99"), // Cetirizina
    medicamento_id: ObjectId("681a388f7d76855ca6732da1"), // Noxpirin
    elemento: "Cetirizina",
    concentracion: "5",
    unidad_medida: "mg"
});

db.compuestos_medicamentos.insertOne({
    compuesto_id: ObjectId("681a37b87d76855ca6732d9a"), // Cafeína
    medicamento_id: ObjectId("681a388f7d76855ca6732da1"), // Noxpirin
    elemento: "Cafeína",
    concentracion: "30",
    unidad_medida: "mg"
});

db.compuestos_medicamentos.insertOne({
    compuesto_id: ObjectId("681a37b87d76855ca6732d9b"), // Fenilefrina Clorhidrato
    medicamento_id: ObjectId("681a388f7d76855ca6732da1"), // Noxpirin
    elemento: "Fenilefrina Clorhidrato",
    concentracion: "10",
    unidad_medida: "mg"
});

// para dolex
db.compuestos_medicamentos.insertOne({
    compuesto_id: ObjectId("681a37b87d76855ca6732d98"), // Acetaminofén
    medicamento_id: ObjectId("681a388f7d76855ca6732da2"), // Dolex
    elemento: "Acetaminofén",
    concentracion: "500",
    unidad_medida: "mg"
});

// para advil 
db.compuestos_medicamentos.insertOne({
    compuesto_id: ObjectId("681a37b87d76855ca6732d9c"), // Ibuprofeno
    medicamento_id: ObjectId("681a388f7d76855ca6732da3"), // Advil
    elemento: "Ibuprofeno",
    concentracion: "200",
    unidad_medida: "mg"
});

db.compuestos_medicamentos.insertOne({
    compuesto_id: ObjectId("681a37b87d76855ca6732d9a"), // Cafeína
    medicamento_id: ObjectId("681a388f7d76855ca6732da3"), // Advil
    elemento: "Cafeína",
    concentracion: "30",
    unidad_medida: "mg"
});


// creacion de la colecion de compuestos con validaciones
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

// INSERCIÓN DE DATOS EN "compuestos"
db.compuestos.insertMany([
    { _id: ObjectId("681a37b87d76855ca6732d98"), nombre: "Acetaminofén" },
    { _id: ObjectId("681a37b87d76855ca6732d99"), nombre: "Cetirizina" },
    { _id: ObjectId("681a37b87d76855ca6732d9a"), nombre: "Cafeína" },
    { _id: ObjectId("681a37b87d76855ca6732d9b"), nombre: "Fenilefrina Clorhidrato" },
    { _id: ObjectId("681a37b87d76855ca6732d9c"), nombre: "Ibuprofeno" },
    { _id: ObjectId("681a37b87d76855ca6732d9d"), nombre: "Dipirona" },
    { _id: ObjectId("681a37b87d76855ca6732d9e"), nombre: "Loratadina" },
    { _id: ObjectId("681a5e5b7de31c5396b02e7e"), nombre: "lidocaina" }
]);









//creacion de la colecion de medicamentos con validaciones
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

// INSERCIÓN DE DATOS EN "medicamentos"
db.medicamentos.insertMany([
    { _id: ObjectId("681a388f7d76855ca6732da1"), nombre: "Noxpirin", fabricante: "Laboratorios Siegried" },
    { _id: ObjectId("681a388f7d76855ca6732da2"), nombre: "Dolex", fabricante: "GlaxoSmithKline" },
    { _id: ObjectId("681a388f7d76855ca6732da3"), nombre: "Advil", fabricante: "Pfizer" }
]);