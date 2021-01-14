class GameObject:
    def __init__(self, game, position, velocity):
        self.game = game
        self.position = position
        self.velocity = velocity
        self.max_velocity = 10
