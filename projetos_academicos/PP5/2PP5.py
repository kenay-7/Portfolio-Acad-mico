def somar_tres_valores(v1, v2, v3):
    soma = v1 + v2 + v3
    return soma

def main():
    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))
    n3 = int(input("Digite o terceiro valor: "))
    
    resultado = somar_tres_valores(n1, n2, n3)
    print(f"A soma dos valores é: {resultado}")

main()