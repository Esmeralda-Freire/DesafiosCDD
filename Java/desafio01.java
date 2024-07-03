package desafio;
import java.util.Scanner;

public class desafio01 {

	public static void main(String[] args) {
		System.out.println("Responda com 1-Sim 2-Não");
		 Scanner entrada = new Scanner(System.in);
		 System.out.println("Telefonou para a vítima?\n");
		 int resp = entrada.nextInt();
		 System.out.println("Esteve no local do crime?\n");
		 int resp2 = entrada.nextInt();
		 System.out.println("Mora perto da vítima?\n");
		 int resp3 = entrada.nextInt();
		 System.out.println("Devia para a vítima?\n");
		 int resp4 = entrada.nextInt();
		 System.out.println("Já trabalhou com a vítima?\n");
		 int resp5 = entrada.nextInt();
		 
		 int contagem = 0;
		 
		 if(resp == 1) {
			 contagem++;
			 System.out.println(contagem);
		 }
		 if(resp2 == 1) {
			 contagem++;
		 }
		 if(resp3 == 1) {
			 contagem++;
		 }
		 if(resp4 == 1) {
			 contagem++;
		 }
		 if(resp5 == 1) {
			 contagem++;
		 }
		 
		 if (contagem == 5) {
			 System.out.println("Assassino");
		 }
		 else if (contagem == 2) {
			 System.out.println("Suspeita");
		 }
		 else if (contagem == 3 || contagem == 4) {
			 System.out.println("Cúmplice");
		 }
		 else{
			 System.out.println("Inocente");
		 }
		 
		 entrada.close();

	}

}
