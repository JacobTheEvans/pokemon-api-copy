import sys
sys.dont_write_bytecode = True

import bot
import json
import db


def main():
    print("[+] Starting pokemon scraper bot")

    print("[+] Loading ./config.json file")
    with open("config.json") as json_data_file:
        config = json.load(json_data_file)
    print("[+] Success config loaded")

    driver = bot.web.gen_driver()
    raw_data = bot.pokemon.gather_base_pokemon(driver)
    data = bot.pokemon.gather_specific_pokemon_data(driver, raw_data, config["client_id"])

    print("[+] Connecting to db " + config["db_name"])
    db_connection = db.connect_to_db(config["db_name"])
    print("[+] Success connected to db")

    print("[+] Adding items to " + config["collection_name"])
    for item in data:
        db.insert_item(db_connection, config["collection_name"], item)
    print("[+] Success all items have been added")

    print("[+] Scraper bot complete")

if __name__ == "__main__":
    main()
