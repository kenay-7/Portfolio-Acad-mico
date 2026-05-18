"""            Comentários de várias linhas - Prof. Barbosa
Atalhos: ctrl<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Problema:

- Elabore o programa que gere e mostre a sequência dos números inteiros na
ordem crescente de um em um, onde o usuário fornece (digita) o valor inicial
e o valor final da sequência.

- Passos para resolver o problema (algoritmo):

lê v_inicial
lê v_final
escreva cabeçalho
for variável do for in range(v_inicial, v_final, v_passo):
    escreva variável do for
escreva mensagem

- Teste 1:
- Entrada: Primeiro: n
           Ultimo: m
- Saída:
Sequência de números inteiros:
n
n+1
n+2
n+3
n+4
...
m
Encerrou a repetição.
"""

primeiro = int(input("Primeiro valor: "))
ultimo = int(input("Último valor: "))
print("- Sequência de números inteiros:")   # Cabeçalho.
for numero in range(primeiro, ultimo+1, 1):
    print(numero)
print('\nEncerrou a repetição.')

''' --- ALTERAÇÕES:
a. No final, mostre a quantidade de números gerados na sequência. Use contador.
   Teste 2:   Entrada:  Primeiro: 2, ultimo: 6      Saída: Quantidade: 5
b. No final, mostre também a soma de números gerados na sequência. Use somador.
   Teste 3:   Entrada:  Primeiro: 2, ultimo: 6      Saída: Soma: 20
c. Calcule e mostre a média aritmética dos números da sequência.
   Teste 4:   Entrada:  Primeiro: 2, ultimo: 6      Saída: Média: 4.0
- Fórmula de média aritmética:      media = ____soma____           (numerador)
				                             quantidade            (denominador)
    --- DICAS:
ct = 0                                      # Antes do for              # a.
    ct = ct + 1           # ct += 1         # Dentro do for, indentado
print ("Quantidade: ", ct)                  # Depois do for

soma = 0                                    # Antes do for              # b.
    soma = soma + numero  # soma += numero  # Dentro do for, indentado
print ('Soma: ', soma)                      # Depois do for

media = soma / ct                           # Depois do for             # c.
print("Média:", media)

'''
