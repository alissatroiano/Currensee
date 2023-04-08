const express = require("express");
const path = require("path");

const app = express();
app.get('/', function (req, res) {
    res.send('GET request to homepage. Test')
  })

const port = 3000;
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
}
);
