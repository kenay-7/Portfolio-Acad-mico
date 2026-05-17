"""            Comentários de várias linhas - Prof. Barbosa
Atalhos: Ctrl<d>, duplica linha. Ctrl<y>, apaga linha. Ctrl</>, comenta linha.

- Problema:

- Implemente um programa com a função (def) e a função principal (main):

- A função (def) recebe dois parâmetros (dois valores) inteiros que corresponde
  ao horário no formato (hora e minuto), faz o cálculo e retorna um valor
  inteiro que corresponde ao horário convertido em minutos.

- A função principal (main) lê o horário (as horas e os minutos) digitado pelo
  usuário, chama a função converte em minutos passando os dois argumentos
  (horas e minutos) e com o valor retornado pela função, mostra uma mensagem
  apropriada, ou seja, o horário convertido em minutos.

         - Entrada:                 - Saída:
Teste 1: horas: 1, minutos: 30      Horário convertido em minutos: 90
Teste 2: horas: 2, minutos: 10      Horário convertido em minutos: 130      """

def converte_em_minuto(horas, minutos): # Assinatura da função
    vl_minutos = horas * 60 + minutos   # Converte tudo em minutos
    return vl_minutos                   # Retorna o valor calculado

# O if abaixo indica o início da execução do programa principal (main)
if __name__ == '__main__':              # Atalho: main + <tab>
    h = int(input("Horas: "))           # Lê os dados de entrada
    m = int(input("Minutos: "))
    retorno = converte_em_minuto(h, m)     # Chama a função
    print("\nHorário convertido em minutos:", retorno)  # Tela de saída

''' --- ALTERAÇÕES:
a. No final do programa principal (main), mostre também na tela de saída 
   o valor da hora e do minuto lidos.
b. No final do main, chame a função converte_em_minuto mais uma vez.

    --- DICAS: 
    print("Horas:", h)                                       # Solução 1 # a.
    print("Minutos:", m)
    print(h, "horas e", m, "minutos =", retorno, "minutos.") # Solução 2
    print(f"{h} horas e {m} minutos = {retorno} minutos.")   # Solução 3
    print("{} horas e {} minutos = {} minutos." .format(h, m, retorno)) # Solução 4
    ...                                 # No final do main               # b.
    h = int(input("Horas: "))           # Lê os dados de entrada    
    m = int(input("Minutos: "))
    retorno = converte_em_minuto(h, m)  
    print(f"{h} horas e {m} minutos = {retorno} minutos.")

'''
