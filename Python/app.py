from data import Data
import os

class App:
  def __init__(self):
    self.people = []
    self.json_data = Data("../DataBase/python.json")
    self.chat_data = Data("../chat.yaml")
    self.messages = []

  def getInfo(self):
    people = input("Enter the amount of people you want to communicate with:\n> ")
    persons = people.split(" ")
    self.people.extend(persons)

  def firstLoop(self):
    persons = self.json_data.getData()
    self.people.extend(persons)
    os.system("clear")
    while (True):
      person_input = input("Choose a person: ")
      
      if (person_input == "."): break

      if (person_input not in self.people):
        print("Invalid option.")
        continue;

      msg = input("Type a message:\n> ")
      message = f"{self.people[self.people.index(person_input)]}: {msg}"
      print(message)
      self.messages.append(message)
      self.chat_data.setChatData(self.messages)

  def secondLoop(self):
    self.getInfo()
    os.system("clear")
    while (True):
      person_input = input("Choose a person: ")
      
      if (person_input == "."): break

      if (person_input not in self.people):
        print("Invalid option.")
        continue;

      msg = input("Type a message:\n> ")
      message = f"{self.people[self.people.index(person_input)]}: {msg}"
      print(message)
      self.messages.append(message)

      for i in len(self.messages):
        self.messages[i].spilt(": ")
        
    self.chat_data.setChatData(self.messages)

  def appLoop(self):
    while (True):
      choice = input("Would you like to use the existing people or create new ones? (1/2):\n> ")
      if (choice == "1"):
        self.firstLoop()
        break
      if (choice == "2"):
        self.secondLoop()
        break
      if (choice != "1" or choice != "2"):
        print("Invalid choice")
        continue

  def saveInfo(self):
    self.json_data.setData(self.people)
    
  def start(self):
    self.appLoop()