package Java.Conceito_Linguagem;

public class loop {
    public static void main(String[] args){
        
        for (int i = 0; i < 5; i++){ // for(inicialização; condição; incremento/decremento) 
            System.out.println(i);
        }

        int cont = 0;
        while (cont < 5) { // while(condição) 
        System.out.println(cont);
        cont++;
        }

        // A instrução "break" é usada para sair de um loop.
        for (int i = 0; i < 10; i++) { // Este exemplo interrompe o loop quando i é igual a 4:
            if (i == 4) {
                break;
            }
            System.out.println(i);
        }

        // A instrução "continue" interrompe uma iteração (no loop), se ocorrer uma condição especificada, e continua com a próxima iteração no loop.
        for (int i = 0; i < 10; i++) { // Este exemplo ignora o valor de 4:
            if (i == 4) {
                continue;
            }
            System.out.println(i);
        }
    }
}
