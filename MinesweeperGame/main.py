from tkinter import *
from cell import Cell
import setting
import ulits

root = Tk()
root.configure(bg="Black")
root.geometry(f"{setting.WIDTH}x{setting.HEIGHT}")
root.title("Minesweeper Game")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg="Black",
    width=ulits.width_perc(100),
    height=ulits.height_perc(25)
)
top_frame.place(x=0, y=0)

game_title = Label(top_frame, bg="Black", fg="white", text="Minesweeper Game", font=('', 48))
game_title.place(x=ulits.width_perc(25), y=0)

left_frame = Frame(
    root,
    bg="Black",
    width=ulits.width_perc(25),
    height=ulits.height_perc(75)
)
left_frame.place(x=0, y=ulits.height_perc(25))

center_frame = Frame(
    root,
    bg="Black",
    width=ulits.width_perc(75),
    height=ulits.height_perc(75)
)
center_frame.place(x=ulits.width_perc(25), y=ulits.height_perc(25))

for x in range(setting.GRID_SIZE):
    for y in range(setting.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x,
            row=y
        )
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_obj.place(x=0, y=0)

Cell.random_mines()

root.mainloop()
