const { App } = require("./app.js")

function main() {
  let app = new App();
  app.start();
  app.saveInfo();
}

main();