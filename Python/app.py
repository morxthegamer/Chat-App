from data import Data
import os
import json

class App:
  def __init__(self):
    self.people = []
    self.data = Data()

  def getInfo(self):
    people = input("Enter the amount of people you want to communicate with:\n> ")
    persons = people.split(" ")
    self.people.extend(persons)
    os.system("clear")

  def appLoop(self):
    while (True):
      person_input = input("Choose a person: ")
      
      if (person_input == "quit"): break

      if (person_input not in self.people):
        print("Invalid option.")
        continue;

      message = input("Type a message:\n> ")
      print(f"{self.people[self.people.index(person_input)]}: {message}")

  def saveInfo(self):
    self.data.setData(json.dumps(self.people))
    
  def start(self):
    self.getInfo()
    self.appLoop()