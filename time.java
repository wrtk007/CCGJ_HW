import java.util.*;
import java.util.concurrent.TimeUnit;

public class time {

    static int help = 0;
    private static boolean checkcount(int num) {
        if(num%2 == 0) {
            return false;
        }
        else return true;

    }

    private static int choice(int count) {
        System.out.println("true면 y false면 n 입력");
        Scanner scanner = new Scanner(System.in);

        String ch = scanner.next();
        if (ch.equals("y"))  {
            count++;
            System.out.println(count);
        }
        else System.out.println(count);
        return count;
    }

    public static void main(String args[]) {
        boolean ch = checkcount(choice(help));
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

            ch = checkcount(choice(help));
        }
        
    }
}