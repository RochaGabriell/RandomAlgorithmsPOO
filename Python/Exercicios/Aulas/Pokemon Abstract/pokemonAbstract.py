from abc import ABC, abstractmethod

class PokemonAbstract(ABC):
    def __init__(self, numero: int, nome: str, ataque: int, defesa: int, saude: int, ataqueEspecial: int, defesaEspecial: int, velocidade: int, genero: str) -> None:
        self.numero = numero
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa
        self.saude = saude
        self.ataqueEspecial = ataqueEspecial
        self.defesaEspecial = defesaEspecial
        self.velocidade = velocidade
        self.genero = genero

    @abstractmethod
    def restaurarVida(self) -> None:
        pass

    @abstractmethod
    def golpear(self) -> None:
        pass

    @abstractmethod
    def defender(self) -> None:
        pass