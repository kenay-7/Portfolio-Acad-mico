"""            Comentários de várias linhas - Prof. Barbosa
Atalhos: ctrl<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Problema (não use lista):

- Desenvolva um programa que leia vários números inteiros digitados pelo
usuário e use o valor -1 como condição de saída (flag) da estrutura de
repetição. Na tela de saída, mostre a quantidade de números digitados.

- Analise o problema e verifique quais dados de entrada o usuário precisa digitar.

- Passos para resolver o problema (algoritmo):
variável ct                 # Valor inicial da variável contador
estrutura de repetição:     # início da repetição
    lê número               # Indentação obrigatória
    testa condição saída
    contador                # fim da repetição
tela de saída               # O comando volta para coluna 1

6.1- Sintaxe do while com break:
Comandos antes do while 		    # Na coluna 1, executa uma única vez
...
while True:                         # Executa várias vezes
    variavel = input(“Mensagem: ”)  # Indentação obrigatória
    if condicao:                    # Organização em colunas
        break			            # Saí da estrutura de repetição
    comandos a serem repetidos
    # Fim do while                  # Fim da indentação
Comandos depois do while 		    # Na coluna 1, executa uma única vez
...

Teste 1: Entrada: 5, 6 e -1          Saída: Quantidade de números: 2
Teste 2: Entrada: 5, 6, 7 e -1       Saída: Quantidade de números: 3
Teste 3: Entrada: 5, 6, 6, 7 e -1    Saída: Quantidade de números: 4
"""

ct = 0              # Valor inicial da variável
print('Digite [-1] para sair da repetição')
while True:         # Início da repetição
    numero = int(input("Digite um número: ")) # Indentação obrigatória
    if numero == -1:
        break       # Sai da estrutura de repetição (while)
    ct = ct + 1     # ct += 1 # Contador, incrementa o ct
    # Fim da repetição "while"
print('\nQuantidade de números digitados:', ct) # O comando volta para coluna 1

''' --- ALTERAÇÕES:
a. Na tela de saída, acrescente a soma dos valores digitados.       
   Teste 4:     Entrada: 5, 6 e -1       Saída: Quantidade de números: 2 
				    		 				    Soma: 11
   Teste 5:     Entrada: 5, 6, 7 e -1    Saída: Quantidade de números: 3 
b. Refaça o programa sem usar o break dentro do while
				    		 				    Soma: 18
    --- DICAS:
ct = 0              # Valor inicial das variáveis                       # a.
soma = 0
print('Digite [-1] para sair')
while True:  # Laço de repetição
    numero = int(input("Digite um número: "))  # Indentação 
    if numero == -1:
        break       # Sai de uma estrutura de repetição (while)
    ct = ct + 1     # ct += 1 (contador)
    soma = soma + numero  # soma += numero (somador ou acumulador)
    # Fim da estrutura de repetição "while"
print('Quantidade de números digitados:', ct) # O comando volta para coluna 1
print("Soma dos valores digitados:", soma)

ct = 0              # Valor inicial da variável                         # b
print('Digite [-1] para sair da repetição')
numero = int(input("Digite um número: "))  # Indentação obritória
while numero != -1:  # Laço de repetição, repete enquanto condição verdadeira
    ct = ct + 1     # ct += 1 (contador), incrementa o ct
    numero = int(input("Digite um número: "))  # Indentação obritória
    # Fim da estrutura de repetição "while"
print('Quantidade de números digitados:', ct)  # O comando volta para coluna 1

'''
