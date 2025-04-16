class Player:
    def __init__(self, name):
        self.name = name
        self.lives = 10
        self.powers = ['Healing', 'Alchemy', 'Invisibility',
                       'Air Manipulation', 'Shapeshifting', 'X-ray vision']

    def lose_life(self):
        self.lives -= 1

    def gain_power(self, new_power):
        self.powers.append(new_power)
