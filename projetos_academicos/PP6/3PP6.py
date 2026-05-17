def calcula_desconto_steam(preco_cheio, porcentagem):
    desconto = preco_cheio * (porcentagem / 100) 
    preco_final = preco_cheio - desconto 
    return preco_final

def main_loja():
    print("\n--- DESCONTOS DA STEAM ---")
    nome_jogo = input("Qual jogo você quer comprar? ")
    preco = float(input(f"Quanto custa {nome_jogo}? R$ "))
    cupom = float(input("Qual o % de desconto da promoção? "))
    
    valor_com_desconto = calcula_desconto_steam(preco, cupom)
    
    print(f"\nBoa! O jogo {nome_jogo} vai sair por apenas R$ {valor_com_desconto:.2f}!")
main_loja()