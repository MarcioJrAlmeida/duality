class ArvoreBinaria:
    """Implementação de árvore binária para representar os caminhos da aventura."""

    def __init__(self, valor=None):
        self.valor = valor  # Nó atual pode conter um inimigo ou ser None
        self.esquerda = None  # Caminho esquerdo (False)
        self.direita = None  # Caminho direito (True)
        self.pai = None  # Referência ao nó pai

    def inserir_esquerda(self, valor):
        """Insere um nó à esquerda."""
        if self.esquerda is None:
            self.esquerda = ArvoreBinaria(valor)
            self.esquerda.pai = self
        else:
            novo_no = ArvoreBinaria(valor)
            novo_no.esquerda = self.esquerda
            self.esquerda.pai = novo_no
            novo_no.pai = self
            self.esquerda = novo_no

    def inserir_direita(self, valor):
        """Insere um nó à direita."""
        if self.direita is None:
            self.direita = ArvoreBinaria(valor)
            self.direita.pai = self
        else:
            novo_no = ArvoreBinaria(valor)
            novo_no.direita = self.direita
            self.direita.pai = novo_no
            novo_no.pai = self
            self.direita = novo_no

    def __str__(self):
        return str(self.valor) if self.valor else "Nó vazio"
