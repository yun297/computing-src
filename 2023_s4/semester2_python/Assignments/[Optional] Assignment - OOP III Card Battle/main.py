# Question 1: Card Battle

class Card:
    def __init__(self, name, cost) -> None:
        self._name = name
        self._cost = cost

class MinionCard(Card):
    def __init__(self, name, cost, atk, hp, alive) -> None:
        super().__init__(name, cost)
        self._atk = atk
        self._hp = hp
        self._alive = alive
    
    def action(self, target):
        if not isinstance(target, MinionCard):
            raise ValueError("Target must be a MinionCard instance.")
        
        if self._alive and target._alive:
            target.take_damage(self._atk)

    def take_damage(self, damage_points):
        if self._alive:
            self._hp -= damage_points
            
            if self._hp <= 0:
                self._hp = 0
                self._alive = False
                output = f"{self._name} has been defeated!"
                print("# " + "-"*(len(output)) + " #")
                print(f"| {output} |")
                print("# " + "-"*(len(output)) + " #")
                print()
            else:
                output = f"{self._name} has {self._hp} HP remaining."
                print("# " + "-"*(len(output)) + " #")
                print(f"| {output} |")
                print("# " + "-"*(len(output)) + " #")
                print()

class SpellCard(Card):
    def __init__(self, name, cost, damage, used) -> None:
        super().__init__(name, cost)
        self._damage = damage
        self._used = used
        
    def action(self, target):
        if not isinstance(target, MinionCard):
            raise ValueError("Target must be a MinionCard instance.")
        
        if not self._used:
            target.take_damage(self._damage)
            self._used = True
            output = f"{self._name} used. {target._name} has {target._hp} HP remaining."
            print("# " + "-"*(len(output)) + " #")
            print(f"| {output} |")
            print("# " + "-"*(len(output)) + " #")
            print()
        else:
            output = "This spell card has already been used."
            print("# " + "-"*(len(output)) + " #")
            print(f"| {output} |")
            print("# " + "-"*(len(output)) + " #")
            print()
            
###############################
# Create MinionCard instances #
###############################

minion1 = MinionCard("Goblin", 3, 2, 3, True)
minion2 = MinionCard("Orc", 4, 4, 5, True)

###################################
# Test Case 1: Minion Card Attack #
###################################

print("###################################")
print("# Test Case 1: Minion Card Attack #")
print("###################################")
print()

# Perform an attack action
minion1.action(minion2) 

# Print the HP of both minions
print("#" + "-"*50 + "#")
print(f"{minion1._name} HP: {minion1._hp}")
print(f"{minion2._name} HP: {minion2._hp}")
print("#" + "-"*50 + "#")
print()

#--------------------------------------------------------------------------------------------------------------#
# Expected outcome:
# minion2 should take damage equal to minion1's attack (minion2's HP should be 5-2=3).
# Both minions should still be alive.
#--------------------------------------------------------------------------------------------------------------#

###################################
# Test Case 2: Minion Card Defeat #
###################################

print("###################################")
print("# Test Case 2: Minion Card Defeat #")
print("###################################")
print()

# Create a MinionCard instance with 1 HP
minion1 = MinionCard("Weakened Minion", 2, 1, 1, True)

# Perform an attack action on the same minion 
minion1.action(minion1)

#--------------------------------------------------------------------------------------------------------------#
# Expected outcome:
# minion1 should take damage equal to its own attack (minion1's HP should be 1-1=0).
# The minion should be defeated (alive=False).
#--------------------------------------------------------------------------------------------------------------#

##################################
# Test Case 3: Spell Card Attack #
##################################

print("##################################")
print("# Test Case 3: Spell Card Attack #")
print("##################################")
print()

# Create a MinionCard instance and a SpellCard instance
minion = MinionCard("Beast", 5, 3, 7, True)
spell = SpellCard("Fireball", 4, 4, False)

# Use the spell card against the minion
spell.action(minion)

#--------------------------------------------------------------------------------------------------------------#
# Expected outcome:
# minion should take damage equal to the spell's damage (minion's HP should be 7-4=3).
# The spell card should be marked as used (used=True).
#--------------------------------------------------------------------------------------------------------------#

########################################
# Test Case 4: Spell Card Already Used #
########################################

print("########################################")
print("# Test Case 4: Spell Card Already Used #")
print("########################################")
print()

# Create a MinionCard instance and a used SpellCard instance
minion = MinionCard("Guard", 3, 2, 4, True)
used_spell = SpellCard("Lightning Bolt", 2, 5, True)

# Try to use the used spell card on the minion again
used_spell.action(minion)

#--------------------------------------------------------------------------------------------------------------#
# Expected outcome:
# The spell card should print "This spell card has already been used."
# The minion's HP should remain unchanged (4).
#--------------------------------------------------------------------------------------------------------------#

##############################################
# Test Case 5: Invalid Target for Spell Card #
##############################################

print("##############################################")
print("# Test Case 5: Invalid Target for Spell Card #")
print("##############################################")
print()

# Create a SpellCard instance and a non-MinionCard instance
spell = SpellCard("Magic Missile", 3, 2, False)
non_minion = Card("Random Card", 0)

# Try to use the spell card on the non-MinionCard instance
spell.action(non_minion)

#--------------------------------------------------------------------------------------------------------------#
# Expected outcome:
# The spell card should raise a ValueError with the message "Target must be a MinionCard instance."
#--------------------------------------------------------------------------------------------------------------#