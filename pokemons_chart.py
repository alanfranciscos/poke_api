import concurrent.futures
from typing import Dict, List

import matplotlib.pyplot as plt
import requests


def get_pokemon_type(pokemon_id):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    return response.json().get("types")[0].get("type").get("name")


def get_pokemon_type_list(quantity: int) -> List[str]:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        pokemons_types = list(
            executor.map(get_pokemon_type, range(1, quantity + 1))
        )
    return pokemons_types


def get_quantity_pokemon_by_type(pokemons: List[str]) -> Dict:
    pokemon_dict = {}
    for pokemon in pokemons:
        if pokemon in pokemon_dict:
            pokemon_dict[pokemon] += 1
        else:
            pokemon_dict[pokemon] = 1
    return pokemon_dict


def order_type_pokemon_to_chart(pokemon_dict: Dict, desc: bool) -> Dict:
    return dict(
        sorted(pokemon_dict.items(), key=lambda item: item[1], reverse=desc)
    )


def plot_bar_chart(pokemon_dict: Dict):
    fig, ax = plt.subplots()
    fig.set_figwidth(10)

    ax.set_title("Pokemons by type")
    ax.set_xlabel("Quantity")
    ax.set_ylabel("Type")
    ax.barh(list(pokemon_dict.keys()), list(pokemon_dict.values()))
    plt.show()


def main():
    pokemons_types = get_pokemon_type_list(100)
    pokemons_type_quantity = get_quantity_pokemon_by_type(pokemons_types)
    pokemon_type_sorted = order_type_pokemon_to_chart(
        pokemons_type_quantity, desc=True
    )
    plot_bar_chart(pokemon_type_sorted)


if __name__ == "__main__":
    main()
