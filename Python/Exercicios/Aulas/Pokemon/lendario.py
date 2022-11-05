from pokemon import Pokemon

class Lendario(Pokemon):
    def __init__(self, numero: int, nome: str, ataque: int, defesa: int, saude: int, ataqueEspecial: int, defesaEspecial: int, velocidade: int, genero: str, habilidadeExtra: str) -> None:
        super().__init__(numero, nome, ataque, defesa, saude, ataqueEspecial, defesaEspecial, velocidade, genero)
        self.habilidadeExtra = habilidadeExtra

    def golpearDuplo(self, golpe: int) -> None:
        print(f"Dois golpes seguidos: {golpe}")

    def restaurarVida(self) -> None:
        saude = 100
        print(f"Vida restaurada: {saude}")


if __name__ == "__main__":
    mewtwo = Lendario(150, "Mewtwo", 20, 10, 20, 10, 10, 10, "M", "Habilidade Extra")
    mewtwo.golpe1 = "CONFUSION"
    mewtwo.golpe2 = "PYSICHIC"
    mewtwo.golpe3 = "PYSTRIKE"
    mewtwo.golpe4 = "PSYCHO CUT"

    print(f"Pokemon é: {mewtwo.nome}")
    mewtwo.restaurarVida()

    # mewtwo.golpearDuplo(1)
    # mewtwo.golpear(2)