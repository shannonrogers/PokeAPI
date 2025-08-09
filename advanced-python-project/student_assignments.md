# Lesson 8: Pokemon CLI Game - In-Class Assignments

---

## Assignment 1: Pokemon Data Extractor

### Task
Create a function that can extract Pokemon information needed for our game.

### Requirements
```python
import requests

def get_pokemon_data(pokemon_identifier):
    """
    Get Pokemon data from PokeAPI and extract game-relevant information
    
    Args:
        pokemon_identifier: Pokemon name (str) or ID (int)
    
    Returns:
        dict: Pokemon information with keys: name, id, hp, attack, sprite_url, type
        None: if Pokemon not found or error occurred
    """
    
    # YOUR CODE HERE
    # 1. Make a GET request to https://pokeapi.co/api/v2/pokemon/{pokemon_identifier}
    # 2. Check if the request was successful (status code 200)
    # 3. Parse the JSON response
    # 4. Extract: name, id, hp stat, attack stat, front_default sprite, primary type
    # 5. Return as a dictionary
    # 6. Handle errors gracefully (return None if something goes wrong)
    
    pass

# Test your function with these Pokemon
test_pokemon = ["bulbasaur", "charmander", "squirtle", 25, "pikachu"]

for pokemon in test_pokemon:
    print(f"\n--- Testing {pokemon} ---")
    data = get_pokemon_data(pokemon)
    if data:
        print(f"Found: {data['name']} (ID: {data['id']})")
        print(f"   HP: {data['hp']}, Attack: {data['attack']}")
        print(f"   Type: {data['type']}")
        print(f"   Sprite: {data['sprite_url']}")
    else:
        print(f"Failed to get data for {pokemon}")
```

### Expected Output:
```
--- Testing bulbasaur ---
Found: Bulbasaur (ID: 1)
   HP: 45, Attack: 49
   Type: grass
   Sprite: https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png
```

---

## Assignment 2: Complete the remove_pokemon Method

### Task
Complete the `remove_pokemon` method in the Player class to allow removing Pokemon from the collection.

### Requirements
```python
def remove_pokemon(self, index):
    """Remove a Pokemon from the collection by index"""
    # YOUR CODE HERE
    # 1. Check if the index is valid (between 0 and 5, and less than collection size)
    # 2. If valid, remove the Pokemon at that index using pop()
    # 3. Print a message about releasing the Pokemon
    # 4. Return the removed Pokemon
    # 5. If invalid index, return None
    pass
```

### Test Your Implementation
```python
def test_remove_pokemon():
    """Test the remove_pokemon functionality"""
    player = Player("Ash")
    
    # Add some Pokemon
    pikachu = Pokemon("Pikachu", 25, 90, 55, "url", "electric")
    charizard = Pokemon("Charizard", 6, 158, 84, "url", "fire")
    bulbasaur = Pokemon("Bulbasaur", 1, 45, 49, "url", "grass")
    squirtle = Pokemon("Squirtle", 7, 44, 48, "url", "water")
    
    player.add_pokemon(pikachu)
    player.add_pokemon(charizard)
    player.add_pokemon(bulbasaur)
    player.add_pokemon(squirtle)
    
    print("Initial collection:")
    player.show_collection()
    
    # Test removing Pokemon
    print("\n--- Testing remove_pokemon ---")
    
    # Remove the second Pokemon (index 1)
    removed = player.remove_pokemon(1)
    if removed:
        print(f"Successfully removed: {removed.name}")
    else:
        print("Failed to remove Pokemon")
    
    print("\nCollection after removal:")
    player.show_collection()
    
    # Test invalid index
    print("\n--- Testing invalid index ---")
    invalid_removed = player.remove_pokemon(10)
    if invalid_removed is None:
        print("Correctly handled invalid index")

# Run the test
test_remove_pokemon()
```

### Expected Output:
```
Initial collection:

Ash's Pokemon Collection:
   1. Pikachu (ID: 25) - electric type
   2. Charizard (ID: 6) - fire type
   3. Bulbasaur (ID: 1) - grass type
   4. Squirtle (ID: 7) - water type

--- Testing remove_pokemon ---
Released Charizard from the collection.
Successfully removed: Charizard

Collection after removal:

Ash's Pokemon Collection:
   1. Pikachu (ID: 25) - electric type
   2. Bulbasaur (ID: 1) - grass type
   3. Squirtle (ID: 7) - water type

--- Testing invalid index ---
Correctly handled invalid index
```

### Hints:
- Remember that list indices start at 0
- The collection can have a maximum of 6 Pokemon
- Check that the index is between 0 and 5, AND less than the current collection size
- Use the `pop(index)` method to remove and return an item from a list
- Don't forget to handle the case where the index is invalid

---

## Required Classes for Reference

### Pokemon Class
```python
class Pokemon:
    """Represents a Pokemon with basic stats"""
    
    def __init__(self, name, pokemon_id, hp, attack, sprite_url, pokemon_type):
        self.name = name
        self.id = pokemon_id
        self.hp = hp
        self.attack = attack
        self.sprite_url = sprite_url
        self.type = pokemon_type
    
    def info(self):
        """Print the Pokemon's information"""
        print(f"{self.name} (ID: {self.id})")
        print(f"   HP: {self.hp}")
        print(f"   Attack: {self.attack}")
        print(f"   Type: {self.type}")
        print(f"   Sprite: {self.sprite_url}")
```

### Player Class (Partial)
```python
class Player:
    """Represents a player with a collection of Pokemon"""
    
    def __init__(self, name):
        self.name = name
        self.collection = []  # List of Pokemon objects
    
    def add_pokemon(self, pokemon):
        """Add a Pokemon to the collection (max 6 Pokemon)"""
        if len(self.collection) < 6:
            self.collection.append(pokemon)
            print(f"{pokemon.name} added to {self.name}'s collection!")
            return True
        else:
            print(f"Collection is full! Can't add {pokemon.name}")
            return False
    
    def remove_pokemon(self, index):
        """Remove a Pokemon from the collection by index"""
        # YOUR CODE HERE - Complete this method
        pass
    
```

---

