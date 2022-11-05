class Pokemon:
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

        self.__golpe1 = ""
        self.__golpe2 = ""
        self.__golpe3 = ""
        self.__golpe4 = ""

    @property
    def golpe1(self) -> str:
        return self.__golpe1

    @golpe1.setter
    def golpe1(self, golpe1: str) -> None:
        self.__golpe1 = golpe1
        
    @property
    def golpe2(self) -> str:
        return self.__golpe2

    @golpe2.setter
    def golpe2(self, golpe2: str) -> None:
        self.__golpe2 = golpe2

    @property
    def golpe3(self) -> str:
        return self.__golpe3

    @golpe3.setter
    def golpe3(self, golpe3: str) -> None:
        self.__golpe3 = golpe3

    @property
    def golpe4(self) -> str:
        return self.__golpe4

    @golpe4.setter
    def golpe4(self, golpe4: str) -> None:
        self.__golpe4 = golpe4

    def golpear(self, golpe: int) -> None:
        if golpe == 1:
            print(f"Golpe: {self.__golpe1}")
        if golpe == 2:
            print(f"Golpe: {self.__golpe2}")
        if golpe == 3:
            print(f"Golpe: {self.__golpe3}")
        if golpe == 4:
            print(f"Golpe: {self.__golpe4}")

    def restaurarVida(self) -> None:
        saude = 10
        print(f"Vida restaurada: {saude}")

    def defender(self) -> None:
        print("Defendido...")



if __name__ == "__main__":
    bubasauro = Pokemon(1, "Bubasauro", 10, 10, 10, 15, 15, 10, "F")
    bubasauro.golpe1 = "TACKLE"
    bubasauro.golpe2 = "GROWL"
    bubasauro.golpe3 = "LEECH SEED"
    bubasauro.golpe4 = "VINE WHIP"

    print(f"Pokemon é: {bubasauro.nome}")
    bubasauro.restaurarVida()

    # print(bubasauro.golpe1)
    # print(bubasauro.golpe2)
    # print(bubasauro.golpe3)
    # print(bubasauro.golpe4)