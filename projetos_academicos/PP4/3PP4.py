impar = 0
M3 = 0
for i in range (0,501):
    if i % 2 == 1:
        impar = impar + i
    if i % 3 == 0:
        M3 = M3 + i
print(f"a soma dos numeros impares e multiplos de 3 = {impar + M3}")
