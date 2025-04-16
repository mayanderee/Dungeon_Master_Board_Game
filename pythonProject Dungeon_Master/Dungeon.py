import random
from Floor import Floor


class Dungeon:
    def __init__(self):
        self.floors = self.create_dungeon()

    def create_dungeon(self):
        contents = ['Monster'] * 31 + ['Trap'] * 10 + ['Empty'] * 22
        random.shuffle(contents)

        contents.insert(0, 'Empty') # Ensures the first floor is always 'Empty'
        contents.insert(63, 'Crown') # Ensures the last floor is always 'Crown'

        return [Floor(i + 1, contents[i]) for i in range(64)]
