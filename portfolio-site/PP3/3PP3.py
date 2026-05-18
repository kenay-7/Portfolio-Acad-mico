cand1 = cand2 = cand3 = 0
nulos = brancos = 0
total = 0

while True:
    voto = int(input("Digite seu voto (0 para encerrar): "))
    
    if voto == 0:
        break
    
    if voto == 1:
        cand1 += 1
    elif voto == 2:
        cand2 += 1
    elif voto == 3:
        cand3 += 1
    elif voto == 5:
        nulos += 1
    elif voto == 6:
        brancos += 1
    else:
        print("Código inválido!")
        continue
    
    total += 1

perc_nulos = (nulos / total * 100) if total > 0 else 0
perc_brancos = (brancos / total * 100) if total > 0 else 0

print("\nRESULTADOS:")
print("Candidato 1:", cand1)
print("Candidato 2:", cand2)
print("Candidato 3:", cand3)
print("Nulos:", nulos)
print("Brancos:", brancos)
print("Percentual nulos: {:.2f}%".format(perc_nulos))
print("Percentual brancos: {:.2f}%".format(perc_brancos))