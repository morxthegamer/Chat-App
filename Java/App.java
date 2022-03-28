import java.util.Scanner;
import java.util.*;

public class App {
  public ArrayList<String> people = new ArrayList<>();
  public Data myData;
  public Scanner scan;
  public String infoFile = "../DataBase/java.json";

  public void getInfo() {
    scan = new Scanner(System.in);
    System.out.println("Enter the amount of people you want to communicate with: >");
    String[] persons = scan.next().split(" ");
    int count = -1;

    for (String person : persons) {
      count++;
      people.add(count, person);
    }
  }

  public void start() {
    getInfo();
    appLoop();
  }

  public void appLoop() {
    scan = new Scanner(System.in);
    while (true) {
      System.out.println("Choose a person: ");
      String personInput = scan.nextLine();

      if (personInput.equals(".")) break;

      if (!people.contains(personInput)) {
        System.out.println("Invalid Option.");
        continue;
      }

      System.out.println("Type a message:\n>");
      String message = scan.nextLine();
      System.out.println(people.get(people.indexOf(personInput)) + ": " + message);
    }
  }

  public void saveInfo() {
    myData = new Data(infoFile);
    myData.setData(people.toString());
  }
}