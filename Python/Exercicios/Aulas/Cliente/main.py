from clienteNegocio import ClienteNegocio
from Interface.clienteEntidade import ClienteEntidadeInterface
from Interface.clienteFiltro import ClienteFiltroInterface

negocio = ClienteNegocio()

clientePessoa = ClienteEntidadeInterface(1, "João", "01/01/2000", True)
clientePessoa2 = ClienteEntidadeInterface(2, "Maria", "01/01/2000", True)

clienteFiltro = ClienteFiltroInterface("João")

negocio.incluir(clientePessoa)
negocio.incluir(clientePessoa2)

print(negocio.buscarPorFiltro(clienteFiltro))

print(negocio.buscarPorIdentificador(2))

negocio.alterar(clientePessoa2)

negocio.excluir(clientePessoa)