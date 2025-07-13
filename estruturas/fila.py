class Queue:
    """Implementação de uma fila com seus comportamentos.
    Ideal para ser herdada por tipos que queiram ser comportar como filas"""

    def __init__(self, value):
        """Inicia a lista com [] caso não haja um argumento. Caso contrário já
        inicializar um array"""
        if not value:
            self.data = [value]
        self.data = []

    def __str__(self):
        """Nos permiete imprimir a fila"""
        return str(self.data)

    def enqueue(self, value):
        """Enfileira um novo valor"""
        if not value:
            return
        self.data.append(value)

    def dequeue(self):
        """Retira o primeiro valor da fila. Retorna None se a fila
        estiver vazia"""
        if not self.data:
            return None
        return self.data.pop(0)

    def peek(self):
        """Retorna o primeiro valor da fila. Retorna None se a fila
        estiver vazia"""
        if not self.data:
            return None
        return self.data[0]
