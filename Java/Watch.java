import java.util.Scanner;
import java.io.File;

public class Watch {

  public Scanner scanner;
  public final File chatFile = new File("../../chat.yaml");

  public void watchFile() throws Exception {
    scanner = new Scanner(chatFile);
    while (true) {
      while (scanner.nextLine() != null) {
        System.out.println(scanner.nextLine());
      }
    }
  }

  public static void main(String args[]) {
    try {
      new Watch().watchFile();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}