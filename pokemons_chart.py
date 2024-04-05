from typing import Dict, List

import matplotlib.pyplot as plt
import pokebase as pb


def get_pokemon_type_list(quantity: int) -> List[str]:
    """Get a list of pokemons type by quantity"""
    quantity += 1
    pokemons = []
    for i in range(1, quantity):
        pokemons.append(pb.pokemon(i).types[0].type.name)
    return pokemons


def get_quantity_pokemon_by_type(pokemons: List[str]) -> Dict:
    """Get the quantity of pokemons by type"""
    pokemon_dict = {}
    for pokemon in pokemons:
        if pokemon in pokemon_dict.keys():
            pokemon_dict[pokemon] += 1
        else:
            pokemon_dict[pokemon] = 1
    return pokemon_dict


def order_type_pokemon_to_chart(pokemon_dict: Dict, desc: bool) -> Dict:
    """Order the pokemons by type"""
    return dict(
        sorted(
            pokemon_dict.items(),
            key=lambda item: item[1],
            reverse=desc,
        )
    )


def plot_bar_chart(pokemon_dict: Dict):
    """Plot a bar chart with the pokemons by type"""
    fig, ax = plt.subplots()
    fig.set_figwidth(10)

    ax.set_title("Pokemons by type")
    ax.set_xlabel("Quantity")
    ax.set_ylabel("Type")
    ax.barh(list(pokemon_dict.keys()), list(pokemon_dict.values()))
    plt.show()


def main():
    pokemons = get_pokemon_type_list(100)

    pokemons_type = get_quantity_pokemon_by_type(pokemons)
    pokemon_type_sorted = order_type_pokemon_to_chart(
        pokemon_dict=pokemons_type, desc=True
    )
    plot_bar_chart(pokemon_type_sorted)


main()
