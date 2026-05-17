"""            Comentários de várias linhas - Prof. Barbosa
Atalhos: Ctrl<d>, duplica linha. Ctrl<y>, apaga linha. Ctrl</>, comenta linha.

- Problema:

- Implemente um programa com a função (def) e a função principal (main):

  A função (def) positivo_nulo_negativo que recebe um número qualquer real
(um parâmetro) e não retorna nada.
Ela mostra uma das mensagens:
“Valor positivo.”, se o número recebido for positivo;
“Valor nulo.”, se o número recebido for nulo e
“Valor negativo.”, se o número recebido for negativo.
  O programa (função main) lê o número, chama a função positivo_nulo_negativo
passando o valor lido (argumento).
- Testes:
Teste 1: Entrada  7               Saída: "Valor positivo."
Teste 2: Entrada  0               Saída: "Valor nulo."
Teste 3: Entrada -7               Saída: "Valor negativo."      """
def positivo_nulo_negativo (number): # Função testa um valor
    if number < 0:
        print("Valor negativo.")
    elif number == 0:
        print("Valor nulo.")
    else:
        print("Valor positivo.")
# Início da função main.
if __name__ == '__main__':                  # Atalho:  main + <tab>
    valor_digitado = float(input("Digite um número: "))
    positivo_nulo_negativo(valor_digitado)  # Chama a função








''' --- ALTERAÇÕES:
a. Chame a função mais uma vez, peça para o usuário digitar mais um valor
b. Refaça o exercício sem usar a variável valor_retorno, na função main.

    --- DICAS:
   valor2 = float(input("Digite outro número: "))  # No final do main   # a.
   positivo_nulo_negativo (valor2)

   positivo_nulo_negativo(float(input("Digite um número: ")))           # b.
'''
