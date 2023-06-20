#Nome: Gabrielli Danker
#Matéria: Estrutura de Dados I
#Data: 20/06/2023

#Tabela Hash

class Aluno:
    def __init__(self, nome, matricula, media_geral):
        self.nome = nome
        self.matricula = matricula
        self.media_geral = media_geral
        self.prox = None  #referência ao próximo aluno na lista encadeada

class TabelaHash:
    def __init__(self, N):
        self.N = N
        self.tabela = [None] * N  #inicializa a tabela como uma lista de tamanho N, com todos os elementos como None

    def hash(self, k):
        return k % self.N  #função de dispersão que calcula o índice na tabela a partir da chave k

    def get(self, k):
        index = self.hash(k)  #calcula o índice na tabela
        aluno = self.tabela[index]  #obtém o primeiro aluno na posição index

        while aluno:
            if aluno.matricula == k:  #verifica se a matrícula do aluno é igual à chave k
                return aluno  #retorna o aluno encontrado
            aluno = aluno.prox  #avança para o próximo aluno na lista encadeada

        return None  #retorna None se o aluno não for encontrado

    def set(self, nome, matricula, media_geral):
        index = self.hash(matricula)  #calcula o índice na tabela
        aluno = self.tabela[index]  #obtém o primeiro aluno na posição index

        while aluno:
            if aluno.matricula == matricula:  #verifica se a matrícula do aluno é igual à matrícula passada
                aluno.nome = nome  #atualiza os dados do aluno existente na tabela
                aluno.media_geral = media_geral
                return
            aluno = aluno.prox  #avança para o próximo aluno na lista encadeada

        novo_aluno = Aluno(nome, matricula, media_geral)  #cria um novo aluno
        novo_aluno.prox = self.tabela[index]  #define o próximo aluno como o atual primeiro aluno na posição index
        self.tabela[index] = novo_aluno  #insere o novo aluno na tabela

    def remove(self, k):
        index = self.hash(k)  #calcula o índice na tabela
        aluno = self.tabela[index]  #obtém o primeiro aluno na posição index
        anterior = None  #referência ao aluno anterior

        while aluno:
            if aluno.matricula == k:  #verifica se a matrícula do aluno é igual à chave k
                if anterior:
                    anterior.prox = aluno.prox  #remove o aluno atualizando o próximo do aluno anterior
                else:
                    self.tabela[index] = aluno.prox  #remove o primeiro aluno da tabela
                return
            anterior = aluno  #atualiza o aluno anterior
            aluno = aluno.prox  #avança para o próximo aluno na lista encadeada

    def __str__(self):
        result = ""
        for i in range(self.N):
            result += f"Índice {i}: "
            aluno = self.tabela[i]
            while aluno:
                result += f"{aluno.nome} -> "  #concatena o nome do aluno na representação da tabela
                aluno = aluno.prox  #avança para o próximo aluno na lista encadeada
            result += "None\n"  #indica o fim da lista encadeada para o índice atual
        return result


def main():
    tabela = TabelaHash(10)
    tabela.set("João", 12345, 8.5)  # Insere o aluno "João" com matrícula 12345 e média 8.5
    tabela.set("Maria", 54321, 9.0)  # Insere o aluno "Maria" com matrícula 54321 e média 9.0
    tabela.set("Pedro", 98765, 7.2)  # Insere o aluno "Pedro" com matrícula 98765 e média 7.2

    print(tabela)  #imprime a representação da tabela

    aluno = tabela.get(54321)  #busca o aluno com matrícula 54321
    if aluno:
        print(f"Aluno encontrado: {aluno.nome}")  #imprime o nome do aluno encontrado
    else:
        print("Aluno não encontrado.")

    tabela.remove(54321)  #remove o aluno com matrícula 54321
    print(tabela)  #imprime a representação atualizada da tabela


if __name__ == "__main__":
    main()

