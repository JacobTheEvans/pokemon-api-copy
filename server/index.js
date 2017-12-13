const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const mongoose = require("mongoose");
const settings = require("./config.js");
const pokemonRouter = require("./routes/pokemon.js");

mongoose.connect(`mongodb://localhost/${settings.db_name}`, {useMongoClient: true});
mongoose.Promise = global.Promise;

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: false}));
app.use(cors());

app.use("/api/pokemon", pokemonRouter);

let port = process.env.Port || settings.port;
app.listen(port, () => console.log(`Server started on ${port}`));
