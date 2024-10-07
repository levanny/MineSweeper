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
c1 = Cell()
c1.create_btn_object(center_frame)
c1.cell_btn_object.grid(row=0, column=0)

c2 = Cell()
c2.create_btn_object(center_frame)
c2.cell_btn_object.grid(row=0, column=1)


root.mainloop()
