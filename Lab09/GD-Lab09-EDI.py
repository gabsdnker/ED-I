#Data: 13/06/2023
#Author: Gabrielli Danker   Matéria: Estrutura de Dados I
#Árvore Binária de Busca

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def busca(self, v):
        return self.busca_recursiva(self.raiz, v)

    def busca_recursiva(self, no, v):
        if no is None or no.getInfo() == v:
            return no
        if v < no.getInfo():
            return self.busca_recursiva(no.getEsq(), v)
        return self.busca_recursiva(no.getDir(), v)

    def insere(self, v):
        self.raiz = self.insere_recursiva(self.raiz, v)

    def insere_recursiva(self, no, v):
        if no is None:
            return NoArvoreBinaria(v)
        if v < no.getInfo():
            no.setEsq(self.insere_recursiva(no.getEsq(), v))
        else:
            no.setDir(self.insere_recursiva(no.getDir(), v))
        return no

    def retira(self, v):
        self.raiz = self.retira_recursiva(self.raiz, v)

    def retira_recursiva(self, no, v):
        if no is None:
            return no
        if v < no.getInfo():
            no.setEsq(self.retira_recursiva(no.getEsq(), v))
        elif v > no.getInfo():
            no.setDir(self.retira_recursiva(no.getDir(), v))
        else:
            if no.getEsq() is None:
                return no.getDir()
            elif no.getDir() is None:
                return no.getEsq()
            else:
                sucessor = self.encontra_sucessor(no.getDir())
                no.setInfo(sucessor.getInfo())
                no.setDir(self.retira_recursiva(no.getDir(), sucessor.getInfo()))
        return no

    def encontra_sucessor(self, no):
        while no.getEsq() is not None:
            no = no.getEsq()
        return no

    def toString(self):
        return self.em_ordem(self.raiz)

    def em_ordem(self, no):
        if no is None:
            return ''
        return self.em_ordem(no.getEsq()) + str(no.getInfo()) + ' ' + self.em_ordem(no.getDir())


class NoArvoreBinaria:
    def __init__(self, info, esq=None, dir=None):
        self.info = info
        self.esq = esq
        self.dir = dir

    def setInfo(self, info):
        self.info = info

    def getInfo(self):
        return self.info

    def setEsq(self, esq):
        self.esq = esq

    def getEsq(self):
        return self.esq

    def setDir(self, dir):
        self.dir = dir

    def getDir(self):
        return self.dir

    def toString(self):
        return str(self.info)


def main():
    try:
        arvore = ArvoreBinariaBusca()

        arvore.insere(10)
        arvore.insere(20)
        arvore.insere(14)
        arvore.insere(4)
        arvore.insere(2)
        arvore.insere(1)
        arvore.insere(9)
        arvore.insere(8)

        print(arvore.busca(1).getInfo())
        print(arvore.busca(3))

        arvore.retira(1)
        print(arvore.toString())

        print(arvore.toString())
    
    except:
        print("Deu erro")


if __name__ == "__main__":
    main()
