package Java.Conceito_Linguagem;
import java.util.Scanner; // Tem que ser feito a importação da biblioteca do Scanner do Java

public class scanner {
    public static void main(String[] args){
        Scanner teclado = new Scanner(System.in); // Cria um objeto dá class Scanner

        int n1, n2, res;
        /*
        float numF = teclado.nextFloat();
        int num1 = teclado.nextInt();
        byte byte1 = teclado.nextByte();
        long lg1 = teclado.nextLong();
        boolean b1 = teclado.nextBoolean();
        double num2 = teclado.nextDouble();
        String nome = teclado.nextLine();
        */

        System.out.println("Digite dois valores int: ");
        n1 = teclado.nextInt();
        n2 = teclado.nextInt();
        res = n1+n2;
        System.out.printf("Soma de %d + %d = %d", n1, n2, res); 
    }
}
