from typing import Type
from ferramenta import FerramentaInterface

class Jogador:
    def __init__(self, nome):
        self.nome = nome
    
    def atacar_animal(self, ferramenta: Type[FerramentaInterface]):
        ataque = ferramenta.get_poderDano()
        print(f'{self.nome} deu {ataque} de ataque com o {ferramenta.nome} no Cavalo')
    
    def atacar_personagem(self, ferramenta: Type[FerramentaInterface]):
        ataque = ferramenta.get_poderDano()
        print(f'{self.nome} deu {ataque} de ataque com o {ferramenta.nome} no Zumbi')