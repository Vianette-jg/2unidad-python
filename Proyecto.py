
usuarios = {
    "admin": "password123",    # Ejemplo de usuario con contraseña inicial
    "usuario1": "pass1",
    "usuario2": "pass2",
}

biblioteca = {}  # Diccionario para almacenar los libros

def login():
    print("Inicia sesión")
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")
    
    # Verificación directa de la contraseña sin restricciones de formato
    if usuarios.get(usuario) == contrasena:
        print("Inicio de sesión exitoso. Bienvenido a la biblioteca pública de I2C.")
        return True
    else:
        print("Datos incorrectos. Inténtalo de nuevo.")
        return False

def agregar_libro():
    print("\n--- Agregar Libro ---")
    titulo = input("Título del libro: ")
    autor = input("Autor del libro: ")
    anio = input("Año de publicación: ")
    
    # Guardar los detalles del libro en el diccionario
    biblioteca[titulo] = {
        "autor": autor,
        "anio": anio
    }
    print(f"Libro '{titulo}' agregado exitosamente.")

def buscar_libro():
    print("\n--- Buscar Libro ---")
    titulo = input("Ingrese el título del libro a buscar: ")
    
    if titulo in biblioteca:
        detalles = biblioteca[titulo]
        print(f"Detalles del libro '{titulo}':")
        print(f"Autor: {detalles['autor']}")
        print(f"Año de publicación: {detalles['anio']}")
    else:
        print("El libro no existe en la biblioteca.")

def main():
    if login():
        while True:
            print("\n--- Menú de Biblioteca ---")
            print("1. Agregar Libro")
            print("2. Buscar Libro")
            print("3. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                agregar_libro()
            elif opcion == "2":
                buscar_libro()
            elif opcion == "3":
                print("Saliendo del sistema. ¡Hasta pronto!")
                break
            else:
                print("Opción inválida. Inténtalo de nuevo.")

main()
