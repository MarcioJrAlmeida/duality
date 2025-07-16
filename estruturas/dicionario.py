class Dicionario:
    """Implementação para dicionário"""

    def __init__(self, dados=None):
        self.dados = dados if dados is not None else {}

    def adicionar(self, chave, valor):
        """Adiciona um par chave-valor ao dicionário."""
        self.dados[chave] = valor

    def remover(self, chave):
        """Remove uma chave do dicionário."""
        if chave in self.dados:
            del self.dados[chave]

    def obter(self, chave):
        """Obtém o valor associado a uma chave."""
        return self.dados.get(chave, None)

    def __str__(self):
        return str(self.dados)

