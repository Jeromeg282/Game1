import time

region_array = []

#NoteK: Mr yang said to keep the room/region as a instance and not a class. Keep 1 region room template then create instances and dictionaries where you can go from each region.


class Player():
    def __init__(self):
        #input = input("You are in Teyvat. Where would you like to go [N], [E], [S], [W]")
        self.current_region = current_region
        self.inventory = []

    def move(self,direction):
        
        pass

    def take_action(self,action):

        pass

class Region():
    id = 0
    description = "You are in Monstadt."
    exits = ['w','e','s']

    def __init__(self, id, description, exits, is_shop = False):
        self.id = id
        self.description = description
        self.exits = exits
        self.is_shop = is_shop

    def display_reg(self):
        print(self.description)
        if self.is_shop:
            print("This region is a shop.")
        print("Exits:", ", ".join(self.exits))

def initialize_game():
    player = Player(current_region=world[0])

initialize_game()

class game_loop():
    while True:
        player_input = input ("Where would you like to go [n], [E], [W], [S]")

        if player_input == 'q':
            print("Thanks for playing! Goodbye.")
            break
        elif player_input in player.current_region.exits:
            player.move(player_input)
            player.current_region.display_info


world = []
world.append(
    Region(
        0,
        "You are in Monstadt",
        ['n','s']
        is_shop = True
    )
    
)

world.append(
    Region(
        1, "You are in Liyue", ['w' , 's'], 
        is_shop = False
    )
)

print( world[0].__dict__ )