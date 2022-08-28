from mochila import Mochila
from itens import Itens

def main():
    var = Mochila("Acer", "Preta", 3)
    var.__str__()

    for i in range(3):
        nome = str(input("Nome: "))
        peso = int(input("Peso: "))
        var.colocar_mochila(Itens(nome, peso)) 

if __name__ == "__main__":
    main()