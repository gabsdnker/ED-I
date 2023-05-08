#Nome: Gabrielli Danker
import sys
class NoArvoreBinaria:
    def __init__(self, info):
        self.info = info
        self.sae = None
        self.sad = None


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None
        
    def insere(self, valor):
        novo_no = NoArvoreBinaria(valor)
        
        if self.raiz is None:
            self.raiz = novo_no
        else:
            atual = self.raiz
            while True:
                if valor < atual.info:
                    if atual.sae is None:
                        atual.sae = novo_no
                        break
                    else:
                        atual = atual.sae
                else:
                    if atual.sad is None:
                        atual.sad = novo_no
                        break
                    else:
                        atual = atual.sad
                        
    def vazia(self):
        return self.raiz is None
    
    def __str__(self):
        def pre_ordem(no):
            if no is None:
                return ""
            return str(no.info) + " " + pre_ordem(no.sae) + pre_ordem(no.sad)

        return pre_ordem(self.raiz)
    
    def pertence(self, valor):
        def busca_valor(no, valor):
            if no is None:
                return False
            if no.info == valor:
                return True
            return busca_valor(no.sae, valor) or busca_valor(no.sad, valor)

        return busca_valor(self.raiz, valor)
    
    def pares(self):
        def pares_recursivo(no):
            if no is None:
                return 0

            qtd_pares_esquerda = pares_recursivo(no.sae)
            qtd_pares_direita = pares_recursivo(no.sad)

            if no.info % 2 == 0:
                return qtd_pares_esquerda + qtd_pares_direita + 1
            else:
                return qtd_pares_esquerda + qtd_pares_direita

        return pares_recursivo(self.raiz)

    
    def folhas(self, no):
        if no is None:
            return 0
        elif no.sae is None and no.sad is None:
            return 1
        else:
            return self.folhas(no.sae) + self.folhas(no.sad)
    
    def imprimePre(self, no=None):
        if no is None:
            no = self.raiz
        if no is not None:
            print(no.info, end=" ")
            if no.sae is not None:
                self.imprimePre(no.sae)
            if no.sad is not None:
                self.imprimePre(no.sad)

    def imprimeSim(self, no=None):
        if no is None:
            no = self.raiz
        if no is not None:
            if no.sae is not None:
                self.imprimeSim(no.sae)
            print(no.info, end=" ")
            if no.sad is not None:
                self.imprimeSim(no.sad)

    def imprimePos(self, no=None):
        if no is None:
            no = self.raiz
        if no is not None:
            if no.sae is not None:
                self.imprimePos(no.sae)
            if no.sad is not None:
                self.imprimePos(no.sad)
            print(no.info, end=" ")
            
    def numNos(self):
        return self._numNosRecursivo(self.raiz)
    def _numNosRecursivo(self, no):
        if no is None:
            return 0
        else:
            return 1 + self._numNosRecursivo(no.sae) + self._numNosRecursivo(no.sad)

def main():
    arvore = ArvoreBinaria()
    arvore.insere(2)
    arvore.insere(6)
    arvore.insere(1)
    arvore.insere(3)
    arvore.insere(5)
    arvore.insere(7)
    print('Árvore binária:')
    arvore.imprimePre()
    print('Número de nós:', arvore.numNos())
    print('Quantidade de nós folhas:', arvore.folhas(arvore.raiz))
    print('Quantidade de nós pares:', arvore.pares())
    print('O valor 6 pertence à árvore?', arvore.pertence(6))
    print('O valor 8 pertence à árvore?', arvore.pertence(8))
    print('Impressão pré-ordem:')
    arvore.imprimePre()
    print('Impressão in-ordem:')
    arvore.imprimeSim()
    print('Impressão pós-ordem:')
    sys.setrecursionlimit(20000) # novo limite de recursão
    arvore.imprimePos()

if __name__ == '__main__':
    main()