"""
Módulo que define as classes de personagens do jogo: Herói e Inimigo.
"""

from estruturas.dicionario import Dicionario


class Persona:
    """
    Classe base para personagens.

    Attributes:
        nome (str): Nome do personagem.
        hp (int): Pontos de vida.
        ataque (dict): Tipos de ataque e seus valores.
        defesa (dict): Tipos de defesa e seus valores.

    Methods:
        receber_dano(dano): Aplica dano e retorna se ainda está vivo.
    """

    def __init__(self, nome: str, hp: int, ataque: dict, defesa: dict):
        self.nome = nome
        self.hp = hp
        self.ataque = Dicionario(ataque)
        self.defesa = Dicionario(defesa)

    def receber_dano(self, dano: int) -> bool:
        """Aplica dano e retorna True se ainda estiver vivo."""
        self.hp -= dano
        return self.hp > 0

    def __str__(self) -> str:
        return f"{self.nome} (HP: {self.hp})"


class Heroi(Persona):
    """
    Classe que representa o herói jogável.

    Methods:
        restaurar_vida(): Restaura HP total do herói.
    """

    def __init__(self):
        super().__init__(
            nome="Herói",
            hp=100,
            ataque={"Espada": 10, "Mágico": 8, "Distância": 7},
            defesa={"Espada": 5, "Mágico": 6, "Distância": 4},
        )

    def restaurar_vida(self) -> None:
        """Restaura toda a vida do herói."""
        self.hp = 100
        print("[HP RESTAURADO] +100 pontos de vida 🧥")


class Inimigo(Persona):
    """
    Classe para representar inimigos do jogo.

    Attributes:
        tipo_atk (str): Tipo de ataque principal do inimigo.
        fraqueza (str): Tipo de ataque ao qual é vulnerável.
    """

    def __init__(self, nome: str, hp: int, tipo_atk: str, fraqueza: str):
        super().__init__(
            nome=nome,
            hp=hp,
            # Cada inimigo tem um tipo de ataque principal
            ataque={tipo_atk: 10},
            defesa={},  # Inimigos não têm defesa especial
        )
        self.tipo_atk = tipo_atk
        self.fraqueza = fraqueza
