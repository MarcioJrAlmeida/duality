"""
módulo fila.py

Este módulo contém funções relacionadas a criação e implementação da Fila, no qual vamos guardar todos os históricos de movimentação.
"""

class Fila:
    """
    Fila básica para armazenar eventos do jogo.

    Attributes:
        data (list): Lista de elementos na fila.
    
    Methods:
        enqueue(item): Adiciona item à fila.
        dequeue(): Remove e retorna o primeiro item da fila.
        is_empty(): Verifica se a fila está vazia.
    """

    def __init__(self):
        self.itens = []

    def enfileirar(self, item):
        """Adiciona um item ao final da fila."""
        self.itens.append(item)

    def desenfileirar(self):
        """Remove e retorna o item do início da fila."""
        if not self.vazia():
            return self.itens.pop(0)
        return None

    def vazia(self):
        """Verifica se a fila está vazia."""
        return len(self.itens) == 0

    def __str__(self):
        return "\n".join(self.itens)
