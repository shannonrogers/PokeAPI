import requests
from inclass import get_pokemon_data


class Pokemon:
    """ Represent a simple Pokemon object, instead of just a dictionary"""

    def __init__(self, name, pokemon_id, hp, attack, sprite_url, pokemon_type): #Storing all of my pokemon info when constructing this poke
        self.name = name.title() 
        self.pokemon_id = pokemon_id
        self.hp = hp
        self.attack = attack
        self.sprite_url = sprite_url
        self.pokemon_type = pokemon_type

    def info(self):
        print(f"==========={self.name}'s Info===========")
        print(f"ID: {self.pokemon_id}")
        print(f"Stats: HP- {self.hp} Attack- {self.attack}")
        print(f"Type: {self.pokemon_type}")
        print(f"Sprite: {self.sprite_url}")


class Player:

    def __init__(self, name):
        self.name = name
        self.team = [] #List of pokemon objects No more than 6 at a time

    
    def add_pokemon(self, pokemon):
        """Takes in a pokemon object, and adds it to the team if there is room"""

        if len(self.team) < 6:
            self.team.append(pokemon)
            print(f"{pokemon.name} has been added to the team!")
            return 
        else:
            print("The team is full, remove a pokemon to make space.")
            return

    



charmander = get_pokemon_data('charmander')
print(charmander)

object_charmander = Pokemon(**charmander)
object_charmander.info()

new_player = Player('Ash')
