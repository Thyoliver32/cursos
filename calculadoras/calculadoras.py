# Calculadora completa em Python

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def menu():
    print("\n=== CALCULADORA ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

while True:
    menu()
    escolha = input("Escolha a operação (0-4): ")

    if escolha == '0':
        print("Encerrando a calculadora. Até mais!")
        break

    if escolha in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: entrada inválida. Use números válidos.")
            continue

        if escolha == '1':
            resultado = somar(num1, num2)
        elif escolha == '2':
            resultado = subtrair(num1, num2)
        elif escolha == '3':
            resultado = multiplicar(num1, num2)
        elif escolha == '4':
            resultado = dividir(num1, num2)

        print(f"Resultado: {resultado}")
    else:
        print("Opção inválida. Tente novamente.")
