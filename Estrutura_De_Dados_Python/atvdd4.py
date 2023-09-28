#Questão 1
def ordenar_selecao(vetor):
    for i in range(len(vetor)):
        min_idx = i
        for j in range(i+1, len(vetor)):
            if vetor[j] < vetor[min_idx]:
                min_idx = j
        vetor[i], vetor[min_idx] = vetor[min_idx], vetor[i]

vetor = [64, 25, 12, 22, 11]
ordenar_selecao(vetor)
print("Vetor ordenado:", vetor)

#Questão 2
def ordenar_vetor(vetor, crescente=True):
    return sorted(vetor, reverse=not crescente)

vetor = [64, 25, 12, 22, 11]
vetor_ordenado = ordenar_vetor(vetor, crescente=False)
print("Vetor ordenado em ordem decrescente:", vetor_ordenado)

#Questão 3
def encontrar_max_min(vetor):
    maximo = vetor[0]
    minimo = vetor[0]
    for elemento in vetor:
        if elemento > maximo:
            maximo = elemento
        if elemento < minimo:
            minimo = elemento
    return maximo, minimo

vetor = [64, 25, 12, 22, 11]
maximo, minimo = encontrar_max_min(vetor)
print("Máximo:", maximo)
print("Mínimo:", minimo)

#Questão 4
def selecao_ordenacao(vetor):
    n = len(vetor)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if vetor[j] < vetor[indice_minimo]:
                indice_minimo = j
        vetor[i], vetor[indice_minimo] = vetor[indice_minimo], vetor[i]

def encontrar_segundo_menor(vetor):
    selecao_ordenacao(vetor)
    return vetor[1]

vetor=[5,7,4,3]
print(encontrar_segundo_menor(vetor))
print(vetor)

#Questão 5
def remove_duplicatas(vetor):
    vetor_sd = []
    for elemento in vetor:
        if elemento not in vetor_sd:
            vetor_sd.append(elemento)
    return vetor_sd

vetor=[5,7,4,4,7,3]
print(vetor)
print(remove_duplicatas(vetor))

#Questão 6
def selecao_ordenacao(vetor):
    n = len(vetor)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if vetor[j] < vetor[indice_minimo]:
                indice_minimo = j
        vetor[i], vetor[indice_minimo] = vetor[indice_minimo], vetor[i]

def contar_par_imp(vetor):
    n = len(vetor)
    cp=0
    ci=0
    for i in range(n):
        if (vetor[i]%2==0):
            cp+=1
        else:
            ci+=1
    return cp,ci

vetor=[5,7,2,3]
selecao_ordenacao(vetor)
ct=contar_par_imp(vetor)
print(ct[0],ct[1])

#Questão 7
def selecao_ordenacao(vetor):
    n = len(vetor)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if vetor[j] < vetor[indice_minimo]:
                indice_minimo = j
        vetor[i], vetor[indice_minimo] = vetor[indice_minimo], vetor[i]

def encontrar_terceiro_maior(vetor):
    selecao_ordenacao(vetor)
    if len(vetor)<=2:
        print('Vetor menor que 3 elementos')
        return None
    return vetor[2]

vetor=[5,7,3]
print(encontrar_terceiro_maior(vetor))
print(vetor)

#Questão 8
def selecao_ordenacao(vetor):
    n = len(vetor)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if vetor[j] < vetor[indice_minimo]:
                indice_minimo = j
        vetor[i], vetor[indice_minimo] = vetor[indice_minimo], vetor[i]

def encontrar_mediana(vetor):
    vetor_ordenado = sorted(vetor)
    n = len(vetor_ordenado)
    if n % 2 == 0:
        meio1 = vetor_ordenado[n // 2 - 1]
        meio2 = vetor_ordenado[n // 2]
        return (meio1 + meio2) / 2
    else:
        return vetor_ordenado[n // 2]

vetor=[5,7,3,9]
selecao_ordenacao(vetor)
print(encontrar_mediana(vetor))
print(vetor)