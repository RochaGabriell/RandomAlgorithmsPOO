from ferramenta import FerramentaInterface

class Bussula(FerramentaInterface):
    def __init__(self, nome, composicao, circunferencia):
        super().__init__(nome, composicao)
        self.circunferencia = circunferencia
    
    def get_finalidade(self):
        return 'Localização'
    
    def get_poderDano(self):
        if self.composicao == 'pedra':
            return 10
        elif self.composicao == 'diamante':
            return 35
        elif self.composicao == 'ouro':
            return 50