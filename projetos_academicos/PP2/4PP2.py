quantidade = 0
soma_total = 0

soma_pares = 0 
qtd_pares = 0

soma_impares = 0
qtd_impares = 0

while True:
    num = int(input('Digite um número (0 para sair):'))

    if num == 0:
        break
    quantidade += 1 
    soma_total += num

    if num %2 == 0:
        soma_pares += num
        qtd_pares += 1
    else:
        soma_impares += num
        qtd_impares += 1

media_pares = soma_pares / qtd_pares if qtd_pares > 0 else 0
media_impares = soma_impares / qtd_impares if qtd_impares > 0 else 0

print('Resultados:')
print('Quantidade total:', quantidade)
print('Soma total:', soma_total)
print('Média dos pares:', media_pares)
print('Média dos impares:', media_impares)