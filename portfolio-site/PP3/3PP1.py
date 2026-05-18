soma_pares = 0
qtd_pares = 0

soma_impares = 0
qtd_impares = 0

soma_total = 0
qtd_total = 0

while True:
    num = int(input("Digite um número (0 para sair): "))
    
    if num == 0:
        break
    
    soma_total += num
    qtd_total += 1
    
    if num % 2 == 0:
        soma_pares += num
        qtd_pares += 1
    else:
        soma_impares += num
        qtd_impares += 1

# Cálculo das médias
media_pares = soma_pares / qtd_pares if qtd_pares > 0 else 0
media_impares = soma_impares / qtd_impares if qtd_impares > 0 else 0

print("\nRESULTADOS:")
print("Quantidade total:", qtd_total)
print("Soma total:", soma_total)
print("Média dos pares:", media_pares)
print("Média dos ímpares:", media_impares)