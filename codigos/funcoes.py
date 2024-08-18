def create_game():
    name = input("Digite o nome do jogo: ")
    ano_jogo = float(input("Digite o ano do jogo: "))
    preco_jogo = float(input("Digite o preço do jogo: "))
    nota_jogo = float(input("Digite a nota de avaliação do jogo: "))
    
    print(f"\nNome do Game: {name} \nAno do Game: {ano_jogo} \nPreço do Game: R$ {preco_jogo:.2f} \nNota do Game: {nota_jogo} \n")
    print()


create_game()

create_game()
