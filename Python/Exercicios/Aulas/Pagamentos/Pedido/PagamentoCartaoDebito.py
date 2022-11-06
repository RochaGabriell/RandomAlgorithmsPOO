from Interface.pagamento import PagamentoInterface

class PagamentoCartaoDebito(PagamentoInterface):
    def quitarPedido(self) -> str:
        return "Pamento via Cartão de Debito!"