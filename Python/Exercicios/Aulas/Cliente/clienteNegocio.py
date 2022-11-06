from Interface.clienteEntidade import ClienteEntidadeInterface
from Interface.clienteFiltro import ClienteFiltroInterface
from typing import Type

class ClienteNegocio():
    def __init__(self) -> None:
        super().__init__()
        self.lista = []

    def alterar(self, aCliente: Type[ClienteEntidadeInterface]) -> None:
        cliente = aCliente.nome
        for i in self.lista:
            if i.nome == cliente:
                i.status = False
                print(f"O usuário {cliente} foi alterado!")
                break
        else:
            print(f"O usuário {cliente} não foi alterado!")

    def excluir(self, aCliente: Type[ClienteEntidadeInterface]) -> None:
        cliente = aCliente.nome
        for i in self.lista:
            if i.nome == cliente:
                self.lista.remove(i)
                print(f"O usuário {cliente} foi excluído!")
                break
        else:
            print(f"O usuário {cliente} não foi excluido!")

    def buscarPorFiltro(self, aFiltro: Type[ClienteFiltroInterface]) -> list[Type[ClienteEntidadeInterface]]:
        filtro = aFiltro
        for cliente in self.lista:
            if cliente.nome == filtro.nome:
                return cliente.__dict__
        print(f"A busca por {filtro.nome} não foi encontrada!")

    def buscarPorIdentificador(self, aIdentificador: int) -> Type[ClienteEntidadeInterface]:
        for cliente in self.lista:
            if cliente.identificador == aIdentificador:
                return cliente
        print(f"O usuário com identificador {aIdentificador} não foi encontrado!")
        return 0

    def incluir(self, aCliente: Type[ClienteEntidadeInterface]) -> None:
        self.lista.append(aCliente)