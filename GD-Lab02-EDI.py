#Data: 22/03/2023
#Author: Gabrielli Danker   Matéria: Estrutura de Dados I
#Lista Simplesmente Encadeada 


class NoLista:
    def __init__(self, info=None, prox=None):
        self._info = info
        self._prox = prox
    
    def getInfo(self): #retorna o valor armazenado no nó.
        return self._info
    
    def setInfo(self, info): #define o valor armazenado no nó.
        self._info = info
    
    def getProx(self): #retorna o nó seguinte.
        return self._prox
    
    def setProx(self, prox): #define o nó seguinte.
        self._prox = prox

class Lista:
    def __init__(self): #método construtor que inicializa a lista vazia.
        self.prim = None
    
    def insere(self, v): #insere um novo nó com valor v no início da lista.
        novo = NoLista()
        novo.setInfo(v)
        novo.setProx(self.prim)
        self.prim = novo
    
    def imprime(self): #imprime os valores da lista.
        p = self.prim
        while p != None:
            print(p.getInfo(), end=" ")
            p = p.getProx()
        print()
    
    def vazia(self): #retorna True se a lista está vazia, False caso contrário.
        return self.prim == None
    
    def busca(self, v): #busca o valor v na lista e retorna o primeiro nó encontrado, ou None caso não exista.
        p = self.prim
        while p != None:
            if p.getInfo() == v:
                return p
            p = p.getProx()
        return None
    
    def comprimento(self): #retorna o comprimento da lista (número de nós).
        p = self.prim
        cont = 0
        while p != None:
            cont += 1
            p = p.getProx()
        return cont
    
    def ultimo(self): #retorna o último nó da lista.
        p = self.prim
        if p == None:
            return None
        while p.getProx() != None:
            p = p.getProx()
        return p
    
 def main():
    list= Lista()
    list.insere(1)
    list.insere(2)
    list.insere(3)
    list.insere(4)
    list.insere(5)
    list.imprime()
    print(list.busca(2))
    print(list.busca(0))
    print(list.comprimento())
    print(list.ultimo())
   
if __name__== "__main__":
    main()
