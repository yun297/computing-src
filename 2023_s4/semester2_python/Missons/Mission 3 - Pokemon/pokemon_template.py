# We are going to create a Pokemon game.
# a spell is a move that a pokemon can cast
# A Pokemon is a character with a name, hp, mp, atk, and type.
# A player is also a character with a name, hp, mp, and atk.
# A player can catch pokemons.
# If the player already has a pokemon of the same type, the player can choose to replace the old pokemon with the new one.
# Otherwise, the player can catch the new pokemon.
# Create a Pokemon class and a Player class which are subclasses of the Char class.


# Your code here

class Spell:
    def __init__(self, name, mp_cost, damage):
        self._name = name
        self._mp_cost = mp_cost
        self._damage = damage

    def __str__(self):
        return "Spell details: name: {}, mp_cost: {}, damage: {}.".format(self._name, self._mp_cost, self._damage)
    
    # Accessor methods
    
    def get_name(self):
        return self._name
    
    def get_mp_cost(self):
        return self._mp_cost
    
    def get_damage(self):
        return self._damage

class Character:
    def __init__(self, name, hp, mp, atk):
        self._name = name
        self._hp = hp
        self._mp = mp
        self._atk = atk
        self._alive = True
        
    def __str__(self) -> str:
        return "Name: {}, hp: {}, mp: {}, atk: {}.".format(self._name, self._hp, self._mp, self._atk)
        
    # Accessor methods
    
    def get_name(self):
        return self._name
    
    def get_hp(self):
        return self._hp
    
    def get_mp(self):
        return self._mp
    
    def get_atk(self):
        return self._atk

    # Mutator methods
    
    def update_hp(self, hp_change):
        self._hp = hp_change
    
    def update_mp(self, mp_change):
        self._mp = mp_change
        
    # Other methods
    
    def get_status(self):
        if self._hp <= 0:
            self._hp = 0
            return False
        else:
            return True
    
    def update_status(self):
        self._alive = self.get_status()
    
    def attack(self, target):
        if not target.get_status():
            print(">>> {} is already dead.".format(target.get_name()), end = "\n\n")
        elif target.get_status():
            target.update_hp(target.get_hp() - self._atk)
            print(">>> {} attacks {}. {} is hit, hp changes from {} to {}.".format(self._name, target.get_name(), target.get_name(), target.get_hp() + self._atk, target.get_hp()), end = "\n\n")
            target.update_status()
    
class Pokemon(Character):
    def __init__(self, name, hp, mp, atk, p_type, spell):
        super().__init__(name, hp, mp, atk)
        self._type = p_type
        self._spell = spell
        
    # Accessor methods
    
    def get_type(self):
        return self._type
    
    def get_spell(self):
        return self._spell
    
    # Mutator methods
    
    def set_spell(self, new_spell):
        self._spell = new_spell
        
    # Other methods
    
    def cast_spell(self, target):
        if not target.get_status():
            print(">>> {} is already dead.".format(target.get_name()), end = "\n\n")
        elif self._mp < self._spell.get_mp_cost():
            print(">>>{} costs {} mp, but {} only has {} mp, {} not casted.".format(self._spell.get_name(), self._spell.get_mp_cost(), self._name, self._mp, self._spell.get_name()), end = "\n\n")
        elif self._mp >= self._spell.get_mp_cost():
            print(">>> {} casts {} on {}. {} is hit, hp changes from {} to {}".format(self._name, self._spell.get_name(), target.get_name(), target.get_name(), target.get_hp(), target.get_hp() - self._spell.get_damage()), end = "\n\n")

class Player(Character):
    def __init__(self, name, hp, mp, atk, pokemons = None):
        super().__init__(name, hp, mp, atk)
        self._pokemons = pokemons if pokemons is not None else []
    
    # Accessor methods
    
    def get_pokemons(self):
        return self._pokemons
    
    def display_pokemons(self):
        if len(self._pokemons) == 0 or self._pokemons is None:
            output = "{} have not caught any pokemons yet.".format(self._name)
            print(f"+{'-' * (len(output) + 2)}+")
            print(f"| {output} |")
            print(f"+{'-' * (len(output) + 2)}+")
            print()
        else:
            output = "Here are the pokemons in {}'s team:".format(self._name)
            print(f"+{'-' * (len(output) + 2)}+")
            print(f"| {output} |")
            print(f"+{'-' * (len(output) + 2)}+")
            print()
            for pokemon in self._pokemons:
                print(self._pokemons.index(pokemon) + 1, end = ". ")
                print(pokemon)
            print()
    
    # Mutator methods
    
    def catch_pokemon(self, new_pokemon:Pokemon):
        if len(self._pokemons) == 0:
            self._pokemons.append(new_pokemon)
            print(">>> {} have caught {}.".format(self._name, new_pokemon.get_name()), end = "\n\n")
        else:
            for pokemon in self._pokemons:
                if pokemon.get_type() == new_pokemon.get_type():
                    output = "{}, you already have:".format(self._name)
                    print(f"+{'-' * (len(output) + 2)}+")
                    print(f"| {output} |")
                    print(f"+{'-' * (len(output) + 2)}+", end = "\n\n")
                    
                    print(pokemon)
                    print("Spell details: {}".format(pokemon.get_spell()), end = "\n\n")
                    
                    print("+---------------+")
                    print("| Now you meet: |")
                    print("+---------------+", end = "\n\n")
                    
                    print(new_pokemon)
                    print("Spell details: {}".format(new_pokemon.get_spell()), end = "\n\n")
                    
                    print(f"+{'-' * 63}+")
                    print("| Would you like to replace the pokemon of the same type? [Y/N] |")
                    print(f"+{'-' * 63}+", end = "\n\n")
                    choice = input().lower()
                    print()
                    
                    if choice == "y":
                        self._pokemons.remove(pokemon)
                        self._pokemons.append(new_pokemon)
                        print(">>> {} have released {}, and caught {}.".format(self._name, pokemon.get_name(), new_pokemon.get_name()), end = "\n\n")
                    elif choice == "n":
                        print(">>> {} chose not to catch {}".format(self._name, new_pokemon.get_name()), end = "\n\n")
                
                elif pokemon.get_type() != new_pokemon.get_type():
                    self._pokemons.append(new_pokemon)
                    print(">>> {} have caught {}.".format(self._name, new_pokemon.get_name()), end = "\n\n")
                break

# below are test functions and their expected outputs
# dmg spells (electric, fire, water)
fireball = Spell("Fireball", 12, 25)
fireblast = Spell("Fireblast", 15, 30)
thunderbolt = Spell("Thunderbolt", 10, 20)
frostbolt = Spell("Frostbolt", 8, 16)

# healing spells (grass)
heal = Spell("Heal", 10, -20)


def test_01():
    print("--- Test 01: test cataching different types of pokemons ---")
    player = Player("Ash Ketchum", 100, 100, 20)
    pokemon_01 = Pokemon("Charmander", 50, 60, 18, "Fire", fireball)
    pokemon_02 = Pokemon("Squirtle", 55, 60, 15, "Water", frostbolt)
    pokemon_03 = Pokemon("Bulbasaur", 80, 60, 12, "Grass", heal)
    pokemon_04 = Pokemon("Pikachu", 60, 60, 15, "Electric", thunderbolt)
    pokemon_05 = Pokemon("Ponyta", 60, 60, 18, "Fire", fireblast)

    print(player)

    player.display_pokemons()
    player.catch_pokemon(pokemon_01)
    player.catch_pokemon(pokemon_02)
    player.catch_pokemon(pokemon_03)
    player.catch_pokemon(pokemon_04)
    player.display_pokemons()
    player.catch_pokemon(pokemon_05)
    player.display_pokemons()

    print("--- End of Test 01 ---\n")


test_01()


def test_02():
    print("--- Test 02: test attacking between players and pokemons ---")

    # pokemons with various types and slightly different stats
    pikachu = Pokemon("Pikachu", 120, 100, 10, "Electric", thunderbolt)
    charmander = Pokemon("Charmander", 80, 120, 10, "Fire", fireball)
    squirtle = Pokemon("Squirtle", 100, 90, 10, "Water", frostbolt)
    bulbasaur = Pokemon("Bulbasaur", 120, 100, 10, "Grass", heal)

    # two players
    p1 = Player("Ash", 100, 100, 10)
    p2 = Player("Misty", 100, 100, 10)
    
    # display pokemon
    # p1.display_pokemons()
    # p2.display_pokemons()

    # p1 catches pikachu and charmander
    p1.catch_pokemon(pikachu)
    p1.catch_pokemon(charmander)
    p1.display_pokemons()

    # p2 catches squirtle and bulbasaur
    p2.catch_pokemon(squirtle)
    p2.catch_pokemon(bulbasaur)
    p2.display_pokemons()

    # player take turns to attack
    # player can attack
    # each pokemon can cast 1 spell

    # p1's turn
    p1.attack(p2)
    p1.get_pokemons()[0].cast_spell(p2.get_pokemons()[0])
    p1.get_pokemons()[1].cast_spell(p2.get_pokemons()[0])

    # p2's turn
    p2.attack(p1)
    p2.get_pokemons()[0].cast_spell(p1.get_pokemons()[0])
    p2.get_pokemons()[1].cast_spell(p2.get_pokemons()[0])  # heal

    # display status
    p1.display_pokemons()
    p2.display_pokemons()

    print("--- End of Test 02 ---\n")


test_02()


"""
--- Test 01: test cataching different types of pokemons ---
Name: Ash Ketchum, hp: 100, mp: 100, atk: 20.
Ash Ketchum, you have not caught any pokemons yet.

Ash Ketchum have caught Charmander.
Ash Ketchum have caught Squirtle.
Ash Ketchum have caught Bulbasaur.
Ash Ketchum have caught Pikachu.
Here are the pokemons in Ash Ketchum's team:
Name: Charmander, hp: 50, mp: 60, atk: 18. type: Fire.
Spell details: name: Fireball, mp_cost: 12, damage: 25.
Name: Squirtle, hp: 55, mp: 60, atk: 15. type: Water.
Spell details: name: Frostbolt, mp_cost: 8, damage: 16.
Name: Bulbasaur, hp: 80, mp: 60, atk: 12. type: Grass.
Spell details: name: Heal, mp_cost: 10, damage: -20.
Name: Pikachu, hp: 60, mp: 60, atk: 15. type: Electric.
Spell details: name: Thunderbolt, mp_cost: 10, damage: 20.

Ash Ketchum, you already have:
Name: Charmander, hp: 50, mp: 60, atk: 18. type: Fire.
Spell details: name: Fireball, mp_cost: 12, damage: 25.
Now you meet:
Name: Ponyta, hp: 60, mp: 60, atk: 18. type: Fire.
Spell details: name: Fireblast, mp_cost: 15, damage: 30.
Would you like to replace the pokemon of the same type? [Y/N]y
Ash Ketchum have released Charmander, and caught Ponyta.
Here are the pokemons in Ash Ketchum's team:
Name: Squirtle, hp: 55, mp: 60, atk: 15. type: Water.
Spell details: name: Frostbolt, mp_cost: 8, damage: 16.
Name: Bulbasaur, hp: 80, mp: 60, atk: 12. type: Grass.
Spell details: name: Heal, mp_cost: 10, damage: -20.
Name: Pikachu, hp: 60, mp: 60, atk: 15. type: Electric.
Spell details: name: Thunderbolt, mp_cost: 10, damage: 20.
Name: Ponyta, hp: 60, mp: 60, atk: 18. type: Fire.
Spell details: name: Fireblast, mp_cost: 15, damage: 30.

--- End of Test 01 ---

--- Test 02: test attacking between players and pokemons ---
Ash have caught Pikachu.
Ash have caught Charmander.
Here are the pokemons in Ash's team:
Name: Pikachu, hp: 120, mp: 100, atk: 10. type: Electric.
Spell details: name: Thunderbolt, mp_cost: 10, damage: 20.
Name: Charmander, hp: 80, mp: 120, atk: 10. type: Fire.
Spell details: name: Fireball, mp_cost: 12, damage: 25.

Misty have caught Squirtle.
Misty have caught Bulbasaur.
Here are the pokemons in Misty's team:
Name: Squirtle, hp: 100, mp: 90, atk: 10. type: Water.
Spell details: name: Frostbolt, mp_cost: 8, damage: 16.
Name: Bulbasaur, hp: 120, mp: 100, atk: 10. type: Grass.
Spell details: name: Heal, mp_cost: 10, damage: -20.

Ash attacks Misty.
Misty is hit, hp changes from 100 to 90.

Pikachu casts Thunderbolt on Squirtle.
Squirtle is hit, hp changes from 100 to 80.

Charmander casts Fireball on Squirtle.
Squirtle is hit, hp changes from 80 to 55.

Misty attacks Ash.
Ash is hit, hp changes from 100 to 90.

Squirtle casts Frostbolt on Pikachu.
Pikachu is hit, hp changes from 120 to 104.

Bulbasaur casts Heal on Squirtle.
Squirtle is hit, hp changes from 55 to 75.

Here are the pokemons in Ash's team:
Name: Pikachu, hp: 104, mp: 90, atk: 10. type: Electric.
Spell details: name: Thunderbolt, mp_cost: 10, damage: 20.
Name: Charmander, hp: 80, mp: 108, atk: 10. type: Fire.
Spell details: name: Fireball, mp_cost: 12, damage: 25.

Here are the pokemons in Misty's team:
Name: Squirtle, hp: 75, mp: 82, atk: 10. type: Water.
Spell details: name: Frostbolt, mp_cost: 8, damage: 16.
Name: Bulbasaur, hp: 120, mp: 90, atk: 10. type: Grass.
Spell details: name: Heal, mp_cost: 10, damage: -20.

--- End of Test 02 ---

"""
