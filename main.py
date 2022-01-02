from tkinter import *
from cell import Cell
import settings
import utils

# Override the default settings for the window
root = Tk()
root.configure(bg="black")
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.title("Minesweeper Game")
root.resizable(False, False)

# Creating top frame
top_frame = Frame(
    root,
    bg="red",
    width=settings.WIDTH,
    height=utils.height_percent(25))

# Placing the top frame
top_frame.place(x=0, y=0)

# Creating left frame
left_frame = Frame(
    root,
    bg="yellow",
    width=utils.width_percent(25),
    height=utils.height_percent(75))

# Placing the left frame
left_frame.place(x=0, y=180)

# Creating center frame
center_frame = Frame(
    root,
    bg="white",
    width=utils.width_percent(75),
    height=utils.height_percent(75))

# Placing the center frame
center_frame.place(x=utils.width_percent(
    25), y=utils.height_percent(25))


# Creating a grid of cell buttons with x columns and y rows
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        cell = Cell(x, y)
        cell.create_button_object(center_frame)
        cell.cell_button_object.grid(column=x, row=y, padx=2, pady=2)

Cell.randomize_mines()


# Running the main window in loop
root.mainloop()
