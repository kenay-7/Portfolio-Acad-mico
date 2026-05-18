"""            Comentários de várias linhas - Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Problema (não use lista):
- Desenvolva o programa que calcule a média aritmética de uma turma,
onde cada aluno realizou uma avaliação. Não sabemos a quantidade de
alunos, por isso usaremos o valor “-1” como condição (flag) de saída.
  Na tela de saída, mostre a média aritmética da turma e a quantidade
de alunos da turma.
- Analise o problema e verifique quais dados de entrada o usuário precisa digitar.

- Passos para resolver o problema (algoritmo):
variável ct                 # Valor inicial das variáveis
variável soma
estrutura de repetição:     # Início da repetição
    lê nota
    testa condição saída
    contador
    somador
    # Fim da repetição
calcula média               # Os comandos voltam para coluna 1
tela de saída

- Fórmula de média aritmética: media = ____soma____
				                        quantidade
         - Entrada:             - Saída:
Teste 1: Nota: 5, 6 e -1        Média: 5.5                  Quantidade: 2
Teste 2: Nota: 5, 6, 7 e -1     Média: 6                    Quantidade: 3
Teste 3: Nota: 5, 6, 6 e -1     Média: 5.666666666666667    Quantidade: 3
"""
ct = 0                  # Valor inicial das variáveis
soma = 0
# ct = soma = 0         # Inicializa todas as variáveis numa linha
print('Digite [-1] para sair')
while True:  # Laço de repetição while, repete enquanto condição verdadeira
    nota = float(input("Nota do aluno: "))  # Indentação é obritória
    if nota == -1:
        break           # Sai de uma estrutura de repetição (while)
    ct = ct + 1         # ct += 1 (contador), incrementa o ct
    soma = soma + nota  # soma += nota (somador ou acumulador)
    # Fim da estrutura de repetição "while"
media = soma / ct       # Os comandos voltam para coluna 1
print("\nMédia da turma:", media)
print('Quantidade de alunos:', ct)
""" --- ALTERAÇÕES:
a. No final, mostre também a soma das notas dos alunos da turma.
b. Mostre a média da turma com duas casas decimais.
c. No início do programa, leia também  o nome da disciplina. 
d. No final, na tela de saida, mostre também o nome da disciplina.
e. Mostre a média e a quantidade de alunos na mesma linha, nesta frase:
   A turma de X alunos teve a média aritmética = X.XX
    --- DICAS:
print("Soma das notas: ", soma)                                 # a.
print(f"Média da turma: {media:.2f}")           # f-string      # b.
print("Média da turma: {:.2f}" .format(media))
disciplina = str(input("Nome da disciplina: "))                 # c.
# disciplina = input("Nome da disciplina: ")
print("Disciplina: ", disciplina)                               # d.
# print("Média da turma: ", media)                              # e.
# print('Quantidade de alunos: ', ct)
print("A turma de", ct, "alunos teve a média aritmética =", media) # Solução 1
print(f"Turma de {ct} alunos teve a média aritmética = {media:.2f}") # Solução 2
print("A turma de {} alunos teve a média aritmética = {:.2f}" 
        .format(ct, media)) # Solução 3

"""
