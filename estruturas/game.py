
import random
import time
from fila import Queue as Fila
from arvore_binaria import Sala
from hash_map import inimigos_por_nivel
from heap_sort import heapsort

historico = Fila()
game_over = False

class Heroi:
    def __init__(self):
        self.ataque = {
            "Espada": 10,
            "Mágico": 8,
            "Distância": 7
        }
        self.defesa = {
            "Espada": 5,
            "Mágico": 6,
            "Distância": 4
        }
        self.hp = 100

    def restaurar_vida(self):
        self.hp = 100
        print("[HP RESTAURADO] +100 pontos de vida 🧥")

heroi = Heroi()

def carregando(mensagem="Carregando"):
    for i in range(3):
        print(mensagem + "." * (i + 1))
        time.sleep(0.5)

def rolar_dado():
    return random.randint(1, 20)

def verificar_aparicao_inimigo(nivel):
    if nivel == 4:
        print("⚔️ Um Dragão colossal bloqueia o caminho... não há como escapar!")
        return True
    chance = rolar_dado()
    porcentagem = int((chance / 20) * 100)
    inimigo = inimigos_por_nivel[nivel]["nome"]
    print(f"Você rolou {chance} (~{porcentagem}%) para encontrar um inimigo...")
    if chance > 10:
        print(f"Um {inimigo} ameaçador apareceu... prepare-se!")
        return True
    else:
        print("Nada aqui. A sala está vazia.")
        return False

def escolher_acao():
    print("Escolha sua ação:")
    print("1 - Atacar")
    print("2 - Defender")
    return input("Opção: ")

def escolher_tipo_ataque():
    print("Escolha seu tipo de ataque:")
    print("1 - Espada")
    print("2 - Mágico")
    print("3 - Distância")
    escolha = input("Opção: ")
    return {"1": "Espada", "2": "Mágico", "3": "Distância"}.get(escolha, "Espada")

def escolher_defesa():
    print("Escolha sua defesa:")
    print("1 - Escudo (Físico)")
    print("2 - Escudo Mágico")
    print("3 - Escudo à Distância")
    escolha = input("Opção: ")
    return {"1": "Escudo", "2": "Escudo Mágico", "3": "Escudo à Distância"}.get(escolha, "Nenhum")

def calcular_dano(tipo, base, fraqueza):
    if tipo == fraqueza:
        print("Ataque eficaz contra a fraqueza do inimigo! Dano dobrado!")
        return base * 2
    return base

def aplicar_defesa(tipo_inimigo, defesa_escolhida, dano_recebido):
    if tipo_inimigo == "Espada" and defesa_escolhida == "Escudo":
        return int(dano_recebido * 0.5)
    elif tipo_inimigo == "Mágico" and defesa_escolhida == "Escudo Mágico":
        return int(dano_recebido * 0.5)
    elif tipo_inimigo == "Fogo" and defesa_escolhida == "Escudo à Distância":
        return int(dano_recebido * 0.5)
    elif tipo_inimigo == "Fogo" and defesa_escolhida == "Escudo Mágico":
        return 0
    return dano_recebido

def turno_batalha(inimigo, fraqueza):
    dado_heroi = rolar_dado()
    dado_inimigo = rolar_dado()
    print(f"Iniciativa - Herói: {dado_heroi} vs {inimigo['nome']}: {dado_inimigo}")
    return "heroi" if dado_heroi >= dado_inimigo else "inimigo"

def iniciar_combate(nivel, defesa_forcada=False):
    inimigo = inimigos_por_nivel[nivel].copy()
    tipo_ataque_inimigo = inimigo["ataque_tipo"]
    fraqueza = inimigo["fraqueza"]
    historico.enqueue(f"Início do combate contra {inimigo['nome']} (Nível {nivel})")

    carregando("Iniciando batalha")

    turno = "heroi" if not defesa_forcada else "defesa"

    while heroi.hp > 0 and inimigo["HP"] > 0:
        turno = turno_batalha(inimigo, fraqueza)

        if turno == "heroi":
            acao = escolher_acao()
            if acao == "1":
                tipo = escolher_tipo_ataque()
                dado = rolar_dado()
                dano = calcular_dano(tipo, dado, fraqueza)
                inimigo["HP"] -= dano
                print(f"Herói ataca com {tipo} causando {dano} de dano. HP do inimigo: {inimigo['HP']}")
                historico.enqueue(f"Herói ataca com {tipo} causando {dano} de dano. HP Inimigo: {inimigo['HP']}")
            elif acao == "2":
                tipo_defesa = escolher_defesa()
                dado = rolar_dado()
                dano_bruto = dado
                dano_final = aplicar_defesa(tipo_ataque_inimigo, tipo_defesa, dano_bruto)
                heroi.hp -= dano_final
                print(f"{inimigo['nome']} ataca com {tipo_ataque_inimigo} causando {dano_final} de dano. HP do Herói: {heroi.hp}")
                historico.enqueue(f"Herói se defende com {tipo_defesa}")
                historico.enqueue(f"{inimigo['nome']} ataca com {tipo_ataque_inimigo} causando {dano_final} de dano. HP Herói: {heroi.hp}")
        else:
            dado = rolar_dado()
            heroi.hp -= dado
            print(f"{inimigo['nome']} ataca com {tipo_ataque_inimigo} causando {dado} de dano. HP do Herói: {heroi.hp}")
            historico.enqueue(f"{inimigo['nome']} ataca com {tipo_ataque_inimigo} causando {dado} de dano. HP Herói: {heroi.hp}")

    if heroi.hp <= 0:
        print_derrota()
        return False
    else:
        print(f"{inimigo['nome']} foi derrotado!")
        historico.enqueue(f"{inimigo['nome']} foi derrotado.")
        heroi.restaurar_vida()
        return True

def tentar_fuga(nivel):
    dado_heroi = rolar_dado()
    dado_inimigo = rolar_dado()
    print(f"Fuga - Herói: {dado_heroi} vs Inimigo: {dado_inimigo}")
    historico.enqueue(f"Tentativa de fuga: Herói({dado_heroi}) vs Inimigo({dado_inimigo})")
    if dado_heroi > dado_inimigo:
        print("Fuga bem-sucedida!")
        historico.enqueue("Fuga bem-sucedida.")
        return True
    else:
        print("Fuga falhou! Você deve se defender.")
        historico.enqueue("Fuga falhou. Combate iniciado com defesa.")
        return iniciar_combate(nivel, defesa_forcada=True)

def mover_jogador(sala_atual):
    global game_over
    if sala_atual is None or game_over:
        return

    print(f">>> Você chegou ao NÍVEL {sala_atual.nivel} <<<")
    historico.enqueue(f"Entrou no nível {sala_atual.nivel}")

    print("Você encontrou uma porta misteriosa. Deseja entrar? (S/N)")
    entrar = input().upper()
    if entrar != "S":
        print("Você decidiu não entrar nesta sala.")
        return

    if verificar_aparicao_inimigo(sala_atual.nivel):
        if sala_atual.nivel == 4:
            print("Não é possível fugir do chefe final. Prepare-se para a batalha!")
            sucesso = iniciar_combate(sala_atual.nivel)
            if sucesso:
                print_vitoria()
            game_over = True
            return
        else:
            escolha = input("Deseja combater (C) ou fugir (F)? ").upper()
            if escolha == "C":
                sucesso = iniciar_combate(sala_atual.nivel)
                if not sucesso:
                    game_over = True
                    return
            elif escolha == "F":
                sucesso = tentar_fuga(sala_atual.nivel)
                if not sucesso:
                    game_over = True
                    return
    else:
        historico.enqueue("Sala vazia")

    direcao = input("Deseja ir para Direita (D) ou Esquerda (E)? ").upper()
    if direcao == "D":
        mover_jogador(sala_atual.right)
    elif direcao == "E":
        mover_jogador(sala_atual.left)

def print_vitoria():
    print("🌟 PARABÉNS! 🌟")
    print("Você derrotou o Dragão e salvou o reino!")
    historico.enqueue("Vitória: o herói derrotou o Dragão.")
    imprimir_historia()

def print_derrota():
    print("💀 O MAL PREVALECEU 💀")
    print("O herói caiu em batalha. O reino permanece em trevas...")
    historico.enqueue("Derrota: o herói caiu em batalha.")
    imprimir_historia()

def imprimir_historia():
    print("\n===== HISTÓRICO DO HERÓI =====")
    for evento in historico.data:
        print("-", evento)

def main():
    print("Bem-vindo ao Duality - RPG de Batalha!")
    print("Em um reino outrora pacífico, criaturas sombrias emergiram das profundezas e tomaram cada canto do território.")
    print("Apenas um herói ousou se levantar para retomar a paz: VOCÊ.")
    print("---"*50)
    print("\n")

    raiz = Sala(1)
    raiz.left = Sala(2)
    raiz.right = Sala(2)
    raiz.left.left = Sala(3)
    raiz.left.right = Sala(3)
    raiz.right.left = Sala(3)
    raiz.right.right = Sala(3)
    raiz.left.left.left = Sala(4)
    raiz.left.left.right = Sala(4)
    raiz.left.right.left = Sala(4)
    raiz.left.right.right = Sala(4)
    raiz.right.left.left = Sala(4)
    raiz.right.left.right = Sala(4)
    raiz.right.right.left = Sala(4)
    raiz.right.right.right = Sala(4)

    direcao = input("Deseja iniciar indo para Direita (D) ou Esquerda (E)? ").upper()
    if direcao == "D":
        mover_jogador(raiz)
    elif direcao == "E":
        mover_jogador(raiz)

if __name__ == "__main__":
    main()
