from jogador import Jogador
from machado import Machado
from bussula import Bussula

gamer = Jogador('Gabriel')

ferramenta_machado = Machado('Machado Glorioso', 'ouro', '0.30', '0.70')
print(ferramenta_machado.nome)
print(ferramenta_machado.get_finalidade())

ferramenta_bussula = Bussula('Bussula Sagrada', 'diamante', '0.10')
print(ferramenta_bussula.nome)
print(ferramenta_bussula.get_finalidade())

gamer.atacar_personagem(ferramenta_machado)

gamer.atacar_animal(ferramenta_bussula)