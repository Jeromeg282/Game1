
class Player():
    def __init__(self):
        input = input("You are in Teyvat. Where would you like to go [N], [E], [S], [W]")

class Mondstadt():
    id = 0
    description = "You are in Monstadt."
    exits = ['w','e','s']

    def __init__(self, id, description, exits):
        self.id = id
        self.description = description
        self.exits = exits


class Liyue():
    id = 1
    description = "You are in Liyue."
    exits = ['w','n']

    def __init__(self, id, description, exits):
        self.id = id
        self.description = description
        self.exits = exits


world = []
world.append(
    Mondstadt(
        0,
        "You are in Monstadt",
        ['n','s']
    )
    
)
print( world[0].__dict__ )