class Fila:
    """Implementação de fila para o histórico de eventos."""

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
