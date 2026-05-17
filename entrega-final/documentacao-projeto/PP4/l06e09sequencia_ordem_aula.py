"""            Comentários de várias linhas - Prof. Barbosa
Atalhos: ctrl<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Problema anterior:
- Elabore o programa que gere e mostre a sequência dos números inteiros na
ordem crescente de um em um, onde o usuário fornece (digita) o valor inicial
e o valor final da sequência.

- Problema atual:
- Melhore o programa anterior, se o usuário fornecer (digitar) o valor inicial
menor que o valor final, gere e mostre a sequência na ordem crescente.
  E se o usuário digitar o valor inicial maior que o valor final, gere e mostre
a sequência na ordem decrescente.

- Passos para resolver o problema (algoritmo):

lê primeiro
lê ultimo
escreva cabeçalho
se primeiro <= ultimo:
    for variavel_for in range (v_inicial, v_final, v_passo):
        escreva variável_for    # Variável do for
senão:
    for variável_for in range (v_inicial, v_final, v_passo):
        escreva variável_for    # Variável do for

Teste 1:    Entrada: 1, 5         Saída: 1 2 3 4 5
Teste 2:    Entrada: 5, 1         Saída: 5 4 3 2 1
Teste 3:    Entrada: 5, 5         Saída: 5
"""

primeiro = int(input("Primeiro valor: "))   # Entrada de dados
ultimo = int(input("Último valor: "))
print("- Sequência de números inteiros:")   # Cabeçalho.
if primeiro <= ultimo:          # ordem crescente
    for numero in range(primeiro, ultimo + 1, 1):
        print(numero)
else:                           # Ordem decrescente (primeiro > ultimo)
    for numero in range(primeiro, ultimo - 1, -1):
        print(numero)

''' --- ALTERAÇÕES:
a. Mostre um destes título (cabeçalho): "Valores na ordem crescente:" ou 
   "Valores na ordem decrescente:", na tela de saída.
b. Se os valores forem iguais, mostre a  mensagem: "Os valores são iguais."
c. Mostre também a quantidade de números gerados na sequência. Use contador
   Teste 1: Entrada: primeiro: 1, último: 5              Saída: Quantidade: 5
   Teste 2: Entrada: primeiro: 5, último: 1              Saída: Quantidade: 5
d. No final, mostre a média dos números gerados na sequência.
   Teste: Entrada: Inicial: 1, final: 5              Saída: Média: 3
- Fórmula de média aritmética:      media = ____soma____           (numerador)
				                             quantidade            (denominador)

    --- DICAS:
if primeiro <= ultimo:                                          # a.
    print("Valores na ordem crescente:")
    for numero in range(primeiro, ultimo + 1, 1):
        print(numero)                                
else:
    print("Valores na ordem decrescente:")
    for numero in range(primeiro, ultimo - 1, -1):
        print(numero)
if primeiro < ultimo:                                           # b.
    print("Valores na ordem crescente.")
    for numero in range(primeiro, ultimo + 1, 1):
        print(numero)
elif primeiro > ultimo:                          
    print("Valores na ordem decrescente.")
    for numero in range(primeiro, ultimo - 1, -1):
        print(numero)
else:                           # primeiro = ultimo
    print("Os valores são iguais, ", primeiro)  

ct = 0                          # Antes do for                  # c.
    ct = ct + 1                 # Dentro dos dois for, indentado       
print ("Quantidade: ", ct)      # Depois do for
soma = 0                         # Antes do for                 # d.
...
if primeiro < ultimo:                                                          
    for numero in range(primeiro, ultimo + 1, 1):
        print(numero)
        ct += 1
        soma = soma + numero
    media = soma / ct            # Depois do for
    print ('Média: ', media)            

---
e. Deixe o programa mais flexível, permita que o usuário forneça o valor 
   do passo (incremento), ou seja, o intervalo entre os números gerados.
f. Resolva o problema usando apenas um for  
    --- DICAS:

. . .                                                           # e.
passo = int(input('Valor do passo: '))     
if primeiro < ultimo:                              
    for numero in range(primeiro, ultimo + 1, passo):
elif primeiro > ultimo:                            
    for numero in range(primeiro, ultimo - 1, -passo):     
else:                                         
    print("Os valores são iguais, ", primeiro) 
primeiro = int(input("Digite o número inicial: "))              # f.
ultimo = int(input("Digite o número final: "))
print("- Sequência de números inteiros:")  # Cabeçalho.
if primeiro < ultimo:                 # inicial < final, indica ordem crescente
    passo = +1
    ultimo = ultimo  + 1
elif primeiro > ultimo:               # inicial > final, indica ordem decrescente
    passo = -1
    ultimo = ultimo - 1
else:                               # inicial = final
    print("Os valores são iguais!")
    passo = +1
    ultimo = ultimo + 1
# Executa o for dentro dos limites recebidos, de forma crescente ou decrescente
for numero in range(primeiro, ultimo, passo):
    print(numero)
---

- Outra solução:
# Recebe os números inicial e final
inicial = int(input("Digite o número inicial: "))
final = int(input("Digite o número final: "))
print("Fahrenheit | Celsius")       # Mostra o cabeçalho da tabela
if inicial < final:                 # inicial < final, indica ordem crescente
    passo = +1
    final = final  + 1
elif inicial > final:               # inicial > final, indica ordem decrescente
    passo = -1
    final = final - 1
else:                               # inicial = final
    print("Os valores são iguais!")
    passo = +1
    final = final  + 1
# executa o for dentro dos limites recebidos, de forma crescente ou decrescente
for fahrenheit in range(inicial, final, passo):
    celsius = 5 / 9 * (fahrenheit - 32)      # celsius = 5 * (fahrenheit - 32) / 9
    print ("{:2.1f}{:10s}| {:2.3f}{:3s}".format(fahrenheit, " ºF", celsius, " ºC"))
---
- Obs.: pode fazer sem o if ... else

'''
