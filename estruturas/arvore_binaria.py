class TreeNone:
    """Tipo que representa os nós da árvore.
    Possuem um item e ponteiros para subárvores a esquerda e direita.
    Seus ponteiros serão None por padrão.
    Retorna None caso o data serja nulo."""

    def __init__(self, data):
        if not data:
            return None
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    """Classe que representa uma árvore binária.
    Possuem nós de raíz, a esquerda e direita.
    Seus nós a esquerda serão menores que a raíz.
    Seus nós a direita serão maiores que a raíz.
    Retorna None, caso a raíz não seja inicializada."""

    def __init__(self, value=None):
        if not value:
            return None
        self.root = value
        
class Sala:
    """
    Representa uma sala na árvore do jogo, contendo um nível e ponteiros para salas à esquerda e direita.
    """
    def __init__(self, nivel):
        self.nivel = nivel
        self.left = None
        self.right = None
