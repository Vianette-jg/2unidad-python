class Colas:
    def __init__(self):
        self.lista = []  # Inicializamos una lista vacía

    def agregar(self, elemento):
        self.lista.append(elemento)  # Agregamos elementos al final de la lista

    def front(self):
        if self.lista:
            return self.lista[0]  # Devolver el primer elemento
        else:
            return None  # Si la lista está vacía, devolvemos None

    def back(self):
        if self.lista:
            return self.lista[-1]  # Devolver el último elemento
        else:
            return None  # Si la lista está vacía, devolvemos None

# Ejemplo de uso:
cola = Colas()
cola.agregar(10)
cola.agregar(20)
cola.agregar(30)

print("Primer elemento:", cola.front())  # Debería imprimir 10
print("Último elemento:", cola.back())  # Debería imprimir 30
