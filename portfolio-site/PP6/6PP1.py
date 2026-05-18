def somar(n1, n2):
    resultado = n1 + n2 
    print(f"O resultado da soma é: {resultado}")
def subtrair(n1, n2):
    resultado = n1 - n2
    print(f"O resultado da subtração é: {resultado}")
def multiplicar(n1, n2):
    resultado = n1 * n2
    print(f"O resultado da multiplicação é: {resultado}")
def dividir(n1, n2):
    if n2 == 0:
        print("Vixe, erro! O professor falou que não dá pra dividir por zero.")
    else:
        resultado = n1 / n2
        print(f"O resultado da divisão é: {resultado:.2f}")
def main_calculadora():
    print("\n--- MINHA CALCULADORA ---")
    v1 = float(input("Digite o 1º número: "))
    v2 = float(input("Digite o 2º número: "))
    op = input("Qual operação você quer? (+, -, x, /): ")
    if op == '+':
        somar(v1, v2)
    elif op == '-':
        subtrair(v1, v2)
    elif op == 'x':
        multiplicar(v1, v2)
    elif op == '/':
        dividir(v1, v2)
    else:
        print("Operador errado, digita direito na próxima!")
main_calculadora()