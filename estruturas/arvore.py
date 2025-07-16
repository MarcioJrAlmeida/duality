"""
módulo arvore.py

Este módulo contém funções relacionadas a criação e implementação da Árvore Binária.
"""
class ArvoreBinaria:
    """
    Classe que representa uma árvore binária onde cada nó pode conter um inimigo.

    Attributes:
        inimigo (Inimigo): Inimigo presente na sala.
        esquerda (ArvoreBinaria): Caminho à esquerda.
        direita (ArvoreBinaria): Caminho à direita.
    """

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
