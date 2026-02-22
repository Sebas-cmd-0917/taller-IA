# 🧪 Taller: Construcción de un Programa en Python usando Diccionarios y Persistencia en JSON mediante Prompts

## 📌 Contexto del taller

En el desarrollo de software moderno, saber **formular correctamente un problema** y **guiar a una IA mediante prompts claros** es tan importante como programar. En este taller, el estudiante no solo programará en Python, sino que **aprenderá a diseñar prompts efectivos** para obtener soluciones correctas, mantenibles y bien estructuradas.

------

## 🎯 Objetivo general

Que el estudiante sea capaz de:

- Diseñar **prompts claros y precisos**
- Construir un programa en **Python**
- Usar **diccionarios** como estructura principal de datos
- Implementar **persistencia en archivos JSON**
- Aplicar **manejo básico de errores**
- Comprender la relación entre *prompt → solución generada*

------

## 👥 Público objetivo

- Estudiantes de programación (nivel básico – intermedio)
- Cursos introductorios de Python
- Talleres de Prompt Engineering aplicado a código

------

## 🛠️ Requisitos técnicos

- Python 3.10+
- Editor de texto o IDE (VS Code recomendado)
- Conocimientos previos:
  - Diccionarios en Python
  - Funciones
  - Uso básico de archivos

------

## 📦 Problema a resolver

Se debe construir un **programa de consola en Python** que permita gestionar información usando **diccionarios**, con las siguientes características:

### 📂 Dominio del problema (ejemplo)

Sistema de gestión de **contactos** / **productos** / **estudiantes**
 *(el docente puede elegir uno)*

Cada registro debe contener al menos:

- Identificador único
- Nombre
- Un atributo adicional (correo, precio, edad, etc.)

La información debe:

- Guardarse en un **diccionario**
- Persistirse en un **archivo JSON**
- Recuperarse al reiniciar el programa

------

## 🧩 Estructura del taller (por retos)

------

## 🧠 Reto 1: Comprensión del problema mediante prompt

### 📌 Instrucción al estudiante

Redacta un prompt que le pida a una IA **explicar el problema** y **proponer una solución general en Python**.

### 🧾 Prompt esperado (ejemplo)

```


Actúa como un profesor de programación. Explícame paso a paso cómo puedo construir un programa de consola en Python para gestionar estudiantes (ID, nombre, curso). 
El programa debe usar diccionarios para guardar la información en memoria y archivos JSON para guardar los datos en el disco duro. 
Dame una visión general teórica de cómo debería ser el flujo del programa, sin darme el código completo todavía.

```

### ✅ Resultado esperado

- Explicación del uso de diccionarios
- Explicación de lectura/escritura de JSON
- Flujo general del programa

```


¡Hola! Me parece una excelente iniciativa. Como tu profesor, te digo que este es uno de los mejores proyectos que puedes hacer para consolidar tus conocimientos. Combina lógica de control (menús), estructuras de datos (diccionarios) y persistencia de datos (archivos JSON).

Antes de escribir una sola línea de código, los programadores siempre planeamos la arquitectura de nuestro software. Vamos a desglosar teóricamente cómo debe fluir tu programa, paso a paso.

### 1. La Estructura de los Datos (El "Modelo")

Primero, debemos imaginar cómo vivirá la información en la memoria RAM de la computadora mientras el programa esté abierto. Para esto usaremos un **diccionario de diccionarios**.

* **La llave principal:** Será el ID del estudiante (ya que el ID es único y no se repite).
* **El valor:** Será *otro* diccionario que contenga el "nombre" y el "curso".

Visualmente, en tu mente, los datos se verán así:

> `ID_101` -> `{ Nombre: "Ana", Curso: "Matemáticas" }`
> `ID_102` -> `{ Nombre: "Luis", Curso: "Historia" }`

### 2. El Flujo del Programa (Paso a Paso)

#### Paso A: Inicialización y Carga de Datos

Cuando el usuario ejecuta el programa, lo primero que este debe hacer es intentar recuperar la memoria de sesiones anteriores.

1. El programa busca en tu disco duro un archivo llamado, por ejemplo, `estudiantes.json`.
2. **Si el archivo existe:** El programa lee su contenido, lo traduce de formato JSON a un diccionario de Python y lo guarda en una variable en la memoria RAM.
3. **Si el archivo NO existe (es la primera vez que se usa):** El programa simplemente crea un diccionario vacío en la memoria RAM para empezar a trabajar desde cero.

#### Paso B: El Bucle Principal (El Menú)

Una vez cargados los datos, el programa entra en un ciclo infinito (un bucle `while`) que mantendrá el programa vivo hasta que el usuario decida salir. En cada vuelta del ciclo, se muestra un menú:

1. Agregar un nuevo estudiante.
2. Ver la lista de estudiantes.
3. Salir del programa.

#### Paso C: Ejecución de las Opciones (La Lógica)

Dependiendo de lo que elija el usuario en el menú, el programa toma un camino distinto:

* **Si elige "Agregar":**
1. El programa pide por consola que el usuario escriba el ID, el Nombre y el Curso.
2. Verifica que el ID no exista ya en nuestro diccionario de la memoria (¡no queremos estudiantes duplicados!).
3. Si todo está bien, inserta estos datos en el diccionario que está en la memoria RAM.
4. **El paso crucial:** Inmediatamente después de actualizar el diccionario, el programa toma ese diccionario, lo convierte a formato JSON y sobrescribe el archivo `estudiantes.json` en el disco duro. Así, si se va la luz un segundo después, los datos ya están a salvo.


* **Si elige "Ver lista":**
1. El programa verifica si el diccionario está vacío. Si es así, avisa que no hay estudiantes.
2. Si hay datos, el programa recorre el diccionario en la memoria RAM y va imprimiendo de forma amigable la información de cada estudiante en la pantalla.


* **Si elige "Salir":**
1. El programa se despide y "rompe" el ciclo principal, finalizando la ejecución.



---

Este es el esqueleto conceptual de tu aplicación. Comprender esto es el 80% del trabajo; el código es solo la herramienta para construirlo.

¿Te queda clara esta lógica de funcionamiento? Si es así, **¿te gustaría que empecemos a programar el Paso A (la carga del archivo JSON) para ir construyéndolo juntos poco a poco?**






```



------

## 🧠 Reto 2: Prompt para estructura de datos

### 📌 Instrucción

Crea un prompt que solicite a la IA **definir la estructura del diccionario principal**.

### 🧾 Prompt esperado

```
Escribe el código Python que defina la estructura de datos principal para este sistema de estudiantes. 
Usa un diccionario anidado donde la clave principal sea el ID del estudiante (como un string) y el valor sea otro diccionario con las claves 'nombre' y 'curso'. 
Muéstrame un ejemplo inicializando la variable con un par de registros ficticios.
```

### ✅ Resultado esperado

- Diccionario anidado
- Claves bien definidas
- Identificación del `id` como clave principal

````

¡Excelente! Es el momento perfecto para pasar de la arquitectura teórica a la implementación real.

Aquí tienes exactamente cómo se traduce el modelo que diseñamos a código Python. Fíjate muy bien en la sintaxis: usamos llaves `{}` para definir los diccionarios, y dos puntos `:` para separar cada clave de su respectivo valor.

```python
# Definimos la variable principal que almacenará nuestros datos en la memoria RAM
estudiantes = {
    "1001": {
        "nombre": "Laura Martínez",
        "curso": "Introducción a la Programación"
    },
    "1002": {
        "nombre": "Diego Gómez",
        "curso": "Bases de Datos"
    },
    "1003": {
        "nombre": "Sofía Castro",
        "curso": "Desarrollo Web"
    }
}

# Ejemplo rápido de cómo acceder a la información:
# Si queremos saber el nombre del estudiante con ID "1002":
# print(estudiantes["1002"]["nombre"])  -> Esto imprimiría "Diego Gómez"

```

### ¿Por qué elegimos esta estructura?

* **Búsqueda instantánea:** En Python, buscar una clave (como `"1002"`) en un diccionario es una operación extremadamente rápida. El programa va directo al dato sin tener que revisar a los demás estudiantes uno por uno.
* **Compatibilidad nativa:** La estructura de un diccionario en Python es prácticamente idéntica a la estructura de un archivo de texto JSON. Esto significa que cuando nos toque guardar o cargar datos, la traducción será casi automática.

---

Ahora que ya tenemos nuestra base de datos inicializada en la memoria con un par de registros ficticios, ya tenemos material con el cual trabajar.

**¿Te gustaría que escribamos primero una función sencilla para imprimir la lista de estos estudiantes de forma amigable en la consola, o prefieres que pasemos directamente a programar la función para guardar este diccionario en un archivo JSON en tu disco duro?**


````



------

## 🧠 Reto 3: Prompt para persistencia en JSON

### 📌 Instrucción

Diseña un prompt que le pida a la IA **crear funciones para guardar y cargar datos desde un archivo JSON**.

### 🧾 Prompt esperado

```
Crea dos funciones en Python: `guardar_datos(datos, nombre_archivo)` y `cargar_datos(nombre_archivo)`. 
La primera debe guardar el diccionario de estudiantes en un archivo JSON usando la librería `json` y `json.dump()`. 
La segunda debe leer el archivo con `json.load()` y devolver el diccionario. Es vital que manejes el error `FileNotFoundError` en la segunda función, devolviendo un diccionario vacío si el archivo aún no existe.

```

### ✅ Resultado esperado

- Uso de `json.dump`
- Uso de `json.load`
- Manejo de `FileNotFoundError`

````
¡Vas por un camino excelente! Como tu profesor, me enorgullece que hayas pensado en el `FileNotFoundError`. Ese es el tipo de mentalidad preventiva que separa a los principiantes de los desarrolladores profesionales.

Para lograr esta comunicación entre la memoria RAM y tu disco duro, Python nos ofrece la librería integrada `json`. El proceso de convertir nuestro diccionario a un texto JSON se llama **serialización** (`json.dump`), y el proceso inverso es la **deserialización** (`json.load`).

Aquí tienes la implementación paso a paso de ambas funciones:

```python
import json

def guardar_datos(datos, nombre_archivo):
    """
    Toma un diccionario de Python y lo guarda en un archivo JSON en el disco duro.
    """
    # Usamos 'with open' porque cierra el archivo automáticamente al terminar, 
    # incluso si ocurre un error. La 'w' significa modo escritura (write).
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        # json.dump escribe los datos. 
        # indent=4 le da un formato bonito y legible al archivo JSON.
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
    
    # Imprimimos un mensaje silencioso en consola solo para confirmar (opcional)
    # print(f"Datos guardados exitosamente en {nombre_archivo}")

def cargar_datos(nombre_archivo):
    """
    Intenta leer un archivo JSON y convertirlo a un diccionario de Python.
    Si el archivo no existe, devuelve un diccionario vacío.
    """
    try:
        # La 'r' significa modo lectura (read).
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            return datos
            
    except FileNotFoundError:
        # ¡Aquí está la magia! Si es la primera vez que abrimos el programa 
        # y el archivo aún no existe, no el programa no se "cae", simplemente
        # empezamos con una base de datos limpia.
        return {}

```

### Detalles técnicos importantes que debes notar:

* **El bloque `with open(...)`:** Es una buena práctica fundamental. Garantiza que el archivo se libere de la memoria de tu computadora tan pronto como terminemos de leerlo o escribirlo.
* **`encoding='utf-8'` y `ensure_ascii=False`:** Como estamos escribiendo en español, es muy probable que los nombres o los cursos tengan tildes o la letra "ñ" (por ejemplo, "Matemáticas"). Estos parámetros aseguran que el archivo JSON guarde esos caracteres correctamente y no como símbolos extraños.
* **`indent=4`:** Si abres el archivo `.json` con un bloc de notas, verás que el texto está tabulado y es fácil de leer para un humano, en lugar de estar todo en una sola línea infinita.
* **Manejo de Excepciones (`try...except`):** En lugar de que tu programa colapse con letras rojas la primera vez que alguien lo use, interceptamos el error y respondemos de manera elegante entregando un diccionario vacío (`{}`).

---

Con esto, nuestro sistema ya tiene "memoria a largo plazo". Ya podemos guardar a los estudiantes para siempre y recuperarlos al día siguiente.

Ahora que tenemos las bases de datos y las funciones para guardar/cargar listas, **¿quieres que construyamos el bucle principal `while` y el menú interactivo para que el usuario pueda empezar a interactuar con el sistema?**

````



------

## 🧠 Reto 4: Prompt para menú interactivo

### 📌 Instrucción

Formula un prompt para crear un **menú de consola** que permita interactuar con el sistema.

### 🧾 Prompt esperado

```
Escribe el código para un menú interactivo en consola usando un bucle `while True`. 
El menú debe tener 3 opciones: 1. Agregar estudiante, 2. Mostrar estudiantes, 3. Salir. 
Usa la función `input()` para capturar la opción del usuario. En la opción 1, pide el ID, nombre y curso, agrégalos al diccionario y llama a la función de guardar. En la opción 3, usa `break` para salir.
```

### ✅ Resultado esperado

- Menú con `while`
- Uso de `input`
- Llamado a funciones

````
¡Excelente trabajo! Llegamos a la pieza central de tu programa: el controlador. Como tu profesor, te explico que aquí es donde el usuario y la máquina conversan.

El bucle `while True` actuará como el "corazón" de tu aplicación, latiendo infinitamente hasta que el usuario decida apagarlo con el comando `break`.

Aquí tienes el código de nuestro menú interactivo. He añadido la carga inicial de los datos y una pequeña validación en la Opción 1 para evitar que se sobrescriban estudiantes si se ingresa un ID repetido (una buena práctica profesional).

```python
# Definimos el nombre de nuestro archivo
ARCHIVO_DATOS = "estudiantes.json"

# PASO A: Antes de entrar al bucle, cargamos la "memoria" pasada
estudiantes = cargar_datos(ARCHIVO_DATOS)

# PASO B: Iniciamos el bucle principal (el corazón del programa)
while True:
    print("\n" + "="*35)
    print(" 🎓 SISTEMA DE GESTIÓN ESCOLAR 🎓")
    print("="*35)
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Salir")
    print("="*35)
    
    # Capturamos la decisión del usuario
    opcion = input("Elige una opción (1, 2 o 3): ")
    
    # PASO C: Lógica de las opciones
    if opcion == '1':
        print("\n--- Agregar Nuevo Estudiante ---")
        id_est = input("Introduce el ID del estudiante: ")
        
        # Verificamos que el ID no exista ya en nuestro diccionario
        if id_est in estudiantes:
            print("⚠️ ¡Error! Ya existe un estudiante registrado con ese ID.")
        else:
            nombre = input("Introduce el nombre del estudiante: ")
            curso = input("Introduce el curso: ")
            
            # 1. Actualizamos el diccionario en la memoria RAM
            estudiantes[id_est] = {
                "nombre": nombre,
                "curso": curso
            }
            
            # 2. Guardamos inmediatamente en el disco duro
            guardar_datos(estudiantes, ARCHIVO_DATOS)
            print(f"✅ ¡Estudiante '{nombre}' agregado y guardado con éxito!")

    elif opcion == '2':
        print("\n--- Lista de Estudiantes ---")
        # Si el diccionario está vacío, avisamos al usuario
        if len(estudiantes) == 0:
            print("📂 Aún no hay estudiantes registrados.")
        else:
            # Recorremos el diccionario usando .items() para obtener la clave y el valor
            for id_estudiante, info in estudiantes.items():
                print(f"🔹 ID: {id_estudiante} | Nombre: {info['nombre']} | Curso: {info['curso']}")

    elif opcion == '3':
        print("\n👋 Saliendo del programa... ¡Hasta pronto!")
        # El break "rompe" el ciclo while y termina la ejecución
        break

    else:
        # Si el usuario escribe "4", "hola" o cualquier otra cosa
        print("❌ Opción no válida. Por favor, intenta de nuevo.")

```

### ¿Qué está pasando aquí? (Notas del profesor)

1. **`input()` siempre devuelve texto (strings):** Por eso validamos con `'1'`, `'2'` y `'3'` entre comillas, y no con números enteros `1`. Además, guardar los IDs como texto (strings) es ideal por si un estudiante tiene un ID como `"0045"`, ya que como número entero el sistema borraría los ceros a la izquierda.
2. **`for id_estudiante, info in estudiantes.items():`**: Esta es la forma más "Pythonica" de leer un diccionario. Nos entrega al mismo tiempo la llave (el ID) y el valor (el sub-diccionario con nombre y curso), permitiéndonos imprimir todo en una sola línea formateada (usando las `f-strings`).
3. **El guardado síncrono:** Fíjate que llamamos a `guardar_datos()` *inmediatamente* después de agregar al estudiante en la Opción 1. Esto asegura que nunca se pierda un dato recién ingresado.

¡Felicidades! Si juntas las funciones de carga/guardado que hicimos en el paso anterior con este bucle, **ya tienes un programa completo y funcional**.

¿Qué te parece? ¿Te gustaría hacer alguna prueba ejecutando este flujo mentalmente o quieres que le agreguemos alguna funcionalidad extra, como poder eliminar o actualizar a un estudiante existente?

````

------

## 🧠 Reto 5: Integración final mediante prompt maestro

### 📌 Instrucción

Construye un **prompt maestro** que integre todo el sistema.

### 🧾 Prompt maestro esperado

````
¡Excelente trabajo! Llegamos a la pieza central de tu programa: el controlador. Como tu profesor, te explico que aquí es donde el usuario y la máquina conversan.

El bucle `while True` actuará como el "corazón" de tu aplicación, latiendo infinitamente hasta que el usuario decida apagarlo con el comando `break`.

Aquí tienes el código de nuestro menú interactivo. He añadido la carga inicial de los datos y una pequeña validación en la Opción 1 para evitar que se sobrescriban estudiantes si se ingresa un ID repetido (una buena práctica profesional).

```python
# Definimos el nombre de nuestro archivo
ARCHIVO_DATOS = "estudiantes.json"

# PASO A: Antes de entrar al bucle, cargamos la "memoria" pasada
estudiantes = cargar_datos(ARCHIVO_DATOS)

# PASO B: Iniciamos el bucle principal (el corazón del programa)
while True:
    print("\n" + "="*35)
    print(" 🎓 SISTEMA DE GESTIÓN ESCOLAR 🎓")
    print("="*35)
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Salir")
    print("="*35)
    
    # Capturamos la decisión del usuario
    opcion = input("Elige una opción (1, 2 o 3): ")
    
    # PASO C: Lógica de las opciones
    if opcion == '1':
        print("\n--- Agregar Nuevo Estudiante ---")
        id_est = input("Introduce el ID del estudiante: ")
        
        # Verificamos que el ID no exista ya en nuestro diccionario
        if id_est in estudiantes:
            print("⚠️ ¡Error! Ya existe un estudiante registrado con ese ID.")
        else:
            nombre = input("Introduce el nombre del estudiante: ")
            curso = input("Introduce el curso: ")
            
            # 1. Actualizamos el diccionario en la memoria RAM
            estudiantes[id_est] = {
                "nombre": nombre,
                "curso": curso
            }
            
            # 2. Guardamos inmediatamente en el disco duro
            guardar_datos(estudiantes, ARCHIVO_DATOS)
            print(f"✅ ¡Estudiante '{nombre}' agregado y guardado con éxito!")

    elif opcion == '2':
        print("\n--- Lista de Estudiantes ---")
        # Si el diccionario está vacío, avisamos al usuario
        if len(estudiantes) == 0:
            print("📂 Aún no hay estudiantes registrados.")
        else:
            # Recorremos el diccionario usando .items() para obtener la clave y el valor
            for id_estudiante, info in estudiantes.items():
                print(f"🔹 ID: {id_estudiante} | Nombre: {info['nombre']} | Curso: {info['curso']}")

    elif opcion == '3':
        print("\n👋 Saliendo del programa... ¡Hasta pronto!")
        # El break "rompe" el ciclo while y termina la ejecución
        break

    else:
        # Si el usuario escribe "4", "hola" o cualquier otra cosa
        print("❌ Opción no válida. Por favor, intenta de nuevo.")

```

### ¿Qué está pasando aquí? (Notas del profesor)

1. **`input()` siempre devuelve texto (strings):** Por eso validamos con `'1'`, `'2'` y `'3'` entre comillas, y no con números enteros `1`. Además, guardar los IDs como texto (strings) es ideal por si un estudiante tiene un ID como `"0045"`, ya que como número entero el sistema borraría los ceros a la izquierda.
2. **`for id_estudiante, info in estudiantes.items():`**: Esta es la forma más "Pythonica" de leer un diccionario. Nos entrega al mismo tiempo la llave (el ID) y el valor (el sub-diccionario con nombre y curso), permitiéndonos imprimir todo en una sola línea formateada (usando las `f-strings`).
3. **El guardado síncrono:** Fíjate que llamamos a `guardar_datos()` *inmediatamente* después de agregar al estudiante en la Opción 1. Esto asegura que nunca se pierda un dato recién ingresado.

¡Felicidades! Si juntas las funciones de carga/guardado que hicimos en el paso anterior con este bucle, **ya tienes un programa completo y funcional**.

¿Qué te parece? ¿Te gustaría hacer alguna prueba ejecutando este flujo mentalmente o quieres que le agreguemos alguna funcionalidad extra, como poder eliminar o actualizar a un estudiante existente?


````

------

## 📋 Entregables del estudiante

1. Documento con:
   - Prompts diseñados
   - Explicación breve de cada prompt
2. Código fuente en Python
3. Archivo JSON generado por el programa