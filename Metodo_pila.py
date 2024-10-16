class Historial:
    def __init__(self):
        self.pila = []

    def agregar_registro(self, url, fecha_hora):
        registro = {'url': url, 'fecha_hora': fecha_hora}
        self.pila.append(registro)
        print(f"Registro agregado: {registro}")

    def eliminar_registro(self):
        try:
            eliminado = self.pila.pop()
            print(f"Registro eliminado: {eliminado}")
        except IndexError:
            print("No hay registros para eliminar.")

    def mostrar_historial(self):
        if self.pila:
            print("Historial:")
            for registro in reversed(self.pila):
                print(f"{registro['fecha_hora']}: {registro['url']}")
        else:
            print("El historial está vacío.")

# Ejemplo de uso
if __name__ == "__main__":
    historial = Historial()

    while True:
        print("\nOpciones:")
        print("1. Agregar registro")
        print("2. Eliminar último registro")
        print("3. Mostrar historial")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            url = input("Ingresa la URL: ")
            fecha_hora = input("Ingresa la fecha y hora (YYYY-MM-DD HH:MM:SS): ")
            historial.agregar_registro(url, fecha_hora)
        elif opcion == '2':
            historial.eliminar_registro()
        elif opcion == '3':
            historial.mostrar_historial()
        elif opcion == '4':
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

