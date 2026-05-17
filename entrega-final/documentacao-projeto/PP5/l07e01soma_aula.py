"""            Comentários de várias linhas - Prof. Barbosa
Atalhos: Ctrl<d>, duplica linha. Ctrl<y>, apaga linha. Ctrl</>, comenta linha.

- Problema:

- Implemente um programa com a função def e a função principal (main):

1. A função (def) recebe os dois parâmetros (dois valores), calcula a soma
dos dois valores e retorna o resultado do cálculo para o main.

2. A função principal (main) lê os dois valores inteiros digitados pelo usuário,
chama a função passando os dois argumentos (dois valores lidos) e depois mostra
o valor retornado pela função, ou seja, o resultado obtido.

Teste: Entrada: 2 e 3                   Saída: Soma = 5         """

# O def define a função que recebe os dois parâmetros (dois valores) v1 e v2.
def soma(v1, v2):       # Assinatura da função
    v_soma = v1 + v2    # A variável v_soma recebe o resultado do cálculo
    return v_soma       # Retorna o valor calculado
    # Fim da funçao

# A função (def) só será executada quando for chamada na função main.
# O if abaixo indica o início da execução do programa principal (main)
if __name__ == '__main__':                  # main + <tab> (atalho)
    valor1 = int(input('Primeiro valor: ')) # Indentação obrigatória.
    valor2 = int(input('Segundo valor: '))
    v_retorno = soma(valor1, valor2) # Chama a função
    # A variável v_retorno recebe o valor retornado pela função (def)
    print("\nSoma = ", v_retorno)           # Tela de saída

''' --- ALTERAÇÕES:
a. Altere a função principal (main), refaça sem usar a variável v_retorno
   Dica: a chamada da função pode ser colocado dentro do print
b. Altere a função (def), refaça a função sem usar a variável v_soma.
   Dica: na função, o cálculo pode ser feito dentro do return
c. No final do main, chame a função (def) mais uma vez, 
   passe os valores reais (2.1, 3.5). 

    --- DICAS:
    print("\nSoma = ", soma(valor1, valor2))  # Tela de saída       # a.
def soma(v1, v2):                                                   # b.
    # v_soma = v1 + v2
    # return v_soma
    return v1 + v2
    v_retorno = soma(2.1, 3.3)  # No final do main                  # c.
    print ("Soma = ", v_retorno)

'''
