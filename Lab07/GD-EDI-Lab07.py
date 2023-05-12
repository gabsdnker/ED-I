#Nome: Gabrielli Danker                                                                                  
                                                                                     
class NoArvore:
    def __init__(self, info):
        self.info = info
        self.prim = None
        self.prox = None

    def setInfo(self, info):
        self.info = info

    def getInfo(self):
        return self.info

    def setPrim(self, prim):
        self.prim = prim

    def getPrim(self):
        return self.prim

    def setProx(self, prox):
        self.prox = prox

    def getProx(self):
        return self.prox

    def toString(self):
        return str(self.info)

class Arvore:
    def __init__(self):
        self.raiz = self.criaNo(None)

    def criaNo(self, info):
        return NoArvore(info)

    def insereFilho(self, no, sa):
        if no.getPrim() == None:
            no.setPrim(sa)
        else:
            p = no.getPrim()
            while p.getProx() != None:
                p = p.getProx()
            p.setProx(sa)

    def toString(self):
        if self.raiz == None:
            return "Arvore vazia"
        else:
            return self.imprime(self.raiz)

    def imprime(self, no):
        resultado = ""
        resultado += "<" + no.toString()
        p = no.getPrim()
        while p != None:
            resultado += " " + self.imprime(p)
            p = p.getProx()
        resultado += ">"
        return resultado

    def pertence(self, info):
        if self.raiz == None:
            return False
        else:
            return self.pertenceRec(self.raiz, info)

    def pertenceRec(self, no, info):
        if no.getInfo() == info:
            return True
        else:
            p = no.getPrim()
            while p != None:
                if self.pertenceRec(p, info):
                    return True
                p = p.getProx()
            return False

    def altura(self):
        if self.raiz == None:
            return -1
        else:
            return self.alturaRec(self.raiz)

    def alturaRec(self, no):
        if no.getPrim() == None:
            return 0
        else:
            p = no.getPrim()
            alturaMax = 0
            while p != None:
                altura = self.alturaRec(p)
                if altura > alturaMax:
                    alturaMax = altura
                p = p.getProx()
            return alturaMax + 1

    def pares(self):
        if self.raiz == None:
            return 0
        else:
            return self.paresRec(self.raiz)

    def paresRec(self, no):
        pares = 0
        if no.getInfo() % 2 == 0:
            pares += 1
        p = no.getPrim()
        while p != None:
            pares += self.paresRec(p)
            p = p.getProx()
        return pares

    def folhas(self):
        if self.raiz == None:
            return 0
        else:
            return self.folhasRec(self.raiz)

    def folhasRec(self, no):
        if no.getPrim() == None:
            return 1
        else:
            p = no.getPrim()
            folhas = 0
            while p != None:
                folhas += self.folhasRec(p)
                p = p.getProx()
            return folhas

def main():
    # Creating a tree with the root node containing the value 1
    arvore = Arvore()
    raiz = arvore.criaNo(1)
    arvore.raiz = raiz

    # Adding child nodes to the root node
    no2 = arvore.criaNo(2)
    no3 = arvore.criaNo(3)
    arvore.insereFilho(raiz, no2)
    arvore.insereFilho(raiz, no3)

    # Adding child nodes to node 2
    no4 = arvore.criaNo(4)
    no5 = arvore.criaNo(5)
    arvore.insereFilho(no2, no4)
    arvore.insereFilho(no2, no5)

    # Adding child nodes to node 3
    no6 = arvore.criaNo(6)
    no7 = arvore.criaNo(7)
    no8 = arvore.criaNo(8)
    arvore.insereFilho(no3, no6)
    arvore.insereFilho(no3, no7)
    arvore.insereFilho(no3, no8)

    print("Árvore criada:")
    print(arvore)

    # Testing the 'pertence' method
    print("O valor 6 pertence à árvore?", arvore.pertence(6))
    print("O valor 9 pertence à árvore?", arvore.pertence(9))

    # Testing the 'altura' method
    print("Altura da árvore:", arvore.altura())

    # Testing the 'pares' method
    print("Número de nós pares na árvore:", arvore.pares())

    # Testing the 'folhas' method
    print("Número de folhas na árvore:", arvore.folhas())

if __name__ == '__main__':
    main()
