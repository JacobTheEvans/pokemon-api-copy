const mongoose = require("mongoose");
const {Schema} = mongoose;

const pokemonSchema = new Schema({
  id: Number,
  _id: {
    select: false
  },
  stats: [
    {
      name: String,
      base_stat: String
    }
  ],
  name: String,
  weight: Number,
  base_experience: Number,
  height: Number,
  sprites: {
    back_female: String,
    back_shiny_female: String,
    back_default: String,
    front_female: String,
    front_shiny_female: String,
    back_shiny: String,
    front_default: String,
    front_shiny: String
  },
  types: [String]
}, {collection: "pokemon"});

module.exports = mongoose.model("pokemon", pokemonSchema);
