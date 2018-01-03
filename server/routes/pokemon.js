const {Router} = require("express");
const settings = require("../config.js");
const Pokemon = require("../models/pokemon.js");
const pokemonRouter = Router();

pokemonRouter.get("/", (req, res) => {
  Pokemon.find(req.query, "-_id", (error, pokemon) => {
    if (error) {
      res.status(500).send({message: "Error internal", error});
    } else {
      res.status(200).send({message: `Success, ${pokemon.length} pokemon retrieved`, pokemon});
    }
  });
});

pokemonRouter.get("/:search", (req, res) => {
  if (!isNaN(parseInt(req.params.search))) {
    Pokemon.findOne({
      "id": req.params.search
    }, "-_id", (error, pokemon) => {
      if (error) {
        res.status(500).send({message: "Error internal", error});
      } else if (pokemon === null) {
        res.status(404).send({message: `Pokemon with id of ${req.params.search} was not found`});
      } else {
        res.status(200).send({message: "Success, pokemon retrieved", pokemon});
      }
    });
  } else {
    Pokemon.findOne({
      name: req.params.search
    }, "-_id", (error, pokemon) => {
      if (error) {
        res.status(500).send({message: "Error internal", error});
      } else if (pokemon === null) {
        res.status(404).send({message: `Pokemon with name of ${req.params.search} was not found`});
      } else {
        res.status(200).send({message: "Success, pokemon retrieved", pokemon});
      }
    });
  }
});

pokemonRouter.get("/type/:name", (req, res) => {
  Pokemon.find({
    "types": req.params.name
  }, "-_id", (error, pokemon) => {
    if (error) {
      res.status(500).send({message: "Error internal", error});
    } else if (pokemon.length === 0) {
      res.status(404).send({message: `No pokemon with state of ${req.params.name} was found`});
    } else {
      res.status(200).send({message: `Success, ${pokemon.length} pokemon retrieved`, pokemon});
    }
  });
});

module.exports = pokemonRouter;
