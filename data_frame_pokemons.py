from typing import List

import pandas as pd
import requests


def get_pokemon_list(quantity: int) -> List[str]:
    """ " Get a list of pokemons by quantity"""
    quantity += 1
    pokemons = [
        requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}").json()
        for i in range(1, quantity)
    ]
    return pokemons


def create_pokemons_dataframe(pokemon_list: List[str]) -> pd.DataFrame:
    """ " Create a DataFrame with pokemons data"""
    items = {
        "name": [],
        "weight": [],
        "height": [],
        "type": [],
    }

    for _pokemon in pokemon_list:
        items["name"].append(_pokemon.get("name"))
        items["weight"].append(_pokemon.get("weight"))
        items["height"].append(_pokemon.get("height"))
        items["type"].append(_pokemon.get("types")[0].get("type").get("name"))

    df = pd.DataFrame(items)
    return df


def main():
    pokemon_list = get_pokemon_list(50)
    df = create_pokemons_dataframe(pokemon_list)
    print(df)


main()
