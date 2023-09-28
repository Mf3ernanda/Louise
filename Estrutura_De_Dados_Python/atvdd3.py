#Questão 1
def calcular_media(notas):
    return sum(notas) / len(notas)

notas = []
for i in range(5):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

media = calcular_media(notas)

if media >= 7:
    print(f"Média: {media:.2f}. Aluno aprovado!")
else:
    print(f"Média: {media:.2f}. Aluno reprovado.")

#Questão 2
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

#Questão 3
def e_palindromo(frase):
    frase = frase.lower().replace(" ", "").replace(",", "").replace(".", "")
    return frase == frase[::-1]

frase = input("Digite uma palavra ou frase: ")
if e_palindromo(frase):
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")

#Questão 4
def soma_digitos(numero):
    return sum(int(digito) for digito in str(numero))

numero = int(input("Digite um número inteiro positivo: "))
if numero >= 0:
    resultado = soma_digitos(numero)
    print(f"A soma dos dígitos de {numero} é: {resultado}")
else:
    print("Digite um número inteiro positivo.")

#Questão 5
def e_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = int(input("Digite um número: "))
if e_primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")

#Questão 6
def contar_vogais(frase):
    vogais = "aeiouAEIOU"
    return sum(1 for char in frase if char in vogais)

frase = input("Digite uma string: ")
resultado = contar_vogais(frase)
print(f"A quantidade de vogais na string é: {resultado}")

#Questão 7
def calcular_imc(peso, altura):
    return peso / (altura**2)

peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))
imc = calcular_imc(peso, altura)
print(f"Seu IMC é: {imc:.2f}")

#Questão 8
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

opcao = input("Escolha a conversão (Celsius para Fahrenheit - 'CF' ou Fahrenheit para Celsius - 'FC'): ")

if opcao == "CF":
    celsius = float(input("Digite a temperatura em Celsius: "))
    resultado = celsius_para_fahrenheit(celsius)
    print(f"A temperatura em Fahrenheit é: {resultado:.2f}°F")
elif opcao == "FC":
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    resultado = fahrenheit_para_celsius(fahrenheit)
    print(f"A temperatura em Celsius é: {resultado:.2f}°C")
else:
    print("Opção inválida. Escolha 'CF' ou 'FC'.")

#Questão 9
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero"

print("Operações disponíveis: +, -, *, /")
operacao = input("Escolha a operação desejada: ")

if operacao in ('+', '-', '*', '/'):
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if operacao == '+':
        resultado = somar(num1, num2)
    elif operacao == '-':
        resultado = subtrair(num1, num2)
    elif operacao == '*':
        resultado = multiplicar(num1, num2)
    elif operacao == '/':
        resultado = dividir(num1, num2)
    print(f"Resultado: {resultado}")
else:
    print("Operação inválida.")

#Questão 10
def fibonacci(num_termos):
    sequencia = [0, 1]
    while len(sequencia) < num_termos:
        proximo = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo)
    return sequencia

num_termos = int(input("Digite o número de termos desejado na sequência de Fibonacci: "))
if num_termos > 0:
    resultado = fibonacci(num_termos)
    print("Sequência de Fibonacci:", resultado)
else:
    print("Digite um número positivo.")