package Ciclo2.Clases.Unidad1;
import java.util.Scanner; 

public class junio29d {

    public static void main(String args[]){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Ingresa el numero:");
        int numero = scanner.nextInt();
        int resultado = contadorDigitos(numero);
        System.out.println(resultado);
    }

    public static int contadorDigitos(int numero){
        int cifras = 0;
        while(numero!=0){
            numero /= 10;
            cifras++;
        }
        return cifras;
    }
    
}
