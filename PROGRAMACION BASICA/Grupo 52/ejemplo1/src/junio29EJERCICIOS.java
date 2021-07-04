import java.util.Scanner;

// public class junio29EJERCICIOS {
    
    // public static void main(String[] args){

        // LA FORMA FACIL DE MOSTRAR UN MENSAJE
        // Scanner scanner = new Scanner(System.in);
        // System.out.println("Ingresa tu nombre");
        // String nombre = scanner.nextLine();
        //System.out.println("Hola " + nombre); 
        // System.out.println(saludar(nombre));
    // }

    // ESTO ES PARA UNA FUNCION 
    //def ejemploFuncion(variable1:int)->float: -> // ESTO SE UTILIZA EN PYTHON
    // public static String saludar(String nombre){   //-> // Y ESTA ES UNA FUNCION EN JAVA 
    //     return "Hola " + nombre;
    // } 
// }

// NO SE TIENE ORDEN PARA LAS FUNCIONES 

// EJERCICIOS PARA SABER CUANTAS UNIDADES TIENE UN NUMERO 
public class junio29EJERCICIOS {
    
    public static void main(String[] args){   // VOID ES VACIO ASI QUE NO RETORNA NADA NO ESPERA QUE RETORNE NADA 
        Scanner scanner = new Scanner(System.in);
        int numero = scanner.nextInt();
        int resultado = contadorDigitos(numero);
        //System.out.println(resultado);
        switch (contadorDigitos(numero)){
            case 1:
                System.out.println("Muy poquitos digitos");
                break;
            default:
                System.out.println("Hay muchos digitos");
        }
    }
    public static int contadorDigitos(int numero){
        int cifras = 0;
        while(numero != 0){
            numero /= 10;
            cifras++;   // se aumenta en una vuelta 
        }
        return cifras;
    }

}