import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    String message = input.nextLine();
    int numbersad = 0;
    int numberhappy = 0;
    for(int i = 0; i < message.length()- 2; i++){
      if (message.substring(i, i +3).equals(":-)")){
        numberhappy ++;
      }
      if(message.substring(i,i+3).equals(":-(")){
        numbersad ++;
      }
    }
    if (numbersad > numberhappy){
      System.out.println("sad");
    }
    else if(numbersad < numberhappy){
      System.out.println("happy");
    }
    else if (numbersad == 0 && numberhappy == 0){
      System.out.println("none");
    }
    else{
      System.out.println("unsure");
    }
   
  }
}
