import requests
import json

def get_pokemon_data(pokemon_identifier):
    """
    Get Pokemon data from PokeAPI and extract game-relevant information
    
    Args:
        pokemon_identifier: Pokemon name (str) or ID (int)
    
    Returns:
        dict: Pokemon information with keys: name, id, hp, attack, sprite_url, type
        None: if Pokemon not found or error occurred
    """

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_identifier}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        pokemon = {
        'name': data['name'],
        'pokemon_id': data['id'],
        'hp': data['stats'][0]['base_stat'],
        'attack': data['stats'][1]['base_stat'],
        'sprite_url': data['sprites']['other']['dream_world']['front_default'],
        'pokemon_type': data['types'][0]['type']['name']
        }
        return pokemon
    else:
        print(f"Failed to catch {pokemon_identifier}")
    

