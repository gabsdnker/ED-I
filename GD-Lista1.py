class NoLista:
    def __init__(self, dado):
        self.dado = dado
        self.nextNoLista = None

    def getDado(self):
        return self.dado

    def setDado(self, dado):
        self.dado = dado

    def getNextNoLista(self):
        return self.nextNoLista

    def setNextNoLista(self, nextNoLista):
        self.nextNoLista = nextNoLista

    def __str__(self):
        return str(self.dado)

class Lista:
    def __init__(self):
        self.firstNoLista = None
        self.lastNoLista = None

    def insertAtFirstNoLista(self, valor):
        newNoLista = NoLista(valor)
        if self.isEmpty():
            self.firstNoLista = self.lastNoLista = newNoLista
        else:
            newNoLista.setNextNoLista(self.firstNoLista)
            self.firstNoLista = newNoLista

    def removeFirstNode(self):
        if self.isEmpty():
            raise (IndexError, 'Lista vazia!')
        popValor = self.firstNoLista.getDado()
        if self.firstNoLista == self.lastNoLista:
            self.firstNoLista = self.lastNoLista = None
        else:
            self.firstNoLista = self.firstNoLista.getNextNoLista()
        return popValor

    def isEmpty(self):
        return self.firstNoLista is None

    def __str__(self):
        string = ''
        valor = self.firstNoLista
        while valor is not None:
            string = string + str(valor.getDado()) + ' -> '
            valor = valor.getNextNoLista()
        return string
    
    def insertAtLastNode(self, valor):
        newNoLista = NoLista(valor)
        print(self)
        if self.isEmpty():
            self.firstNoLista = self.lastNoLista = newNoLista
        else:
            self.lastNoLista.setNextNoLista(newNoLista)
            self.lastNoLista = newNoLista

newList = Lista()
newList.insertAtLastNode(5)
newList.insertAtLastNode(4)
newList.insertAtLastNode(3)
newList.insertAtLastNode(2)
newList.insertAtLastNode(1)
print(newList)
