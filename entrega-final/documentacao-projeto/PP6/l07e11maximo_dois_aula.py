"""            Comentários de várias linhas - Prof. Barbosa
Atalhos: Ctrl<d>, duplica linha. Ctrl<y>, apaga linha. Ctrl</>, comenta linha.

- Problema:

    Implemente um programa com a função (def) e a função principal (main):

    A função (def) recebe dois números inteiros como parâmetros, compara
os valores e retornar o maior valor. Se os números forem iguais, a função
retorna qualquer um deles.
    A função principal (main) lê dois números digitados pelo usuário,
chama a função passando os dois argumentos (os números lidos) e
mostra o valor retornado pela função, ou seja, o maior número.
- Obs.: não use a função nativa (pronta) da linguagem, a função max.
Teste 1: Entrada: 2 e 3         Saída: Maior valor: 3
Teste 2: Entrada: 4 e 3         Saída: Maior valor: 4
Teste 3: Entrada: 5 e 5         Saída: Maior valor: 5   """

# A função recebe dois parâmetros (dois valores) e retorna o maior
def maximo_dois(num1, num2):    # Assinatura da função
    if num1 > num2:             # Se num1 for maior que num2
        maior = num1
    else:
        maior = num2
    return maior                # Retorna o maior valor

# O if abaixo indica o início da execução do programa principal (main)
if __name__ == '__main__':      # Atalho: main + <tab>
    numero1 = int(input("Primeiro número: ")) # Lê dois números do usuário
    numero2 = int(input("Segundo número: "))
    vl_retorno = maximo_dois(numero1, numero2) # Chama a função
    # A variável vl_retorno recebe o valor retornado pela função
    print("\nMaior valor:", vl_retorno)

''' --- ALTERAÇÕES:
a. Refaça a função maximo de dois sem a variável maior.
b. Refaça a função main (principal) sem usar a variável vl_retorno. 
c. Acrescente a função mínimo de dois. Ela recebe 2 valores e retorna o menor valor
d. No main, chame a função minimo passando os dois valores

   --- DICAS:
def maximo_dois(num1, num2):                                        # a.
    if num1 > num2:             # Se num1 for maior que num2
        return num1
    else:
        return num2
    # vl_retorno = maximo_dois(numero1, numero2)                    # b.
    # A variável vl_retorno recebe o valor retornado pela função
    print("\nMaior valor:", maximo_dois(numero1, numero2))
def minimo(num1, num2):                                             # c.
    if num1 < num2:         # Se num1 for menor que num2
        menor = num1
    else:
        menor = num2
    return menor            # Retorna

'''
