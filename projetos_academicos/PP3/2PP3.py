qtd = 0
soma = 0
maior = None
menor = None
qtd_maior_50 = 0

while True:
    valor = float(input("Digite um valor (0 para sair): "))
    
    if valor == 0:
        break
    
    qtd += 1
    soma += valor
    
    if maior is None or valor > maior:
        maior = valor
    
    if menor is None or valor < menor:
        menor = valor
    
    if valor >= 50:
        qtd_maior_50 += 1

media = soma / qtd if qtd > 0 else 0

print("\nRESULTADOS:")
print("Quantidade:", qtd)
print("Soma:", soma)
print("Média:", media)
print("Maior valor:", maior)
print("Menor valor:", menor)
print("Valores >= 50:", qtd_maior_50)