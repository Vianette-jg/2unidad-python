def contar_ocurrencias(lista):
    elemento = int(input("¿Qué elemento deseas buscar en la lista? "))
    conteo = lista.count(elemento)
    print(f"El elemento {elemento} se repite {conteo} veces en la lista.")

def eliminar_duplicados(lista):
    lista_sin_duplicados = list(set(lista))  # Convertimos a conjunto para eliminar duplicados y luego volvemos a lista
    print(f"Lista sin elementos duplicados: {lista_sin_duplicados}")

def mostrar_menu():
    lista = []
    while True:
        print("\n--- Menú ---")
        print("1. Agregar elementos a la lista")
        print("2. Contar ocurrencias de un elemento")
        print("3. Eliminar elementos duplicados")
        print("4. Mostrar lista actual")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nums = input("Ingresa los números separados por espacio: ")
            # Convertimos la cadena en una lista de enteros
            lista.extend([int(num) for num in nums.split()])
            print(f"Se agregaron {nums} a la lista.")
        elif opcion == "2":
            if len(lista) == 0:
                print("La lista está vacía, primero debes agregar elementos.")
            else:
                contar_ocurrencias(lista)
        elif opcion == "3":
            if len(lista) == 0:
                print("La lista está vacía, primero debes agregar elementos.")
            else:
                eliminar_duplicados(lista)
        elif opcion == "4":
            print(f"Lista actual: {lista}")
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor selecciona una opción correcta.")

# Ejecutar el menú
mostrar_menu()
