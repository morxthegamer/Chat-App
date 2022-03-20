import java.util.Scanner;
import java.io.BufferedWriter;
import java.io.FileWriter;

public class Data {
  public String file;
  public Scanner scan;
  public BufferedWriter writer;
  public FileWriter write;

  public Data(String file) {
    this.file = file;
  }

  public void getData() {
    try {
      scan = new Scanner(file);
      while (scan.nextLine() != null) {
        System.out.println(scan.nextLine());
      }
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  public void setData(String data) {
    try {
      writer = new BufferedWriter(new FileWriter(file));
      System.out.println("Setting Data: " + data);
      writer.write(data);
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}