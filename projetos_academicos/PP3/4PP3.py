salario_minimo = float(input("Digite o valor do salário mínimo: "))

menos_5 = 0
entre_5_10 = 0
mais_10 = 0
folha_total = 0

while True:
    salario = float(input("Digite o salário (0 para encerrar): "))
    
    if salario == 0:
        break
    
    folha_total += salario
    
    if salario < 5 * salario_minimo:
        menos_5 += 1
    elif salario < 10 * salario_minimo:
        entre_5_10 += 1
    else:
        mais_10 += 1

print("\nRESULTADOS:")
print("Menos de 5 salários mínimos:", menos_5)
print("Entre 5 e 10 salários mínimos:", entre_5_10)
print("10 ou mais salários mínimos:", mais_10)
print("Folha total da empresa:", folha_total)