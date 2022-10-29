from abc import ABC, abstractmethod
class FerramentaInterface():
    def __init__(self, nome, composicao) -> None:
        self.nome = nome
        self.composicao = composicao
    
    @abstractmethod
    def get_finalidade(self) -> str:
        pass
    
    @abstractmethod
    def get_poderDano(self)  -> int:
        pass