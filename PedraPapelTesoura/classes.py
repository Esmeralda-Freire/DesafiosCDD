class PedraPapelTesoura():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.jogada1 = 0
        self.jogada2 = 0

    def jogada(self):
        self.jogada1 = int(input(f"{self.player1}, qual sua escolha?\n1-Pedra\n2-Papel\n3-Tesoura\n"))
        while self.jogada1 != 1 and self.jogada1 != 2 and self.jogada1 != 3:
            self.jogada1 = int(input("Digite uma opção válida!\n1-Pedra\n2-Papel\n3-Tesoura\n"))

        self.jogada2 = int(input(f"{self.player2}, qual sua escolha?\n1-Pedra\n2-Papel\n3-Tesoura\n"))
        while self.jogada2 != 1 and self.jogada2 != 2 and self.jogada2 != 3:
            self.jogada2 = int(input("Digite uma opção válida!\n1-Pedra\n2-Papel\n3-Tesoura\n"))

    def resultado(self):
        if self.jogada1 == self.jogada2:
            print("EMPATE!!")
        elif self.jogada1 == 1 and self.jogada2 == 2:
            print(f"{self.player2} ganhou!!")
        elif self.jogada1 == 2 and self.jogada2 == 3:
            print(f"{self.player2} ganhou!!")
        elif self.jogada1 == 3 and self.jogada2 == 1:
            print(f"{self.player2} ganhou!!")
        else:
            print(f"{self.player1} ganhou!!")
