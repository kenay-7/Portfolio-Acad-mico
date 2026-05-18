def calcular_idade(ano_nascimento):
    idade = 2026 - ano_nascimento
    return idade


def main():
    ano = int(input("Digite seu ano de nascimento: "))

    idade = calcular_idade(ano)

    print("Sua idade é:", idade, "anos")


main()