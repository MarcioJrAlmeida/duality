import random

def escolher_acao():
    """Exibe as opções de ação de combate e retorna a escolha do jogador."""
    print("Escolha sua ação:")
    print("1 - Atacar")
    print("2 - Defender")
    return input("Opção: ")

def escolher_tipo_ataque():
    """Exibe os tipos de ataque disponíveis e retorna o tipo escolhido."""
    print("Escolha seu tipo de ataque:")
    print("1 - Espada")
    print("2 - Mágico")
    print("3 - Distância")
    escolha = input("Opção: ")
    return {"1": "Espada", "2": "Mágico", "3": "Distância"}.get(escolha, "Espada")

def escolher_defesa():
    """Exibe os tipos de defesa disponíveis e retorna a defesa escolhida."""
    print("Escolha sua defesa:")
    print("1 - Escudo (Físico)")
    print("2 - Escudo Mágico")
    print("3 - Escudo à Distância")
    escolha = input("Opção: ")
    return {"1": "Escudo", "2": "Escudo Mágico", "3": "Escudo à Distância"}.get(escolha, "Nenhum")

def rolar_dado():
    """Gera um valor aleatório de 1 a 20, simulando um dado D20."""
    return random.randint(1, 20)