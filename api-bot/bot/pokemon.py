import images
import web
from time import sleep


base_url = "http://pokeapi.co/api/v2/pokemon/"


def gather_start_pokemon(driver):
    return web.base_req(driver, base_url)


def gather_base_pokemon(driver):
    print("[+] Gathering pokemon starting point from pokeAPI")
    starting_data = gather_start_pokemon(driver)
    print("[+] Success starting point gathered")

    count = starting_data["count"]
    next_point = starting_data["next"]
    data = starting_data["results"]

    print("[+] Gathering all pokemon")
    while len(data) < count:
        print("[+] Current count %s" % str(len(data)))
        next_data = web.base_req(driver, next_point)
        data += next_data["results"]
        next_point = next_point.replace("offset=" +  str(len(data) - 20),"offset=" + str(len(data)))
        sleep(1)

    print("[+] All pokemon gathered")
    return data


def format_data(raw_data, client_id):
    wanted_data = {};

    wanted_data["name"] = raw_data["name"]
    wanted_data["weight"] = raw_data["weight"]
    wanted_data["height"] = raw_data["height"]
    wanted_data["base_experience"] = raw_data["base_experience"]

    wanted_data["sprites"] = {}

    for key in raw_data["sprites"]:
        if raw_data["sprites"][key] is not None:
            wanted_data["sprites"][key] = images.handle_file(client_id, raw_data["sprites"][key], raw_data["name"] + key)
            sleep(0.8)

    types = []
    for type_pokemon in raw_data["types"]:
        types.append(type_pokemon["type"]["name"])

    wanted_data["types"] = types

    stats = []
    for raw_stat in raw_data["stats"]:
        stat = {}
        stat["name"] = raw_stat["stat"]["name"]
        stat["base_stat"] = raw_stat["base_stat"]
        stats.append(stat)
    wanted_data["stats"] = stats

    return wanted_data


def gather_specific_pokemon_data(driver, queue, client_id):
    print("[+] Gathering pokemon info from API")
    data = []

    for item in queue:
        print("[+] Gathering data for %s" % item["name"])
        pokemon_raw_data = web.base_req(driver, item["url"])
        print("[+] Success raw data has been gathered")

        print("[+] Formating data")
        pokemon_wanted_data = format_data(pokemon_raw_data, client_id)
        print("[+] Success data has been formated")

        data.append(pokemon_wanted_data)
        sleep(1)

    print("[+] Success all pokemon data collected")

    return data
