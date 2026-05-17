def exibir_mensagem_e_numero(mensagem, numero):
    print(f"Mensagem: {mensagem}")
    print(f"Número: {numero}")

def main():
    msg = input("Digite uma mensagem: ")
    num = input("Digite um número: ")
    exibir_mensagem_e_numero(msg, num)

main()