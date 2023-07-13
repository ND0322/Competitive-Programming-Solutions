import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    int v = input.nextInt();
    String s = input.next();
    int Acount = 0;
    int Bcount = 0;
    for(int i = 0; i < v; i++){
      String temp = s.substring(i,i+1);
      if (temp.equals("A")){
        Acount+=1;
      }else{
        Bcount+=1;
      } 
    }
    if (Acount < Bcount){
      System.out.println("B");
    }
    else if(Acount > Bcount){
      System.out.println("A");
    }
    else{
      System.out.println("Tie");
    }
    
    
  }
}
