from ferramenta import FerramentaInterface

class Machado(FerramentaInterface):
    def __init__(self, nome, composicao, largura, comprimento):
        super().__init__(nome, composicao)
        self.largura = largura
        self.comprimento = comprimento
    
    def get_finalidade(self) -> str:
        return 'Corta madeira'
    
    def get_poderDano(self)  -> int:
        if self.composicao == 'madeira':
            return 10
        elif self.composicao == 'pedra':
            return 30
        elif self.composicao == 'diamante':
            return 60
        elif self.composicao == 'ouro':
            return 100