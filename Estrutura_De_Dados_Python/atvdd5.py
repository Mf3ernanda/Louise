#-------------------------------------------------

#Questão 1:

import numpy as np
import random
import time

class Listasequencial:


p1 = Listasequencial(10000)


vetor = [random.randint(1, 10000) for _ in range(10000)]


inicio = time.time()
for num in vetor:
    p1.insere(num)
fim = time.time()

tempo_gasto = fim - inicio
print(f'Tempo gasto para ordenar o vetor: {tempo_gasto:.6f} segundos')

#-------------------------------------------------

#Questão 2: Fila
#Questão 3: Pilha

#-------------------------------------------------

#Questão 4:

class Pilha:
    def _init_(self):
        self.itens = []

    def vazia(self):
        return len(self.itens) == 0

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.vazia():
            return self.itens.pop()
        else:
            return None

    def topo(self):
        if not self.vazia():
            return self.itens[-1]
        else:
            return None

def encontra_operadores(expressao):
    operadores = set("+-*/^")
    pilha = Pilha()
    lista_operadores = []

    for caractere in expressao:
        if caractere in operadores:
            lista_operadores.append(caractere)

    return lista_operadores

expressao = "(2+3)*(8-9)/(7^3)"
operadores_encontrados = encontra_operadores(expressao)

print(f"Operadores na expressão '{expressao}': {operadores_encontrados}")

#-------------------------------------------------

#Questão 5:

class Pilha:
    def _init_(self):
        self.itens = []

    def vazia(self):
        return len(self.itens) == 0

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.vazia():
            return self.itens.pop()
        else:
            return None

    def topo(self):
        if not self.vazia():
            return self.itens[-1]
        else:
            return None

def encontra_vogais(palavra):
    vogais = "AEIOUaeiou"
    pilha = Pilha()
    vogais_encontradas = set()

    for letra in palavra:
        if letra in vogais and letra not in vogais_encontradas:
            vogais_encontradas.add(letra)
            pilha.empilhar(letra)

    return list(pilha.itens)

palavra = "Disciplina"
vogais_presentes = encontra_vogais(palavra)

print(f"Vogais na palavra '{palavra}': {vogais_presentes}")

#-------------------------------------------------

#Questão 6:


# a. O primeiro elemento da fila é 2 após as operações de enfileiramento e desenfileiramento.
# b. O último elemento da fila é 1 após as operações de enfileiramento e desenfileiramento.
# c. Após as operações de enfileiramento e desenfileiramento, a fila contém 2 elementos.

#-------------------------------------------------

#Questão 7:

# a. A classe contém três métodos.
# b. São necessários três atributos.
# c. O nome do método construtor é _init_