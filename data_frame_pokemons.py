import concurrent.futures
from typing import List

import pandas as pd
import requests


def get_pokemon_info(pokemon_id):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    return response.json()


def get_pokemon_list(quantity: int) -> List[dict]:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        pokemon_list = list(
            executor.map(get_pokemon_info, range(1, quantity + 1))
        )
    return pokemon_list


def create_pokemons_dataframe(pokemon_list: List[dict]) -> pd.DataFrame:
    items = {
        "name": [],
        "weight": [],
        "height": [],
        "type": [],
    }

    for pokemon in pokemon_list:
        items["name"].append(pokemon.get("name"))
        items["weight"].append(pokemon.get("weight"))
        items["height"].append(pokemon.get("height"))
        items["type"].append(pokemon.get("types")[0].get("type").get("name"))

    df = pd.DataFrame(items)
    return df


def main():
    pokemon_list = get_pokemon_list(50)
    df = create_pokemons_dataframe(pokemon_list)
    print(df)


if __name__ == "__main__":
    main()
