from typing import Type
from Interface.pagamento import PagamentoInterface

class Pedido():
    def __init__(self, notaFiscalPedido: int, valorTotalPedido: float) -> None:
        self.notaFiscalPedido = notaFiscalPedido
        self.valorTotalPedido = valorTotalPedido

    def pagarConta(self, formaPagamento: Type[PagamentoInterface]) -> None:
        pagamento = formaPagamento.quitarPedido()
        print(f"Nota Fiscal Nº {self.notaFiscalPedido}\nValor: {self.valorTotalPedido}\nForma de Pagamento: {pagamento}")