public class Main{
    public static void main(String[] args) {
        Pokemon bubasauro = new Pokemon();
        bubasauro.setNumero(1);
        bubasauro.setNome("Bubasauro");
        bubasauro.setDefesa(10);
        bubasauro.setAtaque(10);
        bubasauro.setSaude(5);
        bubasauro.setAtaqueEspecial(10);
        bubasauro.setDefesaEspecial(8);
        bubasauro.setVelocidade(8);
        bubasauro.setGenero("M");

        System.out.println("Pokemon: " + bubasauro.getNome());
        bubasauro.defender();
        bubasauro.restaurarVida();
        bubasauro.golpear();
    }
}