import time

class Player:
    def __init__(self, current_region):
        self.current_region = current_region
        self.inventory = []

    def move(self, direction):
        if direction not in self.current_region.exits:
            return "Invalid direction."
        else:
            next_region_id = self.current_region.exits[direction]
            next_region = next((r for r in world if r.id == next_region_id), None)
            if next_region:
                self.current_region = next_region
                return f"You have moved to {self.current_region.description}"
            else:
                return "Invalid region."

    def take_action(self, action):
        pass

class Region:
    def __init__(self, id, description, exits, is_shop=False):
        self.id = id
        self.description = description
        self.exits = exits
        self.is_shop = is_shop

    def display_info(self):
        print(self.description)
        if self.is_shop:
            print("This region is a shop.")
        print("Exits:", ", ".join(self.exits))

def initialize_game():
    global player, world
    world = []
    
    world.append(
        Region(
            0,
            "You are in Mondstadt",
            {'north': 1, 'south': 2},
            is_shop=True
        )
    )

    world.append(
        Region(
            1, "You are in Liyue", {'west': 0, 'south': 2},
            is_shop=False
        )
    )

    world.append(
        Region(
            2, "You are in Inazuma", {'north': 0, 'west': 1},
            is_shop=True
        )
    )

    player = Player(current_region=world[0])

initialize_game()

while True:
    player.current_region.display_info()
    player_input = input("Enter a direction to move (or 'q' to quit): ").lower()

    if player_input == 'q':
        print("Thanks for playing! Goodbye.")
        break
    else:
        print(player.move(player_input))
