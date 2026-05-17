def calcular_idade(ano_nascimento):
    idade = 2026 - ano_nascimento
    return idade

def main():
    ano = int(input("Digite o seu ano de nascimento: "))
    idade_calculada = calcular_idade(ano)
    print(f"A idade calculada é: {idade_calculada} anos.")

main()