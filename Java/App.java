import java.util.*;

public class App {
  public ArrayList<String> people = new ArrayList<>();
  public Data jsonData = new Data("../../DataBase/java.json");
  public Data chatData = new Data("../../chat.yaml");
  public HashMap<String, String> messages = new HashMap<>();
  public int count = -1;
  public int msgCount = 0;
  public Scanner scan;

  public void getInfo() {
    scan = new Scanner(System.in);
    System.out.print("Enter the amount of people you want to communicate with:\n> ");
    String[] persons = scan.nextLine().split(" ");

    for (String person : persons) {
      count++;
      people.add(count, person);
    }
  }

  public void firstLoop() {
    scan = new Scanner(System.in);
    String[] data = jsonData.getData();
    for (String d : data) {
      count++;
      people.add(count, d);
    }
    while (true) {
      msgCount++;

      System.out.print("Enter a person:\n> ");
      String personInput = scan.nextLine();

      if (personInput.equals(".")) break;
      if (!people.contains(personInput)) {
        System.out.println("Invalid Input.");
        continue;
      }

      System.out.print("Type a message:\n> ");
      String message = scan.nextLine();
      String person = people.get(people.indexOf(personInput));
      System.out.println(person + ": " + message);

      messages.put(msgCount + person, message);
    }
  }

  public void secondLoop() {
    getInfo();
    scan = new Scanner(System.in);
    while (true) {
      System.out.print("Choose a person: ");
      String personInput = scan.nextLine();

      if (personInput.equals(".")) break;

      if (!people.contains(personInput)) {
        System.out.println("Invalid Option.");
        continue;
      }

      System.out.print("Type a message:\n> ");
      String message = scan.nextLine();
      String person = people.get(people.indexOf(personInput));
      System.out.println(person + ": " + message);
    }
  }

  public void appLoop() {
    scan = new Scanner(System.in);
    while (true) {
      System.out.print("Would you like to use the existing people or create new ones? (1/2):\n> ");
      String option = scan.nextLine();

      if (option.equals("1")) {
        firstLoop();
        break;
      }

      if (option.equals("2")) {
        secondLoop();
        break;
      }

      if (!option.equals("1") || !option.equals("2")) {
        System.out.println("Invalid choice.");
        continue;
      }
    }
  }

  public void start() {
    appLoop();
  }

  public void saveInfo() {
    jsonData.setData(people.toString());
  }
}