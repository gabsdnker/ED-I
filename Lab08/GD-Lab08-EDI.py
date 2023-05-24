import random
import time

class Search:
    @staticmethod
    def linear_search(vet, element):
        for i in range(len(vet)):
            if vet[i] == element:
                return i
        return -1

    @staticmethod
    def binary_search(vet, element):
        vet.sort()
        start = 0
        end = len(vet) - 1

        while start <= end:
            middle = (start + end) // 2
            if vet[middle] == element:
                return middle
            elif vet[middle] < element:
                start = middle + 1
            else:
                end = middle - 1

        return -1

def createVetdArray(n):
    vet = random.sample(range(1, n+1), n)
    return vet

# Criação dos vetores embaralhados
vet1 = createVetdArray(101)
vet2 = createVetdArray(102)
vet3 = createVetdArray(103)
vet4 = createVetdArray(104)
vet5 = createVetdArray(105)

# Realização das buscas
element = random.choice(vet1)
start = time.time()
result = Search.linear_search(vet1, element)
time_spent = time.time() - start
print("Linear Search - Vector 1: Element", element, "- Index:", result, "- Elapsed Time:", time_spent)

element = random.choice(vet2)
start = time.time()
result = Search.linear_search(vet2, element)
time_spent = time.time() - start
print("Linear Search - Vector 2: Element", element, "- Index:", result, "- Elapsed Time:", time_spent)

element = random.choice(vet3)
start = time.time()
result = Search.binary_search(vet3, element)
time_spent = time.time() - start
print("Binary Search - Vector 3: Element", element, "- Index:", result, "- Elapsed Time:", time_spent)

element = random.choice(vet4)
start = time.time()
result = Search.binary_search(vet4, element)
time_spent = time.time() - start
print("Binary Search - Vector 4: Element", element, "- Index:", result, "- Elapsed Time:", time_spent)

element = random.choice(vet5)
start = time.time()
result = Search.binary_search(vet5, element)
time_spent = time.time() - start
print("Binary Search - Vector 5: Element", element, "- Index:", result, "- Elapsed Time:", time_spent)
