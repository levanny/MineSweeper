
from tkinter import Button
import random
import Settings as St


def right_click(event):
    print("right click")
    print(event.widget)


def left_click(event):
    print("left click")
    print(event.widget)


class Cell:
    all = []

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y
        Cell.all.append(self)

    def create_btn_object(self, frame):
        btn = Button(
            frame,
            width=10,
            height=4,
            text=f"{self.x} | {self.y}"
        )
        btn.bind('<Button-1>', left_click)
        btn.bind('<Button-3>', right_click)
        self.cell_btn_object = btn

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, St.Mines_Count)

        for cell in picked_cells:
            cell.is_mine = True

    def __repr__(self):
        return f"({self.x})({self.y})"
