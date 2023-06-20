#Author: Gabrielli Danker   Matéria: Estrutura de Dados I
#Lista Duplamente Encadeadas

class NoListaDupla:
    def __init__(self, info, ant=None, prox=None): #
        self.info = info #the value stored in the node.
        self.ant = ant #a reference to the previous node.
        self.prox = prox #a reference to the next node.

class ListaDupla:
    def __init__(self):  #constructor method that initializes an empty Doubly Linked List.
        self.prim = None
        self.ult = None
        self._comprimento = 0

    def insere(self, v): #inserts a new node with value v at the beginning of the list.
        novo_no = NoListaDupla(v)
        if self.vazia():
            self.prim = novo_no
            self.ult = novo_no
        else:
            novo_no.prox = self.prim
            self.prim.ant = novo_no
            self.prim = novo_no
        self._comprimento += 1

    def insereFim(self, v): #inserts a new node with value v at the end of the list.
        novo_no = NoListaDupla(v)
        if self.vazia():
            self.prim = novo_no
            self.ult = novo_no
        else:
            novo_no.ant = self.ult
            self.ult.prox = novo_no
            self.ult = novo_no
        self._comprimento += 1

    def imprime(self): #prints the list's values from the first to the last node.
        atual = self.prim
        while atual != None:
            print(atual.info, end=" ")
            atual = atual.prox
        print()

    def vazia(self): #returns a boolean indicating if the list is empty or not.
        return self.prim == None

    def busca(self, v): #searches for the first node with value v and returns it. If no such node is found, it returns null.
        atual = self.prim
        while atual != None and atual.info != v:
            atual = atual.prox
        return atual

    def comprimento(self): #returns the length of the list (the number of nodes).
        return self._comprimento

    def ultimo(self): #returns the last node of the list.
        return self.ult

    def retira(self, v): #removes the first node with value v from the list, if it exists.
        no_remover = self.busca(v)
        if no_remover != None:
            if no_remover.ant == None:
                self.prim = no_remover.prox
            else:
                no_remover.ant.prox = no_remover.prox
            if no_remover.prox == None:
                self.ult = no_remover.ant
            else:
                no_remover.prox.ant = no_remover.ant
            self._comprimento -= 1

    def libera(self): #deallocates all nodes of the list.
        atual = self.prim
        while atual != None:
            proximo = atual.prox
            del atual
            atual = proximo
        self.prim = None
        self.ult = None
        self._comprimento = 0

    def igual(self, l): #compares the list to another list l and returns true if they have the same values in the same order, false otherwise.
        if self.comprimento() != l.comprimento():
            return False
        atual1 = self.prim
        atual2 = l.prim
        while atual1 != None:
            if atual1.info != atual2.info:
                return False
            atual1 = atual1.prox
            atual2 = atual2.prox
        return True

    def merge(self, l): #appends the list l to the end of the current list.
        nova_lista = ListaDupla()
        atual = self.prim
        while atual != None:
            nova_lista.insereFim(atual.info)
            atual = atual.prox
        atual = l.prim
        while atual != None:
            nova_lista.insereFim(atual.info)
            atual = atual.prox
        return nova_lista
    
def main():
    # Cria um objeto da classe ListaDupla
    list = ListaDupla()

    # Insere valores na lista
    list.insere(10)
    list.insere(20)
    list.insere(30)

    # Imprime a lista
    list.imprime() # Output: 30 20 10

    # Remove um valor da lista
    list.retira(20)

    # Imprime a lista novamente
    list.imprime() # Output: 30 10

    # Insere um valor no fim da lista
    list.insereFim(40)

    # Imprime a lista mais uma vez
    list.imprime() # Output: 30 10 40

if __name__== "__main__":
        main()
   
#Uma lista duplamente encadeada é uma estrutura de dados que permite o armazenamento de uma sequência de elementos, cada um dos quais é representado 
#por um nó contendo um valor e referências para o nó anterior e o nó seguinte.
#Em Python, é possível implementar uma lista duplamente encadeada utilizando uma classe que representa cada nó da lista e uma classe que representa 
#a própria lista.

## The symbols + and - before the method and attribute names, respectively, may indicate the visibility of these members.
#In some languages, + may indicate public visibility, and - may indicate private visibility.
# Finally, the variables prim, prox, and ant seem to be private attributes of the ListaDupla and NoListaDupla classes, respectively, 
#but there's not enough information to determine their exact purpose without seeing the implementation code.
