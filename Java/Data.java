import java.util.Scanner;
import java.io.FileWriter;
import java.util.ArrayList;

public class Data {
  public String file;
  public Scanner scan;
  public FileWriter writer;
  public int count = -1;
  public String[] lines;

  public Data(String file) {
    this.file = file;
  }

  public String[] getData() {
    scan = new Scanner(file);
    while (scan.hasNextLine()) {
      count++;
      System.out.println(scan.nextLine());
    }
    return lines;
  }

  public void setData(String data) {
    try {
      writer = new FileWriter(file);
      System.out.println("Setting Data: " + data);
      writer.write(data);
      writer.close();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}