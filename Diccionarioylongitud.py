longitud = int(input("Ingresa la cantidad de nombres que deseas agregar: "))

# Crear un diccionario vacío
dicc = {}

# Agregar nombres al diccionario
for i in range(longitud):
    nombre = input(f"Ingrese el nombre {i + 1}: ")
    dicc[f"nombre_{i + 1}"] = nombre

# Mostrar el contenido del diccionario
print("\nNombres ingresados:")
for clave, valor in dicc.items():
    print(f"{clave}: {valor}")

# Función para eliminar un nombre específico del diccionario
def eliminar(dicc, clave):
    if clave in dicc:
        del dicc[clave]
        print(f"Elemento eliminado: {clave}")
    else:
        print(f"La clave '{clave}' no existe en el diccionario.")

# Permitir al usuario eliminar elementos hasta que decida terminar
while True:
    print("\nContenido actual del diccionario:")
    for clave, valor in dicc.items():
        print(f"{clave}: {valor}")
    
    opcion = input("\n¿Deseas eliminar algún nombre? (si/no): ").lower()
    if opcion == "no":
        break
    elif opcion == "si":
        clave = input("Ingresa la clave del nombre que deseas eliminar (por ejemplo, nombre_1): ")
        eliminar(dicc, clave)
    else:
        print("Opción no válida. Intenta de nuevo.")

# Mostrar el diccionario final
print("\nDiccionario final:")
for clave, valor in dicc.items():
    print(f"{clave}: {valor}")