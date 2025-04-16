from Player import Player
from Dungeon import Dungeon
from Floor import Floor
from tkinter import messagebox
import random


class Game:
    def __init__(self, player_name, board):
        self.player = Player(player_name)
        self.dungeon = Dungeon()
        self.current_floor = 0
        self.board = board  # Connect the visual board to the game logic
        self.update_board()

    def move_player(self, direction):
        """
        Moves the player forward horizontally or downward vertical based on the player chosen direction
        :param direction:horizontally or vertical
        """
        if direction == "horizontal":
            # move horizontally
            if self.current_floor % 8 < 7: # Ensure not the last column
                self.current_floor += 1
            else:
                messagebox.showerror("Invalid", "You can't move horizontally from the last column")
                return
        elif direction == "vertical":
            # move vertically
            if self.current_floor + 8 < 64: # Ensure not the last row
                self.current_floor += 8
            else:
                messagebox.showerror("Invalid", "You can't move vertically from the last row")
                return
        else:
            messagebox.showerror("Invalid Direction", "Choose a valid direction")

        self.encounter()

        self.update_board()

    def encounter(self):
        floor = self.dungeon.floors[self.current_floor]
        if floor.content == 'Monster':
            self.combat(floor)
        elif floor.content == 'Trap':
            messagebox.showwarning("Trap", f"You fell into a trap! Back to the start! At floor number: {floor.number} ")
            self.current_floor = 0
        elif floor.content == 'Crown':
            messagebox.showinfo("Crown", "You reached the crown floor! The game ends")
        else:
            messagebox.showinfo("Safe Floor", f"An empty floor. Nothing happens. You at floor number: {floor.number}")
        self.update_board()

    def combat(self,floor):
        roll = random.randint(1, 6) # Simulate a dice roll
        if roll > 3: # Example logic: rolls > 3 defeat the monster
            floor.clear_floor()
            new_powers = f"Power from Floor {floor.number}"
            self.player.gain_power(new_powers)
            messagebox.showinfo("Victory!",
                                f"You have defeated the monster! Gained {new_powers} "
                                f"The power gained:{self.player.gain_power(self.player.powers)}.")
        else:
            messagebox.showerror("Defeat!", "The monster defeated you! Try again.")
            self.player.lose_life()
            if self.player.lives == 0:
                messagebox.showerror("Game Over", "You have no lives left.Game over!")
                quit()

    def update_board(self):
        for i, floor in enumerate(self.dungeon.floors):
            row, col = divmod(i, 8)
            self.board.update_tile(row, col, floor.content, floor.is_cleared)
