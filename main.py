from estruturas.arvore import ArvoreBinaria
from estruturas.fila import Fila

from game.batalha import Batalha, verificar_aparicao_inimigo
from game.persona import Heroi, Inimigo

class Duality:
    """Classe principal que gerencia o jogo."""
    def __init__(self):
        self.heroi = Heroi()
        self.historico = Fila()
        self.arvore = self._construir_arvore()
        self.posicao_atual = self.arvore  # Começa na raiz

    def _construir_arvore(self) -> ArvoreBinaria:
        """Constrói manualmente a árvore binária com inimigos por nível (1 a 4)."""
        raiz = ArvoreBinaria()  # Nó inicial (nível 0)

        # Nível 1
        raiz.inserir_esquerda(Inimigo("Goblin", 30, "Espada", "Mágico"))
        raiz.inserir_direita(Inimigo("Goblin", 30, "Espada", "Mágico"))

        # Nível 2
        raiz.esquerda.inserir_esquerda(Inimigo("Troll", 50, "Espada", "Distância"))
        raiz.esquerda.inserir_direita(Inimigo("Troll", 50, "Espada", "Distância"))
        raiz.direita.inserir_esquerda(Inimigo("Troll", 50, "Espada", "Distância"))
        raiz.direita.inserir_direita(Inimigo("Troll", 50, "Espada", "Distância"))

        # Nível 3
        raiz.esquerda.esquerda.inserir_esquerda(Inimigo("Mago Sombrio", 60, "Mágico", "Espada"))
        raiz.esquerda.esquerda.inserir_direita(Inimigo("Mago Sombrio", 60, "Mágico", "Espada"))
        raiz.esquerda.direita.inserir_esquerda(Inimigo("Mago Sombrio", 60, "Mágico", "Espada"))
        raiz.esquerda.direita.inserir_direita(Inimigo("Mago Sombrio", 60, "Mágico", "Espada"))
        raiz.direita.esquerda.inserir_esquerda(Inimigo("Mago Sombrio", 60, "Mágico", "Espada"))
        raiz.direita.esquerda.inserir_direita(Inimigo("Mago Sombrio", 60, "Mágico", "Espada"))
        raiz.direita.direita.inserir_esquerda(Inimigo("Mago Sombrio", 60, "Mágico", "Espada"))
        raiz.direita.direita.inserir_direita(Inimigo("Mago Sombrio", 60, "Mágico", "Espada"))

        # Nível 4 (Finais com o Dragão)
        def inserir_dragoes(no: ArvoreBinaria):
            no.inserir_esquerda(Inimigo("Dragão", 100, "Fogo", "Mágico"))
            no.inserir_direita(Inimigo("Dragão", 100, "Fogo", "Mágico"))

        folhas_nivel_3 = [
            raiz.esquerda.esquerda.esquerda,
            raiz.esquerda.esquerda.direita,
            raiz.esquerda.direita.esquerda,
            raiz.esquerda.direita.direita,
            raiz.direita.esquerda.esquerda,
            raiz.direita.esquerda.direita,
            raiz.direita.direita.esquerda,
            raiz.direita.direita.direita
        ]

        for folha in folhas_nivel_3:
            inserir_dragoes(folha)

        return raiz

    def jogar(self):
        """Inicia o jogo, gerenciando o loop de exploração e combate."""
        # Introdução narrativa do jogo
        print("Bem-vindo ao Duality ⚔️  - RPG de Batalha!")
        print("---" * 50)
        print("Em um reino outrora pacífico, criaturas sombrias emergiram das profundezas...")
        print("Apenas um herói se levantou para retomar a paz: VOCÊ.")
        print("---" * 50)

        # Loop principal de exploração
        while True:
            # 1. Verifica se estamos em um nó folha (último nível da aventura)
            if self.posicao_atual.esquerda is None and self.posicao_atual.direita is None:
                # Chegou ao fim do caminho - combate final contra o chefe, se existir
                if self.posicao_atual.valor:
                    inimigo = self.posicao_atual.valor  # Deve ser o Dragão no nível 4
                    batalha = Batalha(self.heroi, self.historico)
                    print("⚔️ Um Dragão colossal bloqueia o caminho... não há como escapar!")
                    vitoria = batalha.iniciar_combate(inimigo)  # Combate contra o chefe final
                    if vitoria:
                        # Herói venceu o Dragão - vitória do jogo
                        print("🌟 PARABÉNS! Você derrotou o Dragão e salvou o reino! 🌟")
                        self.historico.enfileirar("Vitória: o herói derrotou o Dragão.")
                    else:
                        # Herói foi derrotado pelo Dragão - fim de jogo
                        print("💀 O MAL PREVALECEU 💀")
                        print("O herói caiu em batalha. O reino permanece em trevas...")
                        self.historico.enfileirar("Derrota: o herói foi derrotado pelo Dragão.")
                # Exibe todo o histórico de eventos e encerra o jogo
                print("\n===== HISTÓRICO DO HERÓI =====")
                print(self.historico)
                break  # sai do loop principal

            # 2. Apresenta as opções de caminho nesta sala
            print("\nVocê está em um cruzamento. Qual caminho deseja seguir?")
            print("1- Esquerda")
            print("2- Direita")
            escolha = input("Escolha (1-2): ")
            if escolha == "1":
                # Vai para a sala à esquerda
                self.posicao_atual = self.posicao_atual.esquerda
                self.historico.enfileirar("Você escolheu o caminho da esquerda")
            elif escolha == "2":
                # Vai para a sala à direita
                self.posicao_atual = self.posicao_atual.direita
                self.historico.enfileirar("Você escolheu o caminho da direita")
            else:
                print("Opção inválida! Tente novamente.")
                continue  # retorna ao início do loop sem avançar de sala

            # 3. Ao entrar na nova sala, verifica se um inimigo aparece
            inimigo = self.posicao_atual.valor
            if inimigo:
                apareceu = verificar_aparicao_inimigo(inimigo)
                if apareceu:
                    batalha = Batalha(self.heroi, self.historico)
                    if inimigo.nome != "Dragão":
                        acao = input("Deseja combater (C) ou fugir (F)? ").upper()
                        if acao == "F":
                            resultado = batalha.tentar_fuga(inimigo)
                        else:
                            resultado = batalha.iniciar_combate(inimigo)
                    else:
                        print("Não é possível fugir do chefe final. Prepare-se para a batalha!")
                        resultado = batalha.iniciar_combate(inimigo)
                    if not resultado:
                        # Herói morreu seja fugindo ou lutando - fim do jogo
                        print("\n===== HISTÓRICO DO HERÓI =====")
                        print(self.historico)
                        break  # encerra o loop principal em caso de derrota do herói
                    # Se resultado é True, o herói venceu o inimigo ou fugiu com sucesso.
                    # Neste caso, o jogo continua no loop (herói permanece vivo na sala atual).
            else:
                # Sala explicitamente vazia (nenhum inimigo neste nó)
                print("Nada aqui. A sala está vazia.")
                self.historico.enfileirar("Sala vazia")
            # Loop continua para próxima escolha de caminho ou verificação de fim


# Inicia o jogo
if __name__ == "__main__":
    jogo = Duality()
    jogo.jogar()
