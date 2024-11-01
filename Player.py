#This class is inherits from Character class and represents a player-controlled character , plus the use of polymorphism



from Character import Character


class Player(Character):

    def __init__(self, name, health, position, oxygen,inventory, game):
        super().__init__(name, health, position)
        self.oxygen = oxygen #new attribute unique to the player
        self.inventory = inventory if inventory is not None else []#basically the inventory for the player

#Overriding the move method from the Character class to include oxygen consumption for the player
    def move(self, direction):
        #call the move method from the parent class
        new_position = super().move(direction)
        #consume oxygen when the player moves around
        self.use_oxygen(5)
        return new_position
    
# Method for taking damage
    def take_damage(self, amount):
        self.__health -= amount
        print(f"{self.name} took {amount} damage. Health: {self.__health}")
        if self.__health <= 0:
            self.die()

#This method shows how the oxygen is consumed by the player 
    def use_oxygen(self, amount):
        self.oxygen -= amount
        if self.oxygen <= 0:
            print(f"{self.name} has run out of oxygen ")
            self.die()  
        else:       
            print(f"{self.name} used {amount} oxygen and has {self.oxygen} remaining")


#This methods allows player to add items to their inventory
    def add_item(self, item):
        self.inventory.append(item)
        print(f"Added {item} to inventory")

#This method shows the items in the player's inventory
    def show_inventory(self):
        if not self.inventory:
           print(f"{self.name}'s inventory is empty")
        else:
            print(f"{self.name}'s inventory has {self.inventory}")

#Overriding die method from character class
    def die(self):
         print(f"{self.name} has died or suffocated")

#Overriding __str__ method from character class to include the inventory and oxygen level of the player
    def __str__(self):
        return f"Player: {self.name} is at position {self.position} with health {self.health}, oxygen {self.oxygen} and inventory {self.inventory}"

#Example of how to use the Player class
player = Player("MasterChief", 100, [0,0], 100, None, "Subnautica")
print(player)#prints player's current status

#Player moves around and oxygen is consumed
player.move("south")
print(player)

#add items to the player's inventory
player.add_item("scanner")
player.show_inventory()