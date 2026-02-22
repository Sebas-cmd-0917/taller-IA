import json

ARCHIVO_DATOS = "estudiantes.json"

def guardar_datos(datos, nombre_archivo):
    """Guarda el diccionario en un archivo JSON."""
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

def cargar_datos(nombre_archivo):
    """Carga el diccionario desde un archivo JSON, o devuelve {} si no existe."""
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

def main():
    
    estudiantes = cargar_datos(ARCHIVO_DATOS)
    
    while True:
        print("\n" + "="*35)
        print(" 🎓 SISTEMA DE GESTIÓN ESCOLAR 🎓")
        print("="*35)
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Salir")
        print("="*35)
        
        opcion = input("Elige una opción (1, 2 o 3): ")
        
        if opcion == '1':
            print("\n--- Agregar Nuevo Estudiante ---")
            id_est = input("Introduce el ID del estudiante: ")
            
            if id_est in estudiantes:
                print("⚠️ ¡Error! Ya existe un estudiante registrado con ese ID.")
            else:
                nombre = input("Introduce el nombre del estudiante: ")
                curso = input("Introduce el curso: ")
                
                # Actualizamos la memoria
                estudiantes[id_est] = {
                    "nombre": nombre,
                    "curso": curso
                }
                
                # Guardamos en el disco duro
                guardar_datos(estudiantes, ARCHIVO_DATOS)
                print(f"✅ ¡Estudiante '{nombre}' agregado y guardado con éxito!")

        elif opcion == '2':
            print("\n--- Lista de Estudiantes ---")
            if len(estudiantes) == 0:
                print("📂 Aún no hay estudiantes registrados.")
            else:
                for id_estudiante, info in estudiantes.items():
                    print(f"🔹 ID: {id_estudiante} | Nombre: {info['nombre']} | Curso: {info['curso']}")

        elif opcion == '3':
            print("\n👋 Saliendo del programa... ¡Hasta pronto!")
            break

        else:
            print("❌ Opción no válida. Por favor, intenta de nuevo.")


if __name__ == "__main__":
    main()