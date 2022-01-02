from tkinter import Button
from tkinter.constants import DISABLED, GROOVE
import settings
import random


class Cell:
    all_cell_objects = []

    def __init__(self, x, y, is_mine=False) -> None:
        self.is_mine = is_mine
        self.cell_button_object = None
        self.x = x
        self.y = y

        # Appending the cell objects to all_cell_objects list
        Cell.all_cell_objects.append(self)

    def __repr__(self) -> str:
        return f"Cell({self.x},{self.y})"

    # Creating a button object and assigning it to cell button object
    def create_button_object(self, location):
        button = Button(
            location,
            bg="#D3D3D3",
            width=4,
            height=2
        )
        # Assigning actions to left click and right click on the button
        button.bind("<Button-1>", self.left_click_action)
        button.bind("<Button-3>", self.right_click_action)
        self.cell_button_object = button

    # Defining actions when the user left clicks
    def left_click_action(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            # Show all surrounding cells if there are no mines around a cell object
            if self.surrounding_mines_count == 0:
                for cell_object in self.surrounded_cells:
                    cell_object.show_cell()
                    if cell_object.surrounding_mines_count == 0:        # Show all the zero mine cells that are adjacent
                        for cell in cell_object.surrounded_cells:
                            cell.show_cell()
            self.show_cell()

    # Return cell object from the given x and y coordinate of the grid
    def get_cell_object_by_axis(self, x, y):
        for cell in Cell.all_cell_objects:
            if cell.x == x and cell.y == y:
                return cell

    # Returns a list of all surrounding cells
    @property
    def surrounded_cells(self):
        # Collecting a list of all surrounding cell objects
        surrounding_cells = [
            self.get_cell_object_by_axis(self.x - 1, self.y - 1),
            self.get_cell_object_by_axis(self.x - 1, self.y),
            self.get_cell_object_by_axis(self.x - 1, self.y + 1),
            self.get_cell_object_by_axis(self.x, self.y - 1),
            self.get_cell_object_by_axis(self.x, self.y + 1),
            self.get_cell_object_by_axis(self.x + 1, self.y - 1),
            self.get_cell_object_by_axis(self.x + 1, self.y),
            self.get_cell_object_by_axis(self.x + 1, self.y + 1)
        ]

        # Removing None items from the list for corner and side cells
        surrounding_cells = [
            cell for cell in surrounding_cells if cell is not None]
        return surrounding_cells

    # Returns the number of mines in surrounding cells
    @property
    def surrounding_mines_count(self):
        count = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                count += 1

        return count

    # Display the number of surrounding mines on the cell
    def show_cell(self):
        self.cell_button_object.configure(
            relief=GROOVE,
            state=DISABLED,
            disabledforeground="BLACK",
            text=self.surrounding_mines_count)

    def show_mine(self):
        # Logic to interrupt the game and display game over message
        self.cell_button_object.configure(bg="red")

    # Defining actions when the user right clicks
    def right_click_action(self, event):
        pass

    # Picking random cells from all cells to mark as mine
    @staticmethod
    def randomize_mines():
        picked_mines = random.sample(
            Cell.all_cell_objects, settings.MINE_COUNT)
        for picked_mine in picked_mines:
            picked_mine.is_mine = True
