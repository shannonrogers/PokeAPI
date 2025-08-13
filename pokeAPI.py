import requests
import json
import random

# def get_eevee():
#     url  = 'https://pokeapi.co/api/v2/pokemon/eevee'

#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         eevee = {
#         'name': data['name'],
#         'hp': data['stats'][0]['base_stat']
#         }
#         return eevee
#     else: 
#         print("failed to catch eevee")


def get_pokemon_data(pokemon_identifier):
    """
    Get Pokemon data from PokeAPI and extract game-relevant information
    
    Args:
        pokemon_identifier: Pokemon name (str) or ID (int)
    
    Returns:
        dict: Pokemon information with keys: name, id, hp, attack, sprite_url, type
        None: if Pokemon not found or error occurred
    """
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_identifier}'

    response = requests.get(url)

    if response.status_code == 200: 
        data = response.json()
        pokemon = {
            'name': data['name'],
            'pokemon_id': data['id'],
            'hp': data['stats'][0]['base_stat'],
            'attack': data['stats'][1]['base_stat'], 
            'sprite_url': data['sprites']['front_default'],
            'pokemon_type': data['types'][0]['type']['name']
        }
        return pokemon
    else: 
        print(f'failed to find {pokemon_identifier}')

    

class Pokemon: 

    def __init__(self, name, pokemon_id, hp, attack, sprite_url, pokemon_type):
        self.name = name.title()
        self.pokemon_id = pokemon_id
        self.hp = hp
        self.attack = attack
        self.sprite_url = sprite_url
        self.pokemon_type = pokemon_type

    def info(self):
        print(f"{self.name}")
        print(f"ID: {self.pokemon_id}")
        print(f"HP: {self.hp}")
        print(f"Attack: {self.attack}")
        print(f"Type: {self.pokemon_type}")
        print(f"Sprite URL: {self.sprite_url}")
        


class Player: 

    def __init__(self, name):
        self.name = name
        self.team = []
    
    def add_pokemon(self, pokemon): 

        if len(self.team) < 6: 
            self.team.append(pokemon)
            print(f"{pokemon.name} has been added to the team!")
            return
        else: 
            print("The team is full!  Remove a Pokemon to make space")
            return
    
    def view_team(self,): 
        if not self.team: 
            print("You currently have no Pokemon!")
        else: 
            count = 1
            for pokemon in self.team: 
                print(f"==========\n{count}.") 
                pokemon.info()
                count += 1
    
    def remove_pokemon(self, index): 
        if len(self.team) and index >= 0 and index < len(self.team):
            pokemon = self.team.pop(index)
            print(f"{pokemon.name} has been released!")
            return 
        else: 
            print('Invalid slot number')
            return
        
        

    
        
class PokemonGame: 
    def __init__(self): 
        self.player = None
        self.wild_pokemon = None

    def start_game(self): 
        print("Welcome to Pokemon CLI")
        name = input("What is your name? ").strip().title()
        self.player = Player(name)
        print(f"Let's go, {self.player.name}!")
        self.choose_starter()

    def go_hunting(self):
        num = random.randint(1, 1025)
        hunt = get_pokemon_data(num)
        wild_pokemon = Pokemon(**hunt)
        print(f"A wild {wild_pokemon.name} appeared!")
        print(wild_pokemon.info())
        
        catch = input(f"Would you like to try and catch {wild_pokemon.name}? ").lower().strip()
        if catch == 'yes':
            self.try_catch_pokemon(wild_pokemon)
        else: 
            print(f"{self.player.name} has run away")

    
    def try_catch_pokemon(self, pokemon): 
        chance = random.randint(0,100)
        if chance > 25: 
            self.player.add_pokemon(pokemon)
        else: 
            print(f"{pokemon.name} has escaped")
    
    
    def choose_starter(self):
        while True: 
            starters = ['torchic','turtwig','piplup']
            print("Choose your starting pokemon:")
            print("1. Torchic")
            print("2. Turtwig")
            print("3. Piplup")
            poke_name = input("Which do you choose? (enter name): ").lower().strip()

            if poke_name not in starters: 
                print("Please choose an option from the list")
                continue

            break

        poke_dict = get_pokemon_data(poke_name)
        pokemon = Pokemon(**poke_dict)
        self.player.add_pokemon(pokemon)
        self.main_game_loop()

    def main_game_loop(self):
        while True: 
            print("""
            =========Menu==========
            1. Go hunting (find wild Pokemon)
            2. View your collection
            3. Remove Pokemon from collection
            4. Quit Game
                """)
            choice = int(input("What would you like to do? (1-4): "))
            
            if choice < 1 or choice > 4: 
                print('Choice not valid, please choose from the list')
                continue
           
        
            match choice: 
                case 1: 
                    self.go_hunting()
                case 2: 
                    self.player.view_team()
                case 3: 
                    print("======Current Team=======")
                    self.player.view_team()
                    release = int(input(f"Choose which pokemon to release: (enter number): "))
                    self.player.remove_pokemon(release - 1)
                case 4:
                    print("Thanks for playing")
                    return
                

# print(charmander)
new_game = PokemonGame()
new_game.start_game()



        

