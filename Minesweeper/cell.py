from tkinter import Button, Label, messagebox
import random
import settings
import sys

class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_obj = None
    def __init__(self, x, y, is_mine=False):
        self.x = x
        self.y = y
        self.is_mine = is_mine
        self.cell_btn_obj = None
        self.is_shown = False
        self.is_suspect = False
        Cell.all.append(self)
    
    def create_btn_obj(self, location):
        btn = Button(
            location,
            width=1,
            height=2,
            bg=settings.DEFAULT_BACKGROUND
            # text=f'{self.x[0]}, {self.y[0]}'
        )
        btn.bind('<Button-1>', self.left_click_actions) # Left Click
        btn.bind('<Button-2>', self.right_click_actions) # Right Click
        self.cell_btn_obj = btn
    
    def left_click_actions(self, event):
        # print(event)
        # print('I am left clicked!')
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mine_count == 0:
                for cell in self.surrounded_cells:
                    cell.show_cell()
            self.show_cell()
            if Cell.cell_count == settings.MINES_COUNT:
                messagebox.showinfo(title='Game Over!', message='YOU WON!')
    
    def right_click_actions(self, event):
        # print(event)
        # print('I am right clicked!')
        if not self.is_suspect:
            self.cell_btn_obj.configure(highlightbackground='blue')
            self.is_suspect = True
            # Cell.cell_count -= 1
        else:
            self.cell_btn_obj.configure(highlightbackground='black')
            self.is_suspect = False
            # Cell.cell_count += 1
        Cell.cell_count_label_obj.configure(text=f'Cells left: {Cell.cell_count}')
    
    def show_mine(self):
        messagebox.showinfo(title='Game Over!', message='You clicked on a mine!')
        for cell in Cell.all:
            if cell.is_mine:
                cell.cell_btn_obj.configure(text='💣')
                cell.cell_btn_obj.configure(highlightbackground='red')
                cell.cell_btn_obj.unbind('<Button-1>')
                cell.cell_btn_obj.unbind('<Button-2>')
            else:
                cell.show_cell()


    def show_cell(self):
        if not self.is_shown:
            # Cancel left and right click events if cell is already shown
            self.cell_btn_obj.unbind('<Button-1>')
            self.cell_btn_obj.unbind('<Button-2>')
            Cell.cell_count -= 1
            self.cell_btn_obj.configure(text=self.surrounded_cells_mine_count)
            if Cell.cell_count_label_obj:
                Cell.cell_count_label_obj.configure(text=f'Cells left: {Cell.cell_count}')
            self.cell_btn_obj.configure(highlightbackground='black')
        self.is_shown = True

    
    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells
    
    @property
    def surrounded_cells_mine_count(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell



    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg=settings.DEFAULT_BACKGROUND,
            text=f'Cells left: {Cell.cell_count}',
            font=('', 30)
        )
        Cell.cell_count_label_obj = lbl

    @staticmethod
    def randomize_mines():
        sample_size = settings.MINES_COUNT
        random_cells = random.sample(Cell.all, sample_size)
        # print('random_cells', random_cells)
        for cell in random_cells:
            cell.is_mine = True

    def __repr__(self):
        return f'Cell({self.x}, {self.y})'