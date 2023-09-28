#Questão 1
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

media = (num1 + num2 + num3) / 3

print(f"A média dos três números é: {media}")

#Questão 2
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"{numero} é um número par.")
else:
    print(f"{numero} é um número ímpar.")

#Questão 3
limite = int(input("Digite um número: "))

for i in range(limite + 1):
    if i % 2 == 0:
        print(i)

#Questão 4
numeros = [int(x) for x in input("Digite uma lista de números separados por espaço: ").split()]

maior = max(numeros)
menor = min(numeros)

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")

#Questão 5
numeros = [int(x) for x in input("Digite uma lista de números separados por espaço: ").split()]

numeros_pares = [num for num in numeros if num % 2 == 0]

if numeros_pares:
    media = sum(numeros_pares) / len(numeros_pares)
    print(f"A média dos números pares é: {media}")
else:
    print("Não há números pares na lista.")

#Questão 6
def calcular_fatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

numero = int(input("Digite um número inteiro positivo: "))

if numero >= 0:
    resultado = calcular_fatorial(numero)
    print(f"O fatorial de {numero} é: {resultado}")
else:
    print("Digite um número inteiro positivo.")

#Questão 7
def fibonacci(n):
    fib = [0, 1]
    while fib[-1] + fib[-2] <= n:
        fib.append(fib[-1] + fib[-2])
    return fib

limite = int(input("Digite um valor limite para a sequência de Fibonacci: "))
sequencia = fibonacci(limite)

print("Sequência de Fibonacci até", limite, ":", sequencia)

#Questão 8
def is_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = int(input("Digite um número: "))

if is_primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")

#Questão 9
nomes = input("Digite uma lista de nomes separados por espaço: ").split()

nomes_com_a = [nome for nome in nomes if nome.startswith('A')]

print("Nomes que começam com 'A':", nomes_com_a)

#Questão 10
import random

def jogo_pedra_papel_tesoura(escolha_usuario):
    opcoes = ["pedra", "papel", "tesoura"]
    escolha_computador = random.choice(opcoes)
    
    print(f"Computador escolheu: {escolha_computador}")
    print(f"Você escolheu: {escolha_usuario}")
    
    if escolha_usuario == escolha_computador:
        return "Empate"
    elif (escolha_usuario == "pedra" and escolha_computador == "tesoura") or (escolha_usuario == "papel" and escolha_computador == "pedra") or (escolha_usuario == "tesoura" and escolha_computador == "papel"):
        return "Você venceu!"
    else:
        return "Computador venceu!"

escolha_usuario = input("Escolha pedra, papel ou tesoura: ").lower()

if escolha_usuario in ["pedra", "papel", "tesoura"]:
    resultado = jogo_pedra_papel_tesoura(escolha_usuario)
    print(resultado)
else:
    print("Escolha inválida. Por favor, escolha pedra, papel ou tesoura.")