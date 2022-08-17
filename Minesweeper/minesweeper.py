from tkinter import *
import settings
import utils
from cell import Cell

root = Tk()
# Configure window
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Minesweeper Game')
root.resizable(False, False)
# root.configure(bg=settings.DEFAULT_BACKGROUND)
top_frame = Frame(
    root,
    bg=settings.DEFAULT_BACKGROUND,
    width=settings.WIDTH,
    height=utils.height_pct(20)
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg=settings.DEFAULT_BACKGROUND,
    width=utils.width_pct(25),
    height=utils.height_pct(80)
)
left_frame.place(x=0, y=utils.height_pct(20))

center_frame = Frame(
    root,
    bg=settings.DEFAULT_BACKGROUND,
    width=utils.width_pct(75),
    height=utils.height_pct(80),
)
center_frame.place(x=utils.width_pct(25), y=utils.height_pct(20))

for y in range(settings.GRID_SIZE):
    for x in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_obj(center_frame)
        c.cell_btn_obj.grid(
            column=x,
            row=y
        )

Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_obj.place(x=0, y=0)

# print(Cell.all)
Cell.randomize_mines()

# Run the window
root.mainloop()