import tkinter as tk
from tkinter import *
from Game import Game
from PIL import Image, ImageTk


class DungeonBoard:
    def __init__(self, game):
        self.root = tk.Tk()
        self.root.title("Dungeon Master")
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()
        self.game = game  # Attach the game logic
        self.tiles = []

        # Load trap image
        self.trap_image = PhotoImage(file="images/trap.png")

        # Load crown image
        self.crown_image = PhotoImage(file="images/crown.png")

        # Load  original monster image
        monster_image = Image.open("images/monster.png")
        monster_image = monster_image.resize((50, 50)) # Resize to fit

        self.monster_image = ImageTk.PhotoImage(monster_image)

        # Create the grayscale version of the monster image
        gray_monster_image = monster_image.convert("L")
        self.gray_monster_image = ImageTk.PhotoImage(gray_monster_image)

        # Create an empty 8x8 grid with placeholder images
        self.draw_board()

        # add movement buttons
        self.add_movement_buttons()

    def add_movement_buttons(self):
        horizontal_button = tk.Button(self.root, text="Move Right", command=lambda: self.game.move_player("horizontal"))
        horizontal_button.pack(side="left", padx=5)

        vertical_button = tk.Button(self.root, text="Move Down", command=lambda : self.game.move_player("vertical"))
        vertical_button.pack(side="right", padx=5)

    def draw_board(self):
        tile_size = 50  # Each tile is 50x50 pixels
        for row in range(8):
            row_tiles = []
            for col in range(8):
                x1, y1 = col * tile_size, row * tile_size
                x2, y2 = x1 + tile_size, y1 + tile_size
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")
                text = self.canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text="")
                row_tiles.append((rect, text))
            self.tiles.append(row_tiles)

    def update_tile(self, row, col, content, is_cleared):
        print(f"Updating tile at ({row},{col}) with content: {content}, is_cleared:{is_cleared}")

        rect, text = self.tiles[row][col]

        # Check if the content is "Monster" and use the monster image
        if content == "Monster":
            if is_cleared:
                # Display the gray monster image
                self.canvas.itemconfig(rect, fill="white") # Set the bg to white
                self.canvas.create_image((col * 50) + 25, (row * 50) + 25, image=self.gray_monster_image)
                self.canvas.itemconfig(text, text="") # Clear the text to avoid overlap

            else:
                # Display the regular monster image
                self.canvas.itemconfig(rect, fill="white")  # Set the bg to white
                self.canvas.create_image((col * 50) + 25, (row * 50) + 25, image=self.monster_image)
                self.canvas.itemconfig(text, text="")  # Clear the text to avoid overlap

        elif content == "Trap":
            # Display trap image
            self.canvas.itemconfig(rect, fill="white")  # Set the bg to white
            self.canvas.create_image((col * 50) + 25, (row * 50) + 25, image=self.trap_image)
            self.canvas.itemconfig(text, text="")  # Clear the text to avoid overlap

        elif content == "Crown":
            # Display crown image
            self.canvas.itemconfig(rect, fill="white")  # Set the bg to white
            self.canvas.create_image((col * 50) + 25, (row * 50) + 25, image=self.crown_image)
            self.canvas.itemconfig(text, text="")  # Clear the text to avoid overlap

        else:
            # Use colors for other contents

            color = self.get_color(content, is_cleared)
            self.canvas.itemconfig(rect, fill=color)
            self.canvas.itemconfig(text, text=content if not is_cleared else "Cleared")

    def get_color(self, content, is_cleared):
        if is_cleared:
            return "gray"
        elif content == "Empty":
            return "green"
        return "white"  # Default

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    # Create the visual board first
    dungeon_board = DungeonBoard(None)  # Temporarily set game as None
    # Create the game and link it to the board
    game = Game("Player1", dungeon_board)
    dungeon_board.game = game  # Attach the game logic to the board

    dungeon_board.run()

