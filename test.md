# Pruebas de la API

Este archivo describe cómo realizar pruebas de la API del proyecto utilizando tres métodos diferentes:
1. **curl**: Herramienta de línea de comandos para enviar solicitudes HTTP.
2. **Postman**: Aplicación gráfica para probar APIs.



## Pruebas con curl

### ¿Qué es curl?
`curl` es una herramienta de línea de comandos que te permite realizar solicitudes HTTP hacia servidores web. Es ideal para probar APIs de forma rápida y sencilla.

### Requisitos previos
1. Asegúrate de tener `curl` instalado en tu sistema:
   - En Linux y macOS, normalmente ya está instalado.
   - En Windows, puedes usar PowerShell o Git Bash, o instalarlo desde [https://curl.se/](https://curl.se/).


2. Asegúrate de que tu servidor de la API esté corriendo en `http://localhost:8000` o en la dirección correspondiente.

---

### Paso a paso: Cómo usar curl
1. Abre una terminal en tu sistema operativo.
2. Copia y pega uno de los comandos proporcionados según la prueba que quieras realizar.
3. Ejecuta el comando y revisa la respuesta que muestra la terminal.

> **IMPORTANTE**: Los comandos a continuación utilizan IDs específicos de un ejemplo (`6823b1a42a5aee01b32e32f7` para medicamentos y `6823aa63f3cf615116ff400e` para compuestos). Para tus propias pruebas, deberás reemplazar estos IDs con los valores generados por tu base de datos al crear nuevos recursos. Los IDs se obtienen de las respuestas de los comandos de creación (POST).

---

### Comandos de prueba con curl

#### **1. Crear un compuesto**
Este comando crea un nuevo compuesto en la base de datos.

```bash
curl -X POST http://localhost:8000/api/compuestos -H "Content-Type: application/json" -d "{\"nombre\": \"CompuestoPrueba\"}"
```
## Captura de la respuesta
![Post Compuesto](https://drive.google.com/uc?id=16xYJRL8znqvBgZ1w3Z0yxXFkgUVcQ-b3)
---

#### **2. Ver todos los compuestos**
Este comando obtiene todos los compuestos registrados en la base de datos.

```bash
curl -X GET http://localhost:8000/api/compuestos

```
## Captura de la respuesta
![Get Compuestos](https://drive.google.com/uc?id=192ZPYrTT4ng48eVKx36DMAwsLmKrPYnO)

#### **3. Crear un medicamento**
Este comando crea un nuevo medicamento en la base de datos.

```bash
curl -X POST http://localhost:8000/api/medicamentos -H "Content-Type: application/json" -d "{\"nombre\": \"MedicamentoPrueba\", \"fabricante\": \"FabricantePrueba\"}"

```
## Captura de la respuesta
![Post Medicamento](https://drive.google.com/uc?id=1Ls_wbTpsTHF0GIkL5vBmRgqNg-vCrG12)


#### **4. Asignar un compuesto a un medicamento**
Este comando asigna un compuesto existente a un medicamento.

```bash
curl -X POST http://localhost:8000/api/medicamentos/compuesto -H "Content-Type: application/json" -d "{\"medicamento_id\": \"6823b1a42a5aee01b32e32f7\", \"compuesto_id\": \"6823aa63f3cf615116ff400e\", \"concentracion\": \"10\", \"unidad_medida\": \"mg\"}"
```
## Captura de la respuesta
![Post Medicamento Compuesto](https://drive.google.com/uc?id=122f5xYHk5lcIhai4Qgkc5kZkVsE2maAu)

#### **5. Ver todos los medicamentos**
Este comando obtiene todos los medicamentos registrados en la base de datos.

```bash
curl -X GET http://localhost:8000/api/medicamentos
```
## Captura de la respuesta
![Get Medicamentos](https://drive.google.com/uc?id=1tlJTWIKhRDWm-mFVj6QTdkSj-yKAsE-c)

#### **6. Eliminar un medicamento**
Este comando elimina un medicamento específico de la base de datos.

```bash
curl -X DELETE http://localhost:8000/api/medicamentos/6823b1a42a5aee01b32e32f7
```
## Captura de la respuesta
![Delete Medicamento](https://drive.google.com/uc?id=1QclQzNT7Eh_3oy-UMSrRGysYfnZQ3RIx)

#### **7. Eliminar un compuesto**
Este comando elimina un compuesto específico de la base de datos.

```bash
curl -X DELETE http://localhost:8000/api/compuestos/6823aa63f3cf615116ff400e
```

## Captura de la respuesta

![Delete Compuesto](https://drive.google.com/uc?id=1YfvJAvrBdE1o5DPzvlBhHx2JSy3Npr4g)

---

## Pruebas con Postman

### ¿Qué es Postman?
Postman es una herramienta gráfica que simplifica la interacción con APIs. Permite realizar solicitudes HTTP (GET, POST, PUT, DELETE, etc.) de manera visual e intuitiva, además de guardar las pruebas dentro de colecciones organizadas.

---

### Requisitos previos
1. Descarga e instala Postman desde [https://www.postman.com/downloads/](https://www.postman.com/downloads/).
2. Asegúrate de que tu servidor de la API esté corriendo en `http://localhost:8000` o en la dirección correspondiente.

---

### Paso a paso: Cómo usar Postman para probar la API

#### **1. Configurar una colección**
1. Abre Postman.
2. Haz clic en el botón **"Collections"** en la barra lateral izquierda.
3. Haz clic en **"New Collection"** para crear una nueva colección y así organizar tus pruebas. Ponle un nombre, por ejemplo: `Pruebas API Medicamentos`.

---

#### **2. Agregar solicitudes HTTP**
Cada solicitud representa una operación que deseas probar en tu API (por ejemplo, GET, POST, PUT, DELETE). A continuación se describen las pruebas comunes:

#### **Prueba 1: Ver todos los compuestos**
1. Dentro de tu colección, haz clic en **"Add a request"**.
2. Ponle un nombre a la solicitud, como `Ver Compuestos`.
3. Selecciona el tipo de solicitud `GET` en el menú desplegable.
4. Escribe la URL: `http://localhost:8000/api/compuestos`.
5. Haz clic en **"Send"**.
6. Verifica que la respuesta sea una lista de compuestos registrados.

## Captura de la respuesta
![GET Compuestos](https://drive.google.com/uc?id=1w5WE6N3RPxsDdKjg9GLqv144mlMTTYh8)

---

#### **Prueba 2: Crear un nuevo medicamento**
1. Dentro de tu colección, haz clic en **"Add a request"**.
2. Ponle un nombre a la solicitud, como `Crear Medicamento`.
3. Selecciona el tipo de solicitud `POST` en el menú desplegable.
4. Escribe la URL: `http://localhost:8000/api/medicamentos`.
5. Ve a la pestaña **"Body"**:
    - Selecciona **"raw"**.
    - Cambia el formato a **JSON**.
    - Escribe lo siguiente:
      ```json
      {
         "nombre": "Ibuprofeno",
         "fabricante": "Laboratorio XYZ"
      }
      ```
6. Haz clic en **"Send"**.

## Captura de la respuesta
![Crear Nuevo Medicamento](https://drive.google.com/uc?id=1xa83xE-aLGU7OI1NlluK4VAgPeyCJMp9)

---



#### **Prueba 3: Asignar un compuesto a un medicamento**
1. Dentro de tu colección, haz clic en **"Add a request"**.
2. Ponle un nombre a la solicitud, como `Asignar Compuesto a Medicamento`.
3. Selecciona el tipo de solicitud `POST` en el menú desplegable.
4. Escribe la URL: `http://localhost:8000/api/medicamentos/compuesto`.
5. Ve a la pestaña **"Body"**:
    - Selecciona **"raw"**.
    - Cambia el formato a **JSON**.
    - Escribe lo siguiente:
      ```json
         {
         "medicamento_id": "6823fcb160ee48657e6950af",
         "compuesto_id": "681a37b87d76855ca6732d9a",
         "concentracion": "10",
         "unidad_medida": "mg"
      }
      ```
6. Haz clic en **"Send"**.

## Captura de la respuesta
![Asignar Compuesto a Medicamento](https://drive.google.com/uc?id=1GrtPjH2KRS4tL4pzN1xI64kLZkNRiXcx)
---




#### **Prueba 4: Ver todos los medicamentos**
1. Dentro de tu colección, haz clic en **"Add a request"**.
2. Ponle un nombre a la solicitud, como `Ver Medicamentos`.
3. Selecciona el tipo de solicitud `GET` en el menú desplegable.
4. Escribe la URL: `http://localhost:8000/api/medicamentos`.
5. Haz clic en **"Send"**.
6. Verifica que la respuesta sea una lista de medicamentos registrados.

## Captura de la respuesta
![GET Medicamentos](https://drive.google.com/uc?id=1k8PQZ1X3faKxzPKNpm5SuHz1fBqGgDWQ)

---



#### **Prueba 5: Eliminar un medicamento**
1. Dentro de tu colección, haz clic en **"Add a request"**.
2. Ponle un nombre a la solicitud, como `Eliminar Medicamento`.
3. Selecciona el tipo de solicitud `DELETE` en el menú desplegable.
4. Escribe la URL: `http://localhost:8000/api/medicamentos/6823fcb160ee48657e6950af`.
5. Haz clic en **"Send"**.

    ```
## Captura de la respuesta
![Delete Medicamento](https://drive.google.com/uc?id=12cWsCuLZFp29hAAHPTihGAaQ8DSi2l3Q)

---




#### **Prueba 6: Eliminar un compuesto**
1. Dentro de tu colección, haz clic en **"Add a request"**.
2. Ponle un nombre a la solicitud, como `Eliminar Compuesto`.
3. Selecciona el tipo de solicitud `DELETE` en el menú desplegable.
4. Escribe la URL: `http://localhost:8000/api/compuestos/681a5e5b7de31c5396b02e7e`.
5. Haz clic en **"Send"**.

## Captura de la respuesta
![Delete Compuesto](https://drive.google.com/uc?id=12cWsCuLZFp29hAAHPTihGAaQ8DSi2l3Q)
