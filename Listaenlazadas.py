class Nodo:
    def __init__(self,dato):
        self.dato= dato
        self.next= None

class lista:
    def _init_(self):
        self.head= None

    def final(self, dato):
        new_nodo = Nodo(dato)

        if self.head is None:
            self.head= new_nodo
        else:
            last= self.head
            while last.next:
                last = last.next
            last.next = new_nodo


    def imprimir_lista(self):
        last = self.head
        while last:
            print(last.dato, end=" -> ")
            last = last.next
        print("None")

if  __name__== "_main_":
    lista= lista()

lista.final(4)
lista.final(4)
lista.final(6)
lista.final(3)
lista.imprimir_lista()