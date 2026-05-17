quantidade = 0
soma = 0
maiores_que_20 = 0

while True:
    valor = float(input('Digite um valor ( ou 0 para sair):'))

    if valor == 0:
        break

    quantidade +=1
    soma += valor

    if valor > 20:
        maiores_que_20 += 1 

if quantidade > 0:
    media = soma / quantidade
else:
    media = 0

print('Resultados:')
print('Quantidade de valores:', quantidade)
print('Média:', media)
print('Valores maiores que 20:', maiores_que_20)