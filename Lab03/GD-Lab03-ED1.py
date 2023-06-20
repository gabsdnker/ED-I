#Author: Gabrielli Danker   Matéria: Estrutura de Dados I
#Lista Simplismente Encadeada 

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
    
    def retira(self, v): #remove o primeiro nó com valor v da lista, se existir.
        if self.prim == None:
            return
        if self.prim.getInfo() == v:
            self.prim = self.prim.getProx()
            return
        ant = self.prim
        p = self.prim.getProx()
        while p != None:
            if p.getInfo() == v:
                ant.setProx(p.getProx())
                return
            ant = p
            p = p.getProx()
    
    def libera(self): #remove todos os nós da lista e libera a memória ocupada.
        p = self.prim
        while p != None:
            temp = p.getProx()
            del p
            p = temp
        self.prim = None
    
    def insereFim(self, v): #insere um novo nó com valor v no final da lista.
        novo = NoLista()
        novo.setInfo(v)
        if self.prim == None:
            self.prim = novo
            return
        ult = self.ultimo()
        ult.setProx(novo)
    
    def igual(self, l): #verifica se a lista é igual à lista l passada como parâmetro.
        p1 = self.prim
        p2 = l.prim
        while p1 != None and p2 != None:
            if p1.getInfo() != p2.getInfo():
                return False
            p1 = p1.getProx()
            p2 = p2.getProx()
        return p1 == None and p2 == None
    
    def imprimeRecursivo(self): #imprime os valores da lista de forma recursiva.
        self.imprimeRecursivoAux(self.prim)
        print()
    
    def imprimeRecursivoAux(self, l): 
        if l != None:
            print(l.getInfo(), end=" ")
            self.imprimeRecursivoAux(l.getProx())
    
    def retiraRecursivo(self, v): #remove o primeiro nó com valor v da lista de forma recursiva.
        self.prim = self.retiraRecursivoAux(self.prim, v)
     
    def retiraRecursivoAux(self, l, v): #
        if l == None:
            return None
        if l.getInfo() == v:
            temp = l.getProx()
            del l
            return temp
        l.setProx(self.retiraRecursivoAux(l.getProx(), v))
        return l
    
    def igualRecursivo(self, l): #verifica se a lista é igual à lista l passada como parâmetro de forma recursiva.
        return self.igualRecursivoAux(self.prim, l.prim)
    
    def igualRecursivoAux(self, l1, l2):
        if l1 == None and l2 == None:
            return

