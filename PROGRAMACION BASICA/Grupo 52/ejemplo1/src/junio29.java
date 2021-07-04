
// import java.util.Scanner;

// public class junio29 {

//     public static void main(String[] args){
        // Scanner scanner = new Scanner(System.in); 
        // // Variable = input()
        // System.out.println("Ingresa una palabra");
        // // String entrada = scanner.nextLine();
        // // System.out.println(" El mensaje fue " + entrada);
        // int resultado = scanner.nextInt();
        // System.out.println("El mensaje fue " + resultado);
        // if (5>7){
        //     System.out.println(":)");
        // }else if(3>2){
        //     System.out.println("T.T");
        // }
        // else{
        //     System.out.println(":(");
        // }
        // Scanner scanner = new Scanner(System.in); 
        // System.out.println("Ingresa un animal");
        // String animal = scanner.nextLine();
        /*if (animal.equals("perro")){
            System.out.println("Woff");
        }else if(animal.equals("Gato")){
            System.out.println("Miau");
        }else{
            System.out.println("No encuentro el animal");
        }*/
        /*switch (animal){
            case "perro":
                System.out.println("Woff");
                break; 
            case "gato":
                System.out.println("Miau");
                break; 
            case "loro":
                System.out.println("quiero cacao");
                break; 
            default:
                System.out.println("no se encuentra el animal"); 
        }
        int numero = scanner.nextInt();
        switch(numero){
            case 0:
                System.out.println("es igual a 0");
                break;
            default:
                System.out.println("no es igual a 0");
        }*/
        /*int contador = 1;
        while(true){
            System.out.println(":)");
            contador = contador + 1;
            if(contador==5){
                break;
            }
        }*/
        /*int numero = 5;
        do{
            System.out.println(":)");
        }while(numero>7);*/  
        // for i in range(0,5,1): // en python 
        // for(inicia;termina;incremento)
        /*for(int i=0;i<5;i=i+1){
            System.out.println(i);
        }*/
        /*for(int i=0;i<5;i++){  // ++ es el incremento de 1
            System.out.println(i);
        }*/
        /*for(int i=7;i>0;i=i-1){
            System.out.println(i);
        }*/
        /*for(int i=7;i>0;i--){  // -- resta de 1 en 1
            System.out.println(i);
        }*/
        /*for(int i=0;i<=20;i=i+2){
            System.out.println(i);
        }*/
        // for(int i=0;i<=20;i=i+2){
        //     if(i==8){  // para saltar el 8 del (6 pasa a 10) con continue
        //         //  continue;
        //         break;  // lo deja hasta el 8 pero si colocarlo 
        //     }
        //     System.out.println(i);
        // }
//     }
// } 


// public class junio29 {

//     public static void main(String[] args){
        /*int a = 5; // expresiones (una variable vale tal cosa se le llama EXPRESIONES)
        System.out.println(5+5);
        System.out.println(5-5);
        System.out.println(5*5);
        System.out.println(5/5);
        System.out.println(5%5);
        System.out.println(Math.pow(4, 3));  // POTENCIA
        System.out.println(Math.sqrt(16));   // RAIZ CUADRADA
        System.out.println(Math.abs(3-5));   // VALOR ABSOLUTO
        System.out.println(Math.cbrt(64));*/   // RAIZ CUBICA
        /*int contador = 0;  // NUMERO ENTERO
        // contador = contador + 1
        // contador += 1   // estas dos en python 
        contador = contador + 1;
        contador += 1;  // el valor anterior + 1
        contador -= 3;  // EL VALOR ANTERIOR MENOS 3 
        contador *= 7;  // EL VALOR ANTERIO POR 7
        contador /= 5;  // EL VALOR ANTERIOR DIVIDO EN 5
        contador %= 2;  // EL VALOR ANTERIO MODULO 2
        System.out.println(contador);*/
        // for(int i=0;i<5;i++){ // ++ es el incremento de 1
        //     System.out.println(i);
        // }
        // for(int i=7;i>0;i--){  // -- resta de 1 en 1
        //     System.out.println(i);
        // }
        // int numero = 1;
        // System.out.println(numero++);  // LO MUESTRA
        // System.out.println(++numero);   // LO INCREMENTA DE UNA VEZ 
        // System.out.println(numero);  // DESPUES DE MOSTRARLO EN LA PRIMERA LO INCREMENTA 
        
        // System.out.println(numero--);
        // System.out.println(++numero);


        // char caracter = 'z';
        // System.out.println(++caracter);
        // System.out.println(--caracter);
        // caracter += 2;
        // System.out.println(++caracter);
        
        /*if (5 != 2){
            System.out.println(":)");
        }else{
            System.out.println(":(");
        }*/
        /*String resultado = 5 > 2 ? ":)" : ":("; 
        System.out.println(resultado);*/ 
//     }
// }



public class junio29 {

    public static void main(String[] args){

        // AND -> &, OR -> |, NOT -> !
        // if 5>3 and 4>6:
        // if (5>3 & 4>6){
        //     System.out.println("?");
        // }
        // if (5>3 | 4>6){  // en python es (or) 
        //     System.out.println("?");
        // }
        // if (!(5==1)){  // negacion (not) es python 
        //     System.out.println(":)");
        // }
        // if (5>7 & 8>3 & 9>5 & 6>0 & 10>1){
        //     System.out.println(":)");
        // }
        if (5>7 ^ 5>1){ 
            System.out.println(":)");
        }else{
            System.out.println("se gano el regaño");
        }
    }
}