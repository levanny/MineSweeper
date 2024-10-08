from tkinter import *
import Settings as St
import Utilities as Ut
from Cells import Cell

root = Tk()
root.geometry(f'{St.Width}x{St.Length}')
root.configure(background='white')
root.resizable(False, False)
root.title('Minesweeper')

# Left Frame
left_frame = Frame(root, bg='black', width=Ut.perc_width(12), height=Ut.perc_width(25))
left_frame.pack(side=LEFT, fill=Y)

# Top Frame
top_frame = Frame(root, bg='black', width=1720, height=Ut.perc_height(15))
top_frame.pack(side=TOP, fill=X)

# Center Frame
center_frame = Frame(root, bg='gray', width=Ut.perc_width(88), height=Ut.perc_height(75))
center_frame.pack(side=LEFT, fill=BOTH)

# Create Cell
for i in range(St.Grid_Size):
    for j in range(St.Grid_Size):
        c = Cell(i, j)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(row=i, column=j)

#gamarjobak
Cell.randomize_mines()




print(Cell.all)

root.mainloop()
