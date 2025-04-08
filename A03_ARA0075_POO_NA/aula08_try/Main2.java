package aula08_try;
import java.io.IOException;
class ExemploThrows {
    void umMetodo(int num) throws IOException, ArithmeticException{
        if (num == 1){
            throw new IOException("IOException");
        }else{
            throw new ArithmeticException("ArithmeticException");
        }
    }
}
public class Main2 { 
    public static void main(String[] args) {
        try{
            ExemploThrows obj = new ExemploThrows();
            obj.umMetodo(2);
        }catch(IOException | ArithmeticException ex){
            System.out.println(ex);
        }
    }  
}
