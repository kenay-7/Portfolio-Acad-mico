def somar_valores(a, b, c):
    soma = a + b + c
    return soma


def main():
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    valor3 = int(input("Digite o terceiro valor: "))

    resultado = somar_valores(valor1, valor2, valor3)

    print("Resultado da soma:", resultado)


main()