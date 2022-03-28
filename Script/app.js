const prompt = require("prompt-sync")();
const { Data } = require("./data.js")

class App {
  constructor() {
    this.people = []
    this.jsonData = new Data("../DataBase/python.json");
    this.chatData = new Data("../chat.yaml");
    this.messages = {}
    this.count = 0;
  }

  getInfo() {
    let people = prompt("Enter the amount of people you want to communicate with:\n> ")
    let persons = people.split(" ")
    for (let person of persons) {
      this.people.push(person)
    }
  }

  firstLoop() {
    let persons = this.jsonData.getData();
    for (let person of persons) {
      this.people.push(person)
    }

    while (true) {
      this.count++;
      let personInput = prompt("Choose a person: ")

      if (personInput === ".") break;

      if (!this.people.includes(personInput)) {
        console.log("Invalid Option.")
        continue;
      }

      let message = prompt("Type a message:\n> ")
      let person = this.people[this.people.indexOf(personInput)]
      console.log(`${person}: ${message}`)
    }
  }

  secondLoop() {
    this.getInfo();

    while (true) {
      this.count++;
      let personInput = prompt("Choose a person: ")

      if (personInput === ".") break;

      if (!this.people.includes(personInput)) {
        console.log("Invalid Option.")
        continue;
      }

      let message = prompt("Type a message:\n> ")
      let person = this.people[this.people.indexOf(personInput)]
      console.log(`${person}: ${message}`)
    }
  }

  saveInfo() {
    this.jsonData.setData(this.people)
  }

  appLoop() {
    while (true) {
      let choice = prompt("Would you like to use the existing people or create new ones? (1/2):\n> ")

      if (choice === '1') {
        this.firstLoop();
        break;
      }

      if (choice === '2') {
        this.secondLoop();
        break;
      }

      if (!choice === '1' || !choice === '2') {
        console.log("Invalid choice.")
        continue;
      }
    }
  }
  
  start() {
    this.appLoop();
  }
}

module.exports = { App }