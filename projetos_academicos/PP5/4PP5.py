def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

def main():
    num = int(input("Digite um número inteiro: "))
    resultado = verificar_par_ou_impar(num)
    print(f"O número digitado é {resultado}.")

main()