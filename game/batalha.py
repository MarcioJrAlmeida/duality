from estruturas.fila import Fila
from game.persona import Heroi, Inimigo
from utils.dados import rolar_dado


class Batalha:
    """Gerencia o sistema de combate do jogo."""

    def __init__(self, heroi: Heroi, historico: Fila):
        self.heroi = heroi
        self.historico = historico

    def iniciar_combate(self, inimigo: Inimigo) -> bool:
        """Inicia e gerencia um combate completo."""
        self.historico.enfileirar(f"Combate contra {inimigo.nome} iniciado!")

        # Determina quem começa
        turno = self._determinar_iniciativa(inimigo)
        print(f"{inimigo.nome} aparece! Prepare-se para lutar!")

        while self.heroi.hp > 0 and inimigo.hp > 0:
            if turno == "heroi":
                self._turno_heroi(inimigo)
            else:
                self._turno_inimigo(inimigo)

            # Alterna turnos
            turno = "inimigo" if turno == "heroi" else "heroi"

        return self._verificar_resultado(inimigo)

    def _turno_heroi(self, inimigo: Inimigo) -> None:
        """Executa as ações do turno do herói."""
        print("\nSeu turno:")
        print(f"Seu HP: {self.heroi.hp} | HP do {inimigo.nome}: {inimigo.hp}")

        while True:
            acao = input("Escolha:\n1- Atacar\n2- Defender\n> ")

            if acao == "1":  # Ataque
                print("Tipos de ataque disponíveis:")
                print("1- Espada (10 base)")
                print("2- Mágico (8 base)")
                print("3- Distância (7 base)")

                tipo = input("Escolha o tipo de ataque (1-3): ")
                if tipo == "1":
                    dano = self.heroi.ataque.obter("Espada") + rolar_dado()
                    tipo_atk = "Espada"
                elif tipo == "2":
                    dano = self.heroi.ataque.obter("Mágico") + rolar_dado()
                    tipo_atk = "Mágico"
                elif tipo == "3":
                    dano = self.heroi.ataque.obter("Distância") + rolar_dado()
                    tipo_atk = "Distância"
                else:
                    print("Opção inválida! Tente novamente.")
                    continue

                # Verifica se é um ataque eficaz
                if tipo_atk == inimigo.fraqueza:
                    dano *= 2
                    print("Ataque super efetivo! Dano dobrado!")

                inimigo.receber_dano(dano)
                self.historico.enfileirar(
                    f"Você atacou com {tipo_atk} causando {dano} de dano"
                )
                print(f"Você causou {dano} de dano ao {inimigo.nome}!")
                break

            elif acao == "2":  # Defesa
                print("Tipos de defesa disponíveis:")
                print("1- Escudo (contra Espada)")
                print("2- Escudo Mágico (contra Mágico)")
                print("3- Escudo à Distância (contra Distância/Fogo)")

                tipo_def = input("Escolha o tipo de defesa (1-3): ")
                if tipo_def == "1":
                    defesa = "Escudo"
                elif tipo_def == "2":
                    defesa = "Escudo Mágico"
                elif tipo_def == "3":
                    defesa = "Escudo à Distância"
                else:
                    print("Opção inválida! Tente novamente.")
                    continue

                self.historico.enfileirar(
                    f"Você se preparou para defender com {defesa}"
                )
                print(f"Você se preparou para defender com {defesa} no próximo turno!")
                break

            else:
                print("Opção inválida! Tente novamente.")

    def _turno_inimigo(self, inimigo: Inimigo) -> None:
        """Executa as ações do turno do inimigo."""
        print(f"\nTurno do {inimigo.nome}:")
        dano = rolar_dado()  # Dano base do inimigo

        # Aplica o tipo de ataque do inimigo
        if inimigo.tipo_atk == "Espada":
            dano += 10
        elif inimigo.tipo_atk == "Mágico":
            dano += 8
        elif inimigo.tipo_atk == "Fogo":
            dano += 12  # Dragão é mais forte

        self.heroi.receber_dano(dano)
        self.historico.enfileirar(
            f"{inimigo.nome} atacou com {inimigo.tipo_atk} causando {dano} de dano"
        )
        print(f"{inimigo.nome} te atacou causando {dano} de dano!")

    def _determinar_iniciativa(self, inimigo: Inimigo) -> str:
        """Determina quem começa o combate."""
        ini_heroi = rolar_dado() + 5  # Herói tem pequena vantagem
        ini_inimigo = rolar_dado()

        print(f"Iniciativa: Herói {ini_heroi} vs {inimigo.nome} {ini_inimigo}")
        return "heroi" if ini_heroi >= ini_inimigo else "inimigo"

    def _verificar_resultado(self, inimigo: Inimigo) -> bool:
        """Verifica o resultado do combate."""
        if self.heroi.hp <= 0:
            self.historico.enfileirar("Você foi derrotado!")
            print("Você foi derrotado!")
            return False

        self.historico.enfileirar(f"{inimigo.nome} foi derrotado!")
        print(f"Você derrotou {inimigo.nome}!")
        self.heroi.restaurar_vida()
        return True
