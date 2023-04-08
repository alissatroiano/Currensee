const express = require("express");
const app = express();  
const port = 3000;
const fs = require("fs");
const path = require("path");
const MindsDB = require("mindsdb-js-sdk").default;

const tradeDataHandler = require("./handlers/tradeDataHandler.js");
const forecastHandler = require("./handlers/forecastHandler.js");

commander
  .version("1.0.0", "-v, --version")
  .usage("[OPTIONS]...")
  .option(
    "-c, --config-path <value>",
    "path to config JSON file used for connecting to MindsDB.",
    "./config/mindsdb-config.json"
  )
  .option(
    "-m, --model-config-path <value>",
    "path to config JSON file used for mapping trained models to symbols.",
    "./config/model-config.json"
  )
  .parse(process.argv);

const options = commander.opts();

// Connect to MindsDB
const configPath = options.configPath;
const rawConfig = fs.readFileSync(configPath);
const config = JSON.parse(rawConfig);
MindsDB.connect({
  host: config.host,
  user: config.user,
  password: config.password,
})
  .then(() => {
    console.log("Successfully connected to MindsDB.");
  })
  .catch((error) => {
    console.log(
      `Something went wrong while connecting to MindsDB. Check that you have the right credentials in ${configPath}`
    );
    console.log(error);
    process.exit();
  });


app.use(express.static('public'));

app.get('/', function (req, res) {
    res.sendFile('index.html', { root: __dirname });
});

app.listen(port, () => {
    console.log(`Now listening on port ${port}`); 
});