const fs = require('fs')

const CHAT_FILE = "../chat.yaml"

function watch() {
  while (true) {
    fs.readFile(CHAT_FILE, "utf-8", (e,d) => {
      console.log(d)
    })
  }
}

watch()