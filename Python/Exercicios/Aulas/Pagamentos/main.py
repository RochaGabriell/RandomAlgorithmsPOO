from pedido import Pedido
from Pedido.pagamentoBoleto import PagamentoBoleto
from Pedido.pagamentoCartaoCredito import PagamentoCartaoCredito
from Pedido.PagamentoCartaoDebito import PagamentoCartaoDebito

pedido = Pedido(23421423, 54.20)

cartao_de_Debito = PagamentoCartaoDebito()

pedido.pagarConta(cartao_de_Debito)
