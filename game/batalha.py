from estruturas.fila import Fila
from game.persona import Heroi, Inimigo
from utils.acao import rolar_dado, escolher_acao, escolher_tipo_ataque, escolher_defesa

def verificar_aparicao_inimigo(inimigo: Inimigo) -> bool:
    """Determina aleatoriamente se um inimigo aparece, com base em uma rolagem de dado.
    O Dragão (chefe final) sempre aparece."""
    if inimigo.nome == "Dragão":
        print("⚔️ Um Dragão colossal bloqueia o caminho... não há como escapar!")
        return True
    chance = rolar_dado()
    porcentagem = int((chance / 20) * 100)
    print(f"Você rolou {chance} (~{porcentagem}%) para encontrar um inimigo...")
    if chance > 10:
        print(f"Um {inimigo.nome} ameaçador apareceu... prepare-se!")
        return True
    else:
        print("Nada aqui. A sala está vazia.")
        return False

def aplicar_defesa(tipo_inimigo: str, defesa_escolhida: str, dano: int) -> int:
    """Aplica a lógica de defesa, reduzindo o dano conforme a combinação de ataque e defesa."""
    if tipo_inimigo == "Espada" and defesa_escolhida == "Escudo":
        return int(dano * 0.5)
    elif tipo_inimigo == "Mágico" and defesa_escolhida == "Escudo Mágico":
        return int(dano * 0.5)
    elif tipo_inimigo == "Fogo" and defesa_escolhida == "Escudo à Distância":
        return int(dano * 0.5)
    elif tipo_inimigo == "Fogo" and defesa_escolhida == "Escudo Mágico":
        return 0
    return dano

class Batalha:
    """Gerencia o sistema de combate do jogo."""
    
    def __init__(self, heroi: Heroi, historico: Fila):
        self.heroi = heroi
        self.historico = historico
        self.defesa_preparada = None  # Guarda a defesa preparada pelo herói

    def iniciar_combate(self, inimigo: Inimigo) -> bool:
        """Inicia e gerencia um combate completo."""
        self.historico.enfileirar(f"Combate contra {inimigo.nome} iniciado!")
        # Determina quem começa
        turno = self._determinar_iniciativa(inimigo)
        print(f"{inimigo.nome} aparece! Prepare-se para lutar!")

        while self.heroi.hp > 0 and inimigo.hp > 0:
            if turno == "heroi":
                self._turno_heroi(inimigo)
            else:
                self._turno_inimigo(inimigo)
            # Alterna turnos
            turno = "inimigo" if turno == "heroi" else "heroi"

        return self._verificar_resultado(inimigo)

    def _turno_heroi(self, inimigo: Inimigo) -> None:
        """Executa as ações do turno do herói."""
        print("\nSeu turno:")
        print(f"Seu HP: {self.heroi.hp} | HP do {inimigo.nome}: {inimigo.hp}")
    
        while True:
            acao = escolher_acao()  # 1 - Atacar, 2 - Defender
            if acao == "1":  # Jogador optou por atacar
                tipo_atk = escolher_tipo_ataque()  # tipo de ataque escolhido
                # Calcula dano: ataque base do herói + dado D20
                dano = self.heroi.ataque.obter(tipo_atk) + rolar_dado()
                if tipo_atk == inimigo.fraqueza:
                    dano *= 2  # Dano dobrado se o ataque for eficaz contra a fraqueza
                    print("Ataque super efetivo! Dano dobrado!")
                inimigo.receber_dano(dano)
                self.historico.enfileirar(f"Você atacou com {tipo_atk} causando {dano} de dano")
                print(f"Você causou {dano} de dano ao {inimigo.nome}!")
                break  # turno do herói concluído
            
            elif acao == "2":  # Jogador optou por defender
                defesa = escolher_defesa()  # tipo de defesa escolhido
                if defesa == "Nenhum":
                    print("Opção inválida! Tente novamente.")
                    continue  # retorna ao início do loop se entrada inválida
                self.defesa_preparada = defesa  # prepara a defesa para o próximo ataque inimigo
                self.historico.enfileirar(f"Você se preparou para defender com {defesa}")
                print(f"Você se preparou para defender com {defesa} no próximo turno!")
                break  # sai do loop, passa o turno para o inimigo
            
            else:
                print("Opção inválida! Tente novamente.")
                continue


    def _turno_inimigo(self, inimigo: Inimigo) -> None:
        """Executa as ações do turno do inimigo."""
        print(f"\nTurno do {inimigo.nome}:")
        dano = rolar_dado()  # Dano base do inimigo

        # Aplica o tipo de ataque do inimigo
        if inimigo.tipo_atk == "Espada":
            dano += 10
        elif inimigo.tipo_atk == "Mágico":
            dano += 8
        elif inimigo.tipo_atk == "Fogo":
            dano += 12  # Dragão é mais forte

        if self.defesa_preparada is not None:
            dano = aplicar_defesa(inimigo.tipo_atk, self.defesa_preparada, dano)
            self.defesa_preparada = None
        self.heroi.receber_dano(dano)
        self.historico.enfileirar(f"{inimigo.nome} atacou com {inimigo.tipo_atk} causando {dano} de dano")
        print(f"{inimigo.nome} te atacou causando {dano} de dano!")

    def _determinar_iniciativa(self, inimigo: Inimigo) -> str:
        """Determina quem começa o combate."""
        ini_heroi = rolar_dado() + 5  # Herói tem pequena vantagem
        ini_inimigo = rolar_dado()
        print(f"Iniciativa: Herói {ini_heroi} vs {inimigo.nome} {ini_inimigo}")
        return "heroi" if ini_heroi >= ini_inimigo else "inimigo"

    def _verificar_resultado(self, inimigo: Inimigo) -> bool:
        """Verifica o resultado do combate."""
        if self.heroi.hp <= 0:
            self.historico.enfileirar("Você foi derrotado!")
            print("Você foi derrotado!")
            return False
        self.historico.enfileirar(f"{inimigo.nome} foi derrotado!")
        print(f"Você derrotou {inimigo.nome}!")
        self.heroi.restaurar_vida()
        return True

    def tentar_fuga(self, inimigo: Inimigo) -> bool:
        """Tenta fugir do combate contra o inimigo. Retorna True se a fuga foi bem-sucedida (nenhum combate ocorre) 
        ou se o herói venceu o combate após a fuga falhar. Retorna False se o herói foi derrotado."""
        dado_heroi = rolar_dado()
        dado_inimigo = rolar_dado()
        print(f"Fuga - Herói: {dado_heroi} vs Inimigo: {dado_inimigo}")
        self.historico.enfileirar(f"Tentativa de fuga: Herói({dado_heroi}) vs Inimigo({dado_inimigo})")
        if dado_heroi > dado_inimigo:
            print("Fuga bem-sucedida!")
            self.historico.enfileirar("Fuga bem-sucedida.")
            return True
        else:
            print("Fuga falhou! Você deve se defender.")
            self.historico.enfileirar("Fuga falhou. Combate iniciado com defesa.")
            # Inimigo realiza um ataque inicial enquanto o herói tenta se defender
            self._turno_inimigo(inimigo)
            if self.heroi.hp <= 0:
                return False
            # Prossegue para o combate normal após a falha na fuga
            return self.iniciar_combate(inimigo)
