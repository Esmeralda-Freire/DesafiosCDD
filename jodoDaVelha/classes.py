class JogoDaVelha:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.jogadaPlayer1 = True
        self.posicao = [str(i + 1) for i in range(9)]

    def jogo(self):
        print(f" {self.posicao[0]} | {self.posicao[1]} | {self.posicao[2]} ")
        print("-----------")
        print(f" {self.posicao[3]} | {self.posicao[4]} | {self.posicao[5]} ")
        print("-----------")
        print(f" {self.posicao[6]} | {self.posicao[7]} | {self.posicao[8]} ")

    def resultado(self, jogador):
        vitoria = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for condicao in vitoria:
            if all(self.posicao[i] == jogador for i in condicao):
                return True
        return False

    def verificarEmpate(self):
        return all(pos in ['X', 'O'] for pos in self.posicao)

    def jogadas(self, jogada):
        if jogada in range(9) and self.posicao[jogada] not in ['X', 'O']:
            return True
        else:
            print("Posição inválida.")
            return False

    def comecarJogo(self):
        while True:
            self.jogo()
            jogador_atual = self.player1 if self.jogadaPlayer1 else self.player2
            simbolo_atual = 'X' if self.jogadaPlayer1 else 'O'
            print(f"{jogador_atual}, é a sua vez.")
            jogada = int(input("Escolha uma posição de 1 a 9: ")) - 1

            if self.jogadas(jogada):
                self.posicao[jogada] = simbolo_atual
                if self.resultado(simbolo_atual):
                    self.jogo()
                    print(f"Parabéns {jogador_atual}, você venceu!")
                    break

                if self.verificarEmpate():
                    self.jogo()
                    print("O jogo terminou em empate!")
                    break

                self.jogadaPlayer1 = not self.jogadaPlayer1




