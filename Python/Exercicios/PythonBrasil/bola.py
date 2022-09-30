class Bola:
    """
    cor = public
    _cor = protected
    __cor = private
    """
    def __init__(self, cor: str, circunferencia: float, material: str) -> None:
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    @property #  getter para obter valor fora da classe/objeto
    def cor(self) -> str:
        return self._cor

    @cor.setter #  # setter para setar valor fora da classe/objeto
    def cor(self, cor) -> None:
        self._cor = cor

bola = Bola('Branco', 10, 'Borracha')
print(bola.cor)
bola.cor = "Preto"
print(bola.cor)