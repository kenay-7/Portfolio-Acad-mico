def verificar_nota(nota):
    if nota >= 6:
        return "Aprovado"
    else:
        return "Reprovado"


def main():
    nota_aluno = float(input("Digite a nota do aluno: "))

    resultado = verificar_nota(nota_aluno)

    print("Resultado:", resultado)


main()