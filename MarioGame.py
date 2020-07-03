'Imagine you are creating a Super Mario game.'
'You need to define a class to represent Mario. What would it look like? '
'If you are not familiar with SuperMario, use your own favorite video or board game to model a player.'

class Mario():
    print("""****MARIO****""")
    print("""***The character of Mario class***""")

    def __init__(self, id):
        self.height = 64
        self.width = 76
        self.speed = 10
        self.jump = 5
        self.lives = 3
        self.sprite = ""
        self.id = id

    def draw(self, screen):
        pass

    def update(self, time):
        pass

    def move(self, direction):
        pass

    def jump(self):
        pass

    def collides(self, other):
        return
