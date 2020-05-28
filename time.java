import java.util.*;
import java.util.concurrent.TimeUnit;

public class time {
    private static boolean choice() {
        System.out.println("true면 y false면 n 입력");
        Scanner scanner = new Scanner(System.in);

        String ch = scanner.next();

        if (ch.equals("y")) return true;
        else return false;
    }

    public static void main(String args[]) {
        boolean ch = choice();
        while(true) {
            if (!ch) {
                System.out.println("Done");
                break;
            }
            Date now = new Date();
            System.out.println(now.toString());
    
            try {
                TimeUnit.SECONDS.sleep(4);
            } catch (InterruptedException exception) {
                exception.getStackTrace();
            }
            
            Date after = new Date();
            System.out.println(after.toString());

            ch = choice();
        }
        
    }
}