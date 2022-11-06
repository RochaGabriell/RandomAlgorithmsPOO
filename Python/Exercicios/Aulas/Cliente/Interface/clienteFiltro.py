from abc import ABC, abstractmethod
from datetime import datetime

class ClienteFiltroInterface(ABC):
    def __init__(self, nome: str, dataCadastro: datetime = datetime.now()) -> None:
        self.nome = nome
        self.dataCadastro = dataCadastro