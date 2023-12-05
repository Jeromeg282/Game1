class Room:
    def __init__(self, name, description, directions):
        self.name = name
        self.description = description
        self.directions = directions

    def display_info(self):
        print(f"\n{self.name}")
        print(self.description)
        print("Directions available:", ", ".join(self.directions.keys()))


class Game:
    def __init__(self, start_room):
        self.current_room = start_room

    def play(self):
        while True:
            self.current_room.display_info()
            user_input = input("Enter a direction (or 'quit' to exit): ").lower()

            if user_input == 'quit':
                print("Thanks for playing! Goodbye.")
                break

            if user_input in self.current_room.directions:
                self.move(user_input)
            else:
                print("Invalid direction. Try again.")

    def move(self, direction):
        next_room = self.current_room.directions[direction]
        print(f"\nMoving {direction} to {next_room.name}")
        self.current_room = next_room


# Define rooms
# Define rooms
mondstadt = Room("Mondstadt", "The city of freedom, surrounded by mountains.", {"north": None, "south": liyue, "east": None, "west": None})
liyue = Room("Liyue", "The city of contracts, with vast landscapes and mountains.", {"north": mondstadt, "south": None, "east": None, "west": None})
inazuma = Room("Inazuma", "The nation of eternity, with a unique cultural atmosphere.", {"north": None, "south": liyue, "east": None, "west": None})
snezhnaya = Room("Snezhnaya", "The city of scholars, surrounded by icy plains.", {"north": None, "south": None, "east": None, "west": inazuma})


# Set initial room for the game
start_room = mondstadt

# Initialize the game
genshin_game = Game(start_room)

# Play the game
genshin_game.play()
