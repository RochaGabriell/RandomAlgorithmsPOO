class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float, altura: float) -> None:
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1

    def engordar(self, peso: float) -> float:
        self.peso += peso
        return self.peso

    def emagrecer(self, peso: float) -> float:
        self.peso -= peso
        return self.peso

    def validarIdade(self, idade):
        if idade <= 21:
            return True
        return False

    def crescer(self):
        if self.validarIdade(self.idade):
            crescer = self.altura + 0.05
            self.altura = float(f"{crescer:.2f}")

pessoa = Pessoa("Gabriel", 16, 72, 1.6)
print(pessoa.__dict__)

pessoa.engordar(3)
pessoa.envelhecer()
pessoa.crescer()
pessoa.emagrecer(2)
pessoa.envelhecer()
pessoa.crescer()
pessoa.emagrecer(2)
pessoa.envelhecer()
pessoa.crescer()
pessoa.envelhecer()
pessoa.envelhecer()
pessoa.envelhecer()
pessoa.crescer()

print(pessoa.__dict__)
