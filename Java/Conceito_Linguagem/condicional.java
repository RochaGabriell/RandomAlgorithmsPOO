package Java.Conceito_Linguagem;
public class condicional{
    public static void main(String[] args){
        
        int num; // Ou int num = 1;
        String res;
        num = 1;

        /*
        ==, >, <, >=, <=. 

        && E (“logical AND”) a && b
        Retorna true se a e b forem ambos true. Senão retorna false. Se a for false, b não é avaliada.

        & E (“boolean logical AND”) a & b
        Retorna true se a e b forem ambos true. Senão retorna false. Ambas expressões a e b são sempre avaliadas.

        || OU (“logical OR”) a || b
        Retorna true se a ou b for true. Senão retorna false. Se a for true, b não é avaliada.

        | OU (“boolean logical inclusive OR”) a | b
        Retorna true se a ou b for true. Senão retorna false. Ambas expressões a e b são sempre avaliadas.

        ^ OU EXCLUSIVO (“boolean logical exclusive OR”) a ^ b
        Retorna true se a for true e b for false ou vice-versa. Senão retorna false.

        ! NÃO (“logical NOT”) !a
        Retorna true se a for false. Senão retorna false.

        != DIFERENTE ("Operador matemático") a != b
        Retorna true se a for diferente de b. Senão retorna false.
        */

        // Estrutura if, else if e else
        if (num > 0){
            System.out.println("O número é maior que 0");
        }
        else{
            System.out.println("O número é menor que 0");
        }
        // SWITCH
        switch(num){
            case 1:
                System.out.println("1º");
                break;
            case 2:
                System.out.println("2º");
                break;
            default:
                System.out.println("Não é 1 ou 2.");
                break;
        }
        // Operador Ternário
        res = (num == 1? "O número é 1" : "O número não é 1");
        System.out.println("Resultado: " + res);
    }
}