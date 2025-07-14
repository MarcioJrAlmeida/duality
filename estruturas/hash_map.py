class HashMap:
    """Implementação de um dicionário com seus comportamentos.
    Ideal para ser herdado para os que queiram ser comportar como um Dict"""

    def __init__(self):
        """Inicia um dicionário vazio"""
        self.items = {}

    def drop(self):
        """Apaga o dicionário"""
        self.items.clear()

    def __str__(self):
        """Nos permiete imprimir o HashMap"""
        return str(self.items)

    def add(self, key, value):
        """Adiciona o item com o a chave key com o novo valor value.
        Caso a chave exista: Não faz nada"""
        if key in self.items:
            return
        self.items[key] = value

    def get(self, key):
        """Busca o valor da chave key.
        Caso o item não exista: Retorna None"""
        if key not in self.items:
            return None
        return self.items[key]

    def set(self, key, value):
        """Atualiza o item com o a chave key com o novo valor value.
        Caso o item não exista: insere um novo valor com chave no HashMap"""
        self.items.update({key: value})

    def values(self):
        """Retorna os valores do dicionário"""
        if not self.items:
            return None
        self.items.values()

    def keys(self):
        """Retorna as chaves do dicionário"""
        self.items.keys()
        
inimigos_por_nivel = {
    1: {
        "nome": "Goble",
        "HP": 30,
        "fraqueza": "Espada",
        "ataque_tipo": "Espada"
    },
    2: {
        "nome": "Troll",
        "HP": 50,
        "fraqueza": "Mágico",
        "ataque_tipo": "Espada"
    },
    3: {
        "nome": "Lich",
        "HP": 70,
        "fraqueza": "Distância",
        "ataque_tipo": "Mágico"
    },
    4: {
        "nome": "Dragão",
        "HP": 100,
        "fraqueza": "Distância",
        "ataque_tipo": "Fogo"
    }
}
