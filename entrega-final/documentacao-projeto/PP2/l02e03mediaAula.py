"""            Comentários de várias linhas - Prof. Barbosa
Atalhos: ctrl<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Problema:
- Implemente o programa que calcule a média aritmética de duas notas
bimestrais fornecidas (digitadas) pelo usuário.

- Analise o problema e verifique quais dados de entrada o usuário precisa digitar.

- Fórmula de média aritmética: media = ____soma____            (numerador)
				                        quantidade             (denominador)

- Fórmula de média aritmética: media = ___nota1___+___nota2___ (numerador)
                                                  2            (denominador)

- Passos para resolver o problema (algoritmo):
Entrada de dados (leia)
Processamento (calcule)
Saída de dados (escreva)

Teste 1: Entrada: nota1: 4.5 e nota2: 6.1       Saída: Média = 5.3
Teste 2: Entrada: nota1: 7.5 e nota2: 5.1       Saída: Média = 6.3
Obs.: digite o valor da nota com ponto no lugar da vírgula (notação americana)

Fim do Comentário de várias linhas.             """
nota1 = float(input("Primeira nota: ")) # Converte os valores para float
nota2 = float(input("Segunda nota: "))
# Processamento, atribui o cálculo à variável media
media = (nota1 + nota2) / 2             # Parênteses obrigatórios.
print("Média =", media)                  # Mostra o resultado
''' --- ALTERAÇÕES:
a. Mostre a média com duas casas decimais
b. Acrescente, considere que o aluno realizou três avaliações. 
   Teste 3: Entrada: nota1: 2, nota2: 3 e nota3: 4       Saída: 3
c. Na execução, pule três linhas antes de mostrar o valor da média.
d. Depois da média, mostre também o valor das três notas.
    --- DICAS:
print(f'Média: {media:.2f}')  # Mostra com 2 casas decimais.    # a.
print('Média: {:.2f}' .format(media))  # Mostra com 2 casas decimais.
nota3 = float(input("Terceira nota: "))                         # b.
#   . . . 
media = (nota1 + nota2 + nota3) / 3
print ()                         # Solução 1                    # c.
print ()
print ()
print ('\n\n\n')                 # Solução 2                            
print("\n\n\nA média é", media)  # Solução 3                  
    --- DICAS:
print ("Nota 1 =", nota1)                                       # d.
print ("Nota 2 =", nota2)                                      
print ("Nota 3 =", nota3)                                      
    . . .

'''
