from pokemonAbstract import PokemonAbstract

class Pokemon(PokemonAbstract):
    def restaurarVida(self) -> None:
        self.saude = 10
        print(f"Vida restaurada: {self.saude}")

    def golpear(self) -> None:
        print("Golpeando!")

    def defender(self) -> None:
        print("Defendido!!!")

if __name__ == "__main__":
    bubasauro: Pokemon = Pokemon(1, "Bubasauro", 10, 10, 5, 10, 8, 8, "M")
    bubasauro.defender()
    bubasauro.restaurarVida()
    bubasauro.golpear()