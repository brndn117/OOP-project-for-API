from Creature import Creature
import Player

class Leviathan(Creature):
    def __init__(self, name, health, position,size):
        #leviathan is a large sea creature that is extremely hostile to the player
        super().__init__(name, health, position, aggression_level=10)
        self.size = size #an attribute unique to the leviathan


#Overriding the attack method from the Creature class to deal more damage than other hostile creatures
    def attack(self, player):
        print(f"Detecting multiple leviathan class lifeforms in the region. Are you certain whatever you're doing is worth it? {self.name} (Leviathan)")
        player.take_damage(50)


def __str__(self):
        return f"Leviathan: {self.name} with health {self.health} size {self.size}"



def main():
    leviathan_instance = Leviathan("Reaper", 100, [0,0], "Gigantic")
    player_instance = Player("MasterChief", 100, [0, 0], 100)
    print(leviathan_instance)
    leviathan_instance.attack("player")


if __name__ == "__main__":
    main()
