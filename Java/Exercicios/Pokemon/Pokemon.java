public class Pokemon extends PokemonAbstract {
    public void restaurarVida() {
        setSaude(10);
        System.out.println("Vida restaurada: " + getSaude());
    }

    public void golpear() {
        System.out.println("Golpeando");
    }

    public void defender() {
        System.out.println("Defendido!!!");
    }
    
}