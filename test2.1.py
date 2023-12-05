import time
import random

class Player:
    def __init__(self, current_region):
        self.current_region = current_region
        self.inventory = []
        self.money = 0

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
        if action.lower() == 'shop' and self.current_region.is_shop:
            enter_shop()
        elif action.lower() == 'gacha':
            gacha_menu()

    def fight_monster(self, monster):
        base_chance = monster['base_chance']
        if 'item_boost' in self.inventory:
            base_chance += self.inventory['item_boost']
        chance = min(base_chance, 100)  # Ensure chance does not exceed 100%
        result = random.random() * 100  # Generate a random percentage

        if result <= chance:
            self.money += monster['reward']
            return f"You defeated {monster['name']} and earned {monster['reward']} money!"
        else:
            return f"You were defeated by {monster['name']}. Better luck next time!"

    def fight_grass_plain_monster(self, monster):
        base_chance = monster['base_chance']
        if 'item_boost' in self.inventory:
            base_chance += self.inventory['item_boost']
        chance = min(base_chance, 100)  # Ensure chance does not exceed 100%
        result = random.random() * 100  # Generate a random percentage

        if result <= chance:
            self.money += monster['reward']
            return f"You defeated {monster['name']} and earned {monster['reward']} money!"
        else:
            return f"You were defeated by {monster['name']}. Better luck next time!"

class Region:
    def __init__(self, id, description, exits, is_shop=False, is_grass_plain=False, shop_items=None):
        self.id = id
        self.description = description
        self.exits = exits
        self.is_shop = is_shop
        self.is_grass_plain = is_grass_plain
        self.shop_items = shop_items or []

    def display_info(self):
        print(self.description)
        if self.is_shop:
            print("This region is a shop.")
            print("Type 'shop' to enter the shop.")
        elif self.is_grass_plain:
            print("You are in a grass plain. Be prepared for monster encounters!")
        print("Exits:", ", ".join(self.exits))

def initialize_game():
    global player, world
    world = []

    world.append(
        Region(
            0,
            "You are in Mondstadt",
            {'north': 1, 'south': 2},
            is_shop=True,
            shop_items=["Item Boost (+5% chance for monster encounters)", "Gacha Spin"]
        )
    )

    world.append(
        Region(
            1, "You are in a Grass Plain", {'south': 0},
            is_grass_plain=True
        )
    )

    world.append(
        Region(
            2, "You are in Liyue", {'north': 0, 'south': 4},
            is_shop=True,
            shop_items=["Health Potion", "Gacha Spin"]
        )
    )

    world.append(
        Region(
            3, "You are in a Grass Plain", {'west': 5},
            is_grass_plain=True
        )
    )

    world.append(
        Region(
            4, "You are in Inazuma", {'north': 2},
            is_shop=True,
            shop_items=["Attack Boost", "Gacha Spin"]
        )
    )

    world.append(
        Region(
            5, "You are in a Grass Plain", {'east': 3},
            is_grass_plain=True
        )
    )

    player = Player(current_region=world[0])

initialize_game()

def enter_shop():
    print("\nWelcome to the Shop!")
    print("Available Items:")
    for i, item in enumerate(player.current_region.shop_items, 1):
        print(f"{i}. {item}")

    choice = input("Enter the item number you want to buy (or 'exit' to leave the shop): ")
    if choice.lower() == 'exit':
        print("Exiting Shop.")
    elif choice.isdigit() and 1 <= int(choice) <= len(player.current_region.shop_items):
        buy_item(int(choice))
    else:
        print("Invalid choice. Try again.")

def buy_item(item_number):
    selected_item = player.current_region.shop_items[item_number - 1]
    if selected_item == "Item Boost (+5% chance for monster encounters)" and player.money >= 10:
        player.inventory.append('item_boost')
        player.money -= 10
        print("Item Boost purchased!")
    elif selected_item == "Gacha Spin" and player.money >= 20:
        gacha_menu()
        player.money -= 20
    elif selected_item == "Health Potion" and player.money >= 15:
        # Add logic for Health Potion effect if needed
        player.money -= 15
        print("Health Potion purchased!")
    elif selected_item == "Attack Boost" and player.money >= 25:
        # Add logic for Attack Boost effect if needed
        player.money -= 25
        print("Attack Boost purchased!")
    else:
        print("Not enough money to buy the selected item.")

def gacha_menu():
    print("\nWelcome to the Gacha!")
    print("1. Spin Gacha - 20 money")
    print("2. Exit Gacha")

    choice = input("Enter your choice (1-2): ")
    if choice == '1' and player.money >= 20:
        spin_gacha()
        player.money -= 20
    elif choice == '2':
        print("Exiting Gacha.")
    else:
        print("Invalid choice. Try again.")

def spin_gacha():
    characters = ["Character A", "Character B", "Character C"]
    items = ["Item X", "Item Y", "Item Z"]

    gacha_result = random.choice(characters + items)
    print(f"\nCongratulations! You obtained: {gacha_result}")

def generate_monster():
    monsters = [
        {'name': 'Weak Monster', 'base_chance': 30, 'reward': 10},
        {'name': 'Strong Monster', 'base_chance': 50, 'reward': 20},
        # Add more monsters as needed
    ]
    return random.choice(monsters)

while True:
    player.current_region.display_info()
    player_input = input("Enter a direction to move, 'shop' to enter the shop, 'gacha' to spin the gacha, or 'q' to quit: ").lower()

    if player_input == 'q':
        print("Thanks for playing! Goodbye.")
        break
    elif player_input == 'shop' and player.current_region.is_shop:
        enter_shop()
    elif player_input == 'gacha':
        player.take_action('gacha')
    elif player_input in player.current_region.exits:
        player.move(player_input)
        if player.current_region.is_grass_plain:
            monster = generate_monster()
            print(f"A wild {monster['name']} appears!")
            print(player.fight_grass_plain_monster(monster))
    else:
        print("Invalid input. Try again.")
