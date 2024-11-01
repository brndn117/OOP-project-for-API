#The code for the Subnautica-inspired game models core gameplay elements using Object-Oriented Programming (OOP) principles. Key classes include Character, Player, Creature, and Leviathan, each with attributes and behaviors that define in-game entities and interactions


                          #BRANDON ADAM GIKANDI 164616


class Character:
    def __init__(self, name, health, position):
        self.name = name
        self.health = health
        self.position = position

#getters types of encapsulation
    def get_health(self):
            return self.health
        
    def get_position(self):
            return self.position
        
#setters types of encapsulation
    def set_health(self, health):
            if health > 0:
                self.health = health
            else:
                print("Health can never be negative")
        
    def set_position(self, position):
            self.position = position

#Example of a method in  this class
    def move(self, direction):
            if direction == "north":
                self.position[1] += 1
            elif direction == "south":
                self.position[1] -= 1
            elif direction == "east":
                self.position[0] += 1
            elif direction == "west":
                self.position[0] -= 1
            else:
                print("Invalid direction")
            
            return self.position
    
 # Method for taking damage
    def take_damage(self, amount):
        self.__health -= amount
        print(f"{self.name} took {amount} damage. Health: {self.__health}")
        if self.__health <= 0:
            self.die()
        
#Method for characters death
    def die(self):
            print(f"{self.name} has died")
            
    def __str__(self):
            return f"Character: {self.name} is at position {self.position} with health {self.health}"
        
