import time
import random
#make inventory as list of id numbers
class GachaSystem:
    def __init__(self):
        self.banners = {
            "Monstadt": {"characters": {"CharacterA": 5, "ItemX": 95}},
            "Liyue": {"characters": {"CharacterB": 10, "ItemY": 90}},
            "Inazuma": {"characters": {"Yae Miko": 6, "Raiden Shogun": 5, "Yelan": 5}},
            "Fontaine": {"characters": {}},
            "Sumeru": {"characters": {"Nilou": 15, "Candace": 75, "Dendro Traveler": 10, "Nahida": 5, "YaoYao": 8, "Dori": 25, "Faruzan": 25}},
        }
        self.inventory = []

    def update_gacha_contents(self, region_description):
        self.current_banner = self.banners.get(region_description, {"characters": {}})

    def view_banner(self):
        print("\nCurrent Banner:")
        for character, rate in self.current_banner["characters"].items():
            print(f"{character}: {rate}%")

    def gacha_menu(self):
        print("\nGacha Menu:")
        print("1. View Banner")
        print("2. Spin Gacha")
        print("3. Exit to Shop")
        choice = input("Enter your choice: ")

        if choice == '1':
            self.view_banner()
        elif choice == '2':
            self.spin_gacha()
        elif choice == '3':
            print("Returning to the shop.")
        else:
            print("\033[1;31mInvalid choice. Please try again.\033[0m")

    def spin_gacha(self):
        if not self.current_banner["characters"]:
            print("No characters available in the current banner.")
            return

        input("Press Enter to spin the gacha...")

        character = self.roll_item(self.current_banner["characters"])
        self.inventory.append(character)
        print("\033[1;32mCongratulations! You got {}\033[0m".format(character))

    def roll_item(self, gacha_pool):
        total_percentage = sum(gacha_pool.values())
        roll = random.randint(1, total_percentage)

        cumulative_percentage = 0
        for item, percentage in gacha_pool.items():
            cumulative_percentage += percentage
            if roll <= cumulative_percentage:
                return item

        # in case
        return random.choice(list(gacha_pool.keys()))


class Player:
    def __init__(self, current_region):
        self.current_region = current_region
        self.inventory = []
        self.money = 0  # Navigation game money
        self.encountered_monsters = []
        self.gacha_system = GachaSystem()

    def move(self, direction):
        if direction not in self.current_region.exits:
            return "\033[1;31mInvalid region.\033[0m"
        else:
            next_region_id = self.current_region.exits[direction]
            next_region = next((r for r in world if r.id == next_region_id), None)
            if next_region:
                self.current_region = next_region
                self.gacha_system.update_gacha_contents(self.current_region.description)
                return f"You have moved to {self.current_region.description}"
            else:
                return "\033[1;31mInvalid region.\033[0m"

    def take_action(self, action):
        if action.lower() == 'shop' and self.current_region.is_shop:
            enter_shop()
        elif action.lower() == 'gacha' and not self.current_region.is_shop:
            self.gacha_system.gacha_menu()
        else:
            print("\033[1;31mInvalid choice. Please try again.\033[0m")

    def spin_gacha(self):
        self.gacha_system.spin_gacha()
        self.money -= 20  # Deduct money

    def fight_monster(self, monster):
        base_chance = monster['base_chance']
        if 'item_boost' in self.inventory:
            base_chance += self.inventory['item_boost']
        chance = min(base_chance, 100)
        result = random.random() * 100  # random

        if result <= chance:
            self.money += monster['reward']
            return f"\033[1;32mYou defeated {monster['name']} and earned {monster['reward']} money!\033[0m"
        else:
            return f"\033[1;32mYou were defeated by {monster['name']}. Better luck next time!\033[0m"

    def fight_grass_plain_monster(self, monster):
        base_chance = monster['base_chance']
        if 'item_boost' in self.inventory:
            base_chance += self.inventory['item_boost']
        chance = min(base_chance, 100)
        result = random.random() * 100

        if result <= chance:
            self.money += monster['reward']
            self.encountered_monsters.append(monster)
            return f"\033[1;32mYou defeated {monster['name']} and earned {monster['reward']} money!\033[0m"
        else:
            return f"\033[1;32mYou were defeated by {monster['name']}. Better luck next time!\033[0m"

def check_inventory():
    print("\nInventory:")
    print(f"Money (Navigation Game): {player.money}")
    print(f"Money (Gacha System): {player.gacha_system.inventory}")
    print("---------------------")
    if player.inventory:
        print("Items:")
        for item in player.inventory:
            print(f"- {item}")
    else:
        print("No items in inventory.")
    print("---------------------")


class Region:
    def __init__(self, id, description, exits, is_shop=False, is_grass_plain=False, shop_items=None, gacha_items=None):
        self.id = id
        self.description = description
        self.exits = exits
        self.is_shop = is_shop
        self.is_grass_plain = is_grass_plain
        self.shop_items = shop_items or []
        self.gacha_items = gacha_items or []

    def display_info(self):
        print("\033[1;32m---------------------\033[0m")  # Green color
        print("\033[1;34m" + self.description + "\033[0m")  # Blue color
        if self.is_shop:
            print("\033[1;33mThis region is a shop.\033[0m")  # Yellow color
            print("\033[1;33mType 'shop' to enter the shop.\033[0m")
        elif self.is_grass_plain:
            print("\033[1;31mYou are in a grass plain. Be prepared for monster encounters!\033[0m")  # Red 
        print("\033[1;32m---------------------\033[0m")  # Green
        print("\033[1;37mExits:", ", ".join(self.exits), "\033[0m")  # White
        print("\033[1;32m---------------------\033[0m")  # Green

def initialize_game():
    global player, world
    world = []

    world.append(
        Region(
            0,
            "You are in Mondstadt. (west:Ruins, south:Plains)",
            {'west': 1, 'south': 2},
            is_shop=True,
            shop_items=["Item Boost (+5% chance for monster encounters)", "Gacha Spin"]
        )
    )
    world.append(
        Region(
            1,
            "You are in a Ruin. (east: Monstadt, south: Plains)",
            {'east': 0, 'south': 3},
            is_shop=True,
            shop_items=["Item Boost (+5% chance for monster encounters)", "Gacha Spin"]
        )
    )
    world.append(
        Region(
            2, "You are in Grass Plains (north: Monstadt, west: Plains, south: Dragonspine)",
             {'north':0, 'west' : 3, 'south': 5},
            is_grass_plain=True
        )
    )

    world.append(
        Region(
            3,
            "You are in Plains (north: Ruin, east: Plains, south: Liyue)",
            {'north': 1, 'east': 2, 'south': 4},
            is_grass_plain=True
        )
    )

    world.append(
        Region(
            4, "You are in Liyue. (north:Plains, south:Water, west:Plains, east:Dragonspine)", 
            {'north': 3, 'east': 5, 'west': 6, 'south': 13},
            is_shop=True,
            shop_items=["Health Potion", "Gacha Spin"],
            gacha_items=["Character A", "Item X"]
        )
    )
    world.append(
        Region(
            5, "You are in Dragonspine. (north:Plains, south:Water, west:Liyue)",
            {'north': 2, 'west': 4, 'south': 11 },
            is_shop=False,
            shop_items=["Health Potion", "Gacha Spin"],
            gacha_items=["Character A", "Item X"]
        )
    )

    world.append(
        Region(
            6,
            "You are in Grass Plains (west:Sumeru, east:Liyue)",
            {'west': 7, 'east': 4},
            is_grass_plain=True
        )
    )
    world.append(
        Region(
            7, "You are in Sumeru. (west:Desert, east:Grass plains)",
            {'west': 8, 'east': 6},
            is_shop=True,
            shop_items=["Health Potion", "Gacha Spin"],
            gacha_items=["Character A", "Item X"]
        )
    )
    world.append(
        Region(
            8,
            "You are in Desert. (east: Sumeru, North: Water)",
            {'north': 9, 'east': 7, },
            is_grass_plain=True
        )
    )

    world.append(
        Region(
            9,
            "You are in the Water. (north: Fontaine, south: Desert)",
            {'north': 10, 'south': 8},
            is_grass_plain=False
        )
    )
    world.append(
        Region(
            10, "You are in Fontaine. (south:Water)", 
            {'south': 9},
            is_shop=True,
            shop_items=["Health Potion", "Gacha Spin"],
            gacha_items=["Character A", "Item X"]
        )
    )
    
    world.append(
        Region(
            11,
            "You are in the water. (north:Dragonspine, west:water, south:Inazuma)",
            {'north': 5, 'west': 13, 'south': 12},
            is_grass_plain=False
        )
    )
    world.append(
        Region(
            12, "You are in Inazuma. (North:Water)", 
            {'north': 11},
            is_shop=True,
            shop_items=["Health Potion", "Gacha Spin"],
            gacha_items=["Character A", "Item X"]
        )
    )
    world.append(
        Region(
            13,
            "You are in the Water. (south:Water, north:Liyue, east:Water)",
            {'north': 4, 'east': 11, 'south': 14},
            is_grass_plain=False
        )
    )

    world.append(
        Region(
            14,
            "You are in the Water. (north: Water, east: Inazuma)",
            {'north': 13, 'east': 12},
            is_grass_plain=False
        )
    )



    player = Player(current_region=world[0])





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
        player.inventory.append('Health Potion')
        player.money -= 15
        print("Health Potion purchased!")
    else:
        print("Not enough money to buy the selected item.")

def gacha_menu():
    print("\nWelcome to the Gacha!")
    print("Available Items:")
    for i, item in enumerate(player.current_region.gacha_items, 1):
        print(f"{i}. {item}")

    choice = input("Enter the item number you want to obtain (or 'exit' to leave the gacha): ")
    if choice.lower() == 'exit':
        print("Exiting Gacha.")
    elif choice.isdigit() and 1 <= int(choice) <= len(player.current_region.gacha_items):
        obtain_item(int(choice))
    else:
        print("Invalid choice. Try again.")

def obtain_item(item_number):
    selected_item = player.current_region.gacha_items[item_number - 1]
    player.gacha_contents.append(selected_item)
    print(f"You obtained: {selected_item}")


def generate_monster():
    monsters = [
        {'name': 'Weak Monster', 'base_chance': 30, 'reward': 10},
        {'name': 'Strong Monster', 'base_chance': 50, 'reward': 20},
        # Add
    ]
    return random.choice(monsters)

initialize_game()

while True:
    player.current_region.display_info()
    player_input = input("Enter a direction to move, 'shop' to enter the shop, 'gacha' to spin the gacha, 'inventory' to check your inventory, or 'q' to quit: ").lower()

    if player_input == 'q':
        print("Thanks for playing! Goodbye.")
        break
    elif player_input == 'shop' and player.current_region.is_shop:
        enter_shop()
    elif player_input == 'gacha':
        player.spin_gacha()
    elif player_input == 'inventory':
        check_inventory()
    elif player_input in player.current_region.exits:
        player.move(player_input)
        if player.current_region.is_grass_plain:
            monster = generate_monster()
            print(f"A wild {monster['name']} appears!")
            print(player.fight_grass_plain_monster(monster))
    else:
        print("\033[1;31mInvalid input. Try again.\033[0m")