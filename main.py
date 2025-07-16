from estruturas.arvore import ArvoreBinaria
from estruturas.fila import Fila

from game.batalha import Batalha
from game.persona import Heroi, Inimigo


class Duality:
    """Classe principal que gerencia o jogo."""

    def __init__(self):
        self.heroi = Heroi()
        self.historico = Fila()
        self.arvore = self._construir_arvore()
        self.posicao_atual = self.arvore  # Começa na raiz

    def _construir_arvore(self) -> ArvoreBinaria:
        """Constrói a árvore de decisões com inimigos em diferentes níveis."""
        raiz = ArvoreBinaria()  # Nó raiz vazio (início da aventura)

        # Nível 1
        raiz.inserir_esquerda(Inimigo("Goblin", 30, "Espada", "Mágico"))
        raiz.inserir_direita(Inimigo("Orc", 50, "Espada", "Distância"))

        # Nível 2 (esquerda da esquerda)
        raiz.esquerda.inserir_esquerda(Inimigo("Mago Sombrio", 40, "Mágico", "Espada"))
        raiz.esquerda.inserir_direita(None)  # Caminho sem inimigo

        # Nível 2 (direita da esquerda)
        raiz.direita.inserir_esquerda(None)  # Caminho sem inimigo
        raiz.direita.inserir_direita(Inimigo("Mago Sombrio", 40, "Mágico", "Espada"))

        # Nível 3 - Dragão em todos os caminhos finais
        # Esquerda-Esquerda-Esquerda
        raiz.esquerda.esquerda.inserir_esquerda(
            Inimigo("Dragão", 100, "Fogo", "Mágico")
        )
        raiz.esquerda.esquerda.inserir_direita(Inimigo("Dragão", 100, "Fogo", "Mágico"))

        # Esquerda-Direita-Esquerda
        raiz.esquerda.direita.inserir_esquerda(Inimigo("Dragão", 100, "Fogo", "Mágico"))
        raiz.esquerda.direita.inserir_direita(Inimigo("Dragão", 100, "Fogo", "Mágico"))

        # Direita-Esquerda-Esquerda
        raiz.direita.esquerda.inserir_esquerda(Inimigo("Dragão", 100, "Fogo", "Mágico"))
        raiz.direita.esquerda.inserir_direita(Inimigo("Dragão", 100, "Fogo", "Mágico"))

        # Direita-Direita-Esquerda
        raiz.direita.direita.inserir_esquerda(Inimigo("Dragão", 100, "Fogo", "Mágico"))
        raiz.direita.direita.inserir_direita(Inimigo("Dragão", 100, "Fogo", "Mágico"))

        return raiz

    def jogar(self):
        """Inicia o jogo."""
        print("Bem-vindo à Aventura do Herói!")
        print(
            "Você está na entrada da masmorra. Escolha seus caminhos com sabedoria..."
        )

        while True:
            # Verifica se chegou a um nó folha (final da aventura)
            if (
                self.posicao_atual.esquerda is None
                and self.posicao_atual.direita is None
            ):
                if self.posicao_atual.valor:  # Se há um inimigo
                    batalha = Batalha(self.heroi, self.historico)
                    vitoria = batalha.iniciar_combate(self.posicao_atual.valor)

                    if not vitoria:
                        print("Fim de jogo!")
                        break

                print("\nVocê chegou ao fim desta aventura!")
                print("\nHistórico de eventos:")
                print(self.historico)
                break

            # Mostra opções de caminho
            print("\nVocê está em um cruzamento. Qual caminho deseja seguir?")
            print("1- Esquerda")
            print("2- Direita")

            escolha = input("Escolha (1-2): ")

            if escolha == "1":
                self.posicao_atual = self.posicao_atual.esquerda
                self.historico.enfileirar("Você escolheu o caminho da esquerda")
            elif escolha == "2":
                self.posicao_atual = self.posicao_atual.direita
                self.historico.enfileirar("Você escolheu o caminho da direita")
            else:
                print("Opção inválida! Tente novamente.")
                continue

            # Verifica se há um inimigo neste nó
            if self.posicao_atual.valor:
                inimigo = self.posicao_atual.valor
                batalha = Batalha(self.heroi, self.historico)
                vitoria = batalha.iniciar_combate(inimigo)

                if not vitoria:
                    print("Fim de jogo!")
                    print("\nHistórico de eventos:")
                    print(self.historico)
                    break


# Inicia o jogo
if __name__ == "__main__":
    jogo = Duality()
    jogo.jogar()
