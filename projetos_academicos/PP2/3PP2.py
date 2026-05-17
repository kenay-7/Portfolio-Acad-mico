total_alunos = 0 
aprovados = 0
reprovados = 0 
soma_nota = 0

while True:
    nota = float(input('Digite a nota do aluno:'))

    if nota == -1:
        break

    total_alunos += 1 
    soma_nota += nota

    if nota >= 5:
        aprovados += 1 
    else:
        reprovados += 1

if total_alunos > 0:
    media = soma_nota / total_alunos
else:
    media = 0

print('Resultados:')
print('Total de alunos:', total_alunos)
print('Aprovados:', aprovados)
print('Reprovados:', reprovados)
print('Média da turma:', media)