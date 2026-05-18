def calcular_fatorial(n):
    if n < 0:
        return -1 
    if n == 0 or n == 1:
        return 1
    for i in range(1, n + 1):
        fatorial = fatorial * i 
    return fatorial
def main_fatorial():
    print("\n---  BORA CALCULAR FATORIAL ---")
    numero = int(input("Digite um número inteiro: "))
    resposta = calcular_fatorial(numero)
    if resposta == -1:
        print("Erro: não existe fatorial de número negativo.")
    else:
        print(f"O fatorial de {numero}! é: {resposta}")
main_fatorial()