#This class represents a creature in the game subnautica

from Character import Character

class Creature(Character):
    def __init__(self, name, health, position, aggression_level):
            super().__init__(name, health, position)
            #Passive creatures dont have aggression level so its = 0 and hostile creatures are = 10
            self.aggression_level = aggression_level

#Overriding the move method from the Character class to include aggression level for the creature
    def move(self, new_position):
        #call the move method from the parent class
         super().move(new_position)
         if self.aggression_level > 5:
            print(f"{self.name} is attacking...")
         else:
            print(f"{self.name} is friendly...")

#This method shows how the creature attacks the player
    def attack(self, player):
        if self.aggression_level > 5:
            print(f"{self.name} is attacking")
            player.take_damage(10)
        else:
            print(f"{self.name} is friendly...")

    def __str__(self):
        return f"Creature: {self.name} is at position {self.position} with health {self.health} and aggression level {self.aggression_level}"
