"""            Comentários de várias linhas - Prof. Barbosa
Atalhos: Ctrl<d>, duplica linha. Ctrl<y>, apaga linha. Ctrl</>, comenta linha.

- Problema:

- Implemente um programa com as funções defs e a função principal (main):

1. A função (def) "soma" recebe dois valores inteiros, realiza a soma e retorna
   o resultado do cálculo.

2. A função (def) "subtrai" recebe dois valores inteiros, realiza a subtração e
   retorna o resultado do cálculo.

3. O programa (função main) lê dois valores inteiros digitados pelos
   usuários e o usuário escolhe apenas uma operação (somar ou subtrair).
   A opção desejada será lida no programa principal (main) que
chama uma das funções passando os dois valores lidos como argumentos.
  A função main recebe o valor retornado pela função soma ou subtrai
e gera a tela de saída com essa informação. Use variável local.

Teste 1: valor 1: 13, valor 2: 14, opção: 1		Saída: Soma = 27
Teste 2: valor 1: 13, valor 2: 14, opção: 2 	Saída: Subtração = -1 """

def soma(x, y):  # A função recebe 2 parâmetros (valores) e retorna a soma
    return x + y

def subtrai(x, y):  # Recebe 2 parâmetros (valores) e retorna a subtração
    calculo = x - y
    return calculo

# O if abaixo indica o início da execução do programa principal (main)
if __name__ == '__main__':               # Atalho: main + <tab>
    v1 = int(input("Primeiro valor: "))  # Início da função main.
    v2 = int(input("Segundo valor: "))
    opcao = int(input("\n[1] Somar\n[2] Subtrair\nOpção: "))
    if opcao == 1:              # Se digitou 1, chama a função soma,
        print('\nSoma =', soma(v1, v2))
    else:                       # senão, chama a função subtrai
        print('\nSubtração =', subtrai(v1, v2))

''' --- ALTERAÇÕES:
a. Mostre também uma mensagem de opção inválida.
   Teste 3: valores v1 = 13, v2 = 14 e opção = 3. Saída: Opção inválida
b. Refaça, use a tecla "+" e "-" no lugar de 1 e 2 na mensagem de leitura:
c. Use a função 'soma' para somar 4 valores e mostre o resultado.
   Não altere (não mexa) a função soma.   

    --- DICAS:
    . . .                                                           # a.
    if opcao == 1:            
        print('Soma =', soma(v1, v2))
    elif opcao == 2:      
        print('Subtração =', subtrai(v1, v2))
    else:
        print('Opção inválida')             

    opcao = str(input("[+] Somar\n[-] Subtrair\nOpção: "))          # b.
    if opcao == '+':   
        print('Soma= ', soma(v1, v2))
    elif opcao == '-':      
        print('Subtração= ', subtrai(v1, v2))
    else:
        print('Opção inválida')      

    . . .                           # No final do main              # c.
    v3 = int(input("Terceiro valor:")           # v3 = 3
    v4 = int(input("Quarto valor:")             # v4 = 5
    s1 = soma(v1, v2)                           # Com variáveis
    s2 = soma(v3, v4)
    total = s1 + s2           
    print("Soma 4 valores:', total) 

'''
