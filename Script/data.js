const fs = require('fs')

class Data {
  constructor(file) {
    this.file = file
  }

  getData() {
    fs.readFile(this.file, 'UTF-8', (e, d) => {
      return d;
    })
  }

  setData(data) {
    fs.writeFile(this.file, data, (err) => {
      if (err) return;
    })
  }
}

module.exports = { Data }