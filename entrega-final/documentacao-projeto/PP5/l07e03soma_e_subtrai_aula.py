"""            Comentários de várias linhas - Prof. Barbosa
Atalhos: Ctrl<d>, duplica linha. Ctrl<y>, apaga linha. Ctrl</>, comenta linha.

- Problema:

- Implemente um programa com duas funções defs e a função principal (main):

1- A função (def) "soma" recebe dois parâmetros (valores) inteiros, realiza
   a soma deles e retorna o resultado do cálculo.

2- A função (def) "subtrai" recebe dois parâmetros (valores) inteiros, realiza
   a subtração deles e retorna o resultado do cálculo.

3- O programa (função main) lê dois valores inteiros digitados pelo
   usuário, chama a função soma passando os dois valores lidos e
   depois chama a função subtrai passando os dois valores lidos.
   A função main recebe o valor retornado pelas funções soma e subtrai
   e gera a tela de saída com essas informações.

Teste 1: Entrada: 3 e 2         Saída: Soma = 5 e Subtração = 1
Teste 2: Entrada: 2 e 6         Saída: Soma = 8 e Subtração = -4    """

def soma(a, b):       # Recebe dois parâmetros (valores)
    somar = a + b     # Com a variável local somar
    return somar      # Retorna o resultado do cálculo para o main

def subtrai(a, b):    # Recebe dois parâmetros (valores)
    subtrair = a - b
    return subtrair

# O if abaixo indica o início da execução do programa principal (main)
if __name__ == '__main__':             # Atalho: main <tab>
    num1 = int(input("Primeiro valor inteiro: ")) # Lê os valores
    num2 = int(input("Segundo valor inteiro: "))
    retorno_soma = soma(num1, num2)     # Chama def com variável
    # A variável retorno_soma recebe o valor retornado pela função
    print("\nSoma =", retorno_soma)
    retorno_subtrai = subtrai(num1, num2) # Chama def com variável
    print("Subtração =", retorno_subtrai)
""" --- ALTERAÇÕES:
a. Refaça a funçao soma sem usar a variável dentro da funçao (variável somar)
b. Refaça o program principal (main) sem usar a variável retorno_subtrai.
   Dica: o retorno da função pode ser colocado dentro do print
    --- Dicas:
def soma(a, b):                                             # a.
    return a + b                                   
if __name__ == '__main__':                                  # b.
    ...
    # retorno_subtrai = subtrai(num1, num2)  
    # print("Subtração =", retorno_subtrai)  
    print("Subtração =", subtrai(num1, num2))           

"""
