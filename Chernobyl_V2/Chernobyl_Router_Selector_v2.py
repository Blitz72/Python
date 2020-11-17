from tkinter import Tk, Frame, Label, Button, Entry, Listbox, Menu, Toplevel, IntVar, Radiobutton, Checkbutton, messagebox
#from tkinter import *
import router_info as router
from PIL import Image, ImageTk
from Database import *
# import pijuice
try:
    import smbus
except Exception as ex:
    print(ex)

root = Tk()
root.child_window = None

root.state('normal')
root.title('C by GE\u2122 Chernobyl Router Selector\u2122')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

geom_str = str(screen_width) + 'x' + str(screen_height)
print('Resolution: ', geom_str)
root.geometry(geom_str)

frameWidth = int(screen_width/6)
frameHeight = int(screen_height/5) - 20

scale_ratio = screen_height/1080

# Style variables
BACKGROUND_LIGHT_FRAME = '#dddddd'
BACKGROUND_LIGHT_BUTTON = '#eeeeee'
FG_COLOR_LIGHT = 'black'
LIGHT_BUTTON_GREEN = 'green'
LIGHT_BUTTON_RED = 'red'
BACKGROUND_DARK_FRAME = '#333333'
BACKGROUND_DARK_BUTTON = '#555555'
DARK_BUTTON_GREEN = '#aaffaa'
DARK_BUTTON_RED = '#ffaaaa'
FG_COLOR_DARK = 'white'
IMG_BACKGROUND_GREEN = '#00bb00'
IMG_ACTIVEBACKGROUND_GREEN = '#005500'
IMG_BACKGROUND_RED = '#bb0000'
IMG_ACTIVEBACKGROUND_RED = '#440000'

borderStyle = 'ridge'
borderWidth = 3
alpha = 168

db_path = '/home/pi/Python/Chernobyl_V2/db/Chernobyl.db'
# db_path = './db/Chernobyl.db'

# MCP23017 config variables
channel = 1
address1 = 0x20
address2 = 0x21
IODIRA = 0x00
IODIRB = 0x01
GPIOA = 0x12
GPIOB = 0x13

# Setup MCP23017, set IODIR registers as outputs with 0's, or inputs as 1's
try:
    bus = smbus.SMBus(channel)
    print('I2C bus initialized!\n')
except Exception as ex:
    print(ex)
    print('Could not initialize I2C bus!\n')

try:
    bus.write_byte_data(address1, IODIRA, 0x00)
    bus.write_byte_data(address1, IODIRB, 0x00)
except Exception as ex:
    print(ex)
    print('An error occurred writing to:', hex(address1))
    print()
try:
    bus.write_byte_data(address2, IODIRA, 0x00)
    bus.write_byte_data(address2, IODIRB, 0x00)
except Exception as ex:
    print(ex)
    print('An error occurred writing to:', hex(address2))
    print()

frames = []

def check_dark_mode():
    # Check dark_mode from the config table of the database before rendering tkinter frames
    with Database(db_path, 'SELECT dark_mode FROM config') as dm_value:
        print('dark_mode: ', dm_value[0])
    if dm_value[0]:
        bg_color_frame = BACKGROUND_DARK_FRAME
        fg_color_frame = FG_COLOR_DARK
        bg_color_button = BACKGROUND_DARK_BUTTON
        fg_color_button_green = DARK_BUTTON_GREEN
        fg_color_button_red = DARK_BUTTON_RED
    else:
        bg_color_frame = BACKGROUND_LIGHT_FRAME
        fg_color_frame = FG_COLOR_LIGHT
        bg_color_button = BACKGROUND_LIGHT_BUTTON
        fg_color_button_green = LIGHT_BUTTON_GREEN
        fg_color_button_red = LIGHT_BUTTON_RED
    return bg_color_frame, fg_color_frame, bg_color_button, fg_color_button_green, fg_color_button_red

bg_color_frame, fg_color_frame, bg_color_button, fg_color_button_green, fg_color_button_red = check_dark_mode()

class Router:
    
    def __init__(self, router_info, bus):
        self.router_info = router_info
        self.bus = bus
        self.relay_num = (self.router_info['x_pos'] + 1) + (self.router_info['y_pos'] * 6)
        
        if 1 <= self.relay_num <= 8:
            self.mcp_address = 0x20
            self.mcp_gpio_reg = GPIOA
            self.gpio_reg = 'gpioa1'
        elif 9 <= self.relay_num <= 16:
            self.mcp_address = 0x20
            self.mcp_gpio_reg = GPIOB
            self.gpio_reg = 'gpiob1'
        elif 17 <= self.relay_num <= 24:
            self.mcp_address = 0x21
            self.mcp_gpio_reg = GPIOA
            self.gpio_reg = 'gpioa2'
        else:
            self.mcp_address = 0x21
            self.mcp_gpio_reg = GPIOB
            self.gpio_reg = 'gpiob2'
            
        db_query = 'SELECT ' + str(self.gpio_reg) + ' from config'
        with Database(db_path, db_query) as gpio_value:
            print(gpio_value)
        _gpio_value = gpio_value[0]
        if _gpio_value & (1 << (self.relay_num - 1) % 8):
            bg_color_image = IMG_BACKGROUND_GREEN
            bg_activebackground = IMG_ACTIVEBACKGROUND_GREEN
        else:
            bg_color_image = IMG_BACKGROUND_RED
            bg_activebackground = IMG_ACTIVEBACKGROUND_RED
        
        self.frame = Frame(root, height=frameHeight, width=frameWidth, bd=borderWidth, bg=bg_color_frame, relief=borderStyle)
        self.frame.grid(column=self.router_info['x_pos'], row=self.router_info['y_pos'])
        
        self.img_URL = self.router_info['img_URL']
        self.img = Image.open(self.img_URL)
        if self.img.mode != 'RGBA':
            self.img.convert('RGBA')
            self.img.putalpha(alpha)
        self.img = self.img.resize((int(frameWidth-self.router_info['width_adjust'] * scale_ratio),
                                    int(frameHeight-self.router_info['height_adjust'] * scale_ratio)), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.img)
        self.info_img = self.img
        self.info_img = self.info_img.resize((int((frameWidth-self.router_info['width_adjust']) * 2),
                                    int((frameHeight-self.router_info['height_adjust']) * 2)), Image.ANTIALIAS)
        self.info_render = ImageTk.PhotoImage(self.info_img)
        self.image = Button(self.frame, image=self.render, bg=bg_color_image, cursor='hand2', relief='flat',
                                  activebackground=bg_activebackground, command=lambda: self.info_window())
        self.image.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.2)
        
        self.label = Label(self.frame, text=self.router_info['label_text'], bg=bg_color_frame, fg=fg_color_frame)
        self.label.place(relwidth=0.9, relheight=0.2, relx=0.05)
        
        self.yes_button = Button(self.frame, text="ON", fg=fg_color_button_green, bg=bg_color_button,
                                activebackground='#aaaaaa',cursor='hand2', command=lambda: self.relay_on())
        self.yes_button.place(relwidth=0.3, relheight=0.2, relx=0.15, rely=0.75)
        
        self.no_button = Button(self.frame, text="OFF",  fg=fg_color_button_red, bg=bg_color_button,
                               activebackground='#aaaaaa',cursor='hand2', command=lambda: self.relay_off())
        self.no_button.place(relwidth=0.3, relheight=0.2, relx=0.55, rely=0.75)
    
    def relay_on(self):
        db_query = 'SELECT ' + str(self.gpio_reg) + ', confirm from config'
        with Database(db_path, db_query) as values:
            print(values[0])
            print(values[1])
        gpio_value = values[0]
        confirm = values[1]
        if gpio_value & (1 << (self.relay_num - 1) % 8):
            return
        else:
            if confirm < 2:
                confirmation = True
            else:
                if messagebox.askyesno("Confirm to energize relay", "Do you want energize the relay?"):
                    confirmation = True
                else:
                    confirmation = False
            print('confirmation', confirmation)
            if confirmation:
                new_value = gpio_value | (1 << (self.relay_num - 1) % 8)
                db_query = 'UPDATE config SET ' + self.gpio_reg + ' = ' + str(new_value)
                with Database(db_path, db_query) as update:
                    print(update)
                try:
                    self.bus.write_byte_data(self.mcp_address, self.mcp_gpio_reg, new_value)
                except Exception as ex:
                    print(ex)
                    print('An error ocurred writing to: ', self.mcp_address)
                print(self.gpio_reg + ' = ', new_value)
                self.image.config(bg=IMG_BACKGROUND_GREEN)
            else:
                return
    
    def relay_off(self):
        db_query = 'SELECT ' + str(self.gpio_reg) + ', confirm from config'
        with Database(db_path, db_query) as values:
            print(values[0])
            print(values[1])
        gpio_value = values[0]
        confirm = values[1]
        if (gpio_value >> (self.relay_num - 1) % 8) & 1 == 0:
            return
        else:
            if confirm < 1:
                confirmation = True 
            else:
                if messagebox.askyesno("Confirm to energize relay", "Do you want de-energize the relay?"):
                    confirmation = True
                else:
                    confirmation = False
            print('confirmation', confirmation)
            if confirmation:
                new_value =  gpio_value & ~(1 << (self.relay_num - 1) % 8)
                db_query = 'UPDATE config SET ' + self.gpio_reg + ' = ' + str(new_value)
                with Database(db_path, db_query) as update:
                    print(update)
                try:
                    self.bus.write_byte_data(self.mcp_address, self.mcp_gpio_reg, new_value)
                except Exception as ex:
                    print(ex)
                    print('An error ocurred writing to: ', self.mcp_address)
                print(self.gpio_reg + ' = ', new_value)
                self.image .config(bg=IMG_BACKGROUND_RED)
            else:
                return
            
    def info_window(self):
        import webbrowser
        
        def callback(event):
            webbrowser.open(event.widget.cget('text'))
            
        global screen_width, screen_height
        center_x = int(screen_width/2)
        center_y = int(screen_height/2)
        win_width = 600
        win_height = 350
        bg = '#e7e7e7'
        
        row_index = 0
        pad_x_desc = 30
        pad_y_desc = 10
        pad_x_table = 110
        
        if not root.child_window:
            root.child_window = Toplevel(bg=bg)
        else:
            root.child_window.destroy()
            root.child_window = Toplevel(bg=bg)
        root.child_window.title(self.router_info['label_text'])
        root.child_window.geometry('%sx%s+%s+%s' % (str(win_width), str(win_height), str(center_x-int(win_width/2)),
                                              str(center_y-int(win_height/2))))
        root.child_window.focus_set()
        
        desc_label = Label(root.child_window, text=self.router_info['description'], bg=bg, wraplength=250, justify='center',
                           padx=pad_x_desc)
        desc_label.grid(row=row_index, column=0, pady=pad_y_desc)
        
        image_label = Label(root.child_window, image=self.info_render, bg='#ffffff', justify='center')
        image_label.grid(row=row_index, column=1, columnspan=2, pady=pad_y_desc)
        row_index += 1
        
        label_blank = Label(root.child_window, text='', bg=bg, pady=2).grid(row=row_index, column=1)
        row_index += 1
        
        label_SSID1 = Label(root.child_window, text='SSID', bg=bg, padx=pad_x_table)
        label_SSID1.grid(row=row_index, column=0, sticky='w')
        label_SSID2 = Label(root.child_window, text=self.router_info['SSID'], bg=bg)
        label_SSID2.grid(row=row_index, column=1, sticky='w')
        row_index += 1
        
        label_password1 = Label(root.child_window, text='Password', bg=bg, padx=pad_x_table)
        label_password1.grid(row=row_index, column=0, sticky='w')
        label_password2 = Label(root.child_window, text=self.router_info['password'], bg=bg)
        label_password2.grid(row=row_index, column=1, sticky='w')
        row_index += 1
        
        label_bands1 = Label(root.child_window, text='RF Bands', bg=bg, padx=pad_x_table)
        label_bands1.grid(row=row_index, column=0, sticky='w')
        label_bands2 = Label(root.child_window, text=self.router_info['rf_bands'], bg=bg)
        label_bands2.grid(row=row_index, column=1, sticky='w')
        row_index += 1
        
        label_links1 = Label(root.child_window, text='Helpful links', bg=bg, padx=pad_x_table)
        label_links1.grid(row=5, column=0, sticky='w')
        for link in self.router_info['router_links']:
            label = Label(root.child_window, text=link, bg=bg, fg='blue', cursor='hand2')
            label.grid(row=row_index, column=1, sticky='w')
            label.bind('<Button-1>', callback)
            row_index += 1
    
    def print_info(self):
        print(self.router_info)


def update_root():
    bg_color_frame, fg_color_frame, bg_color_button, fg_color_button_green, fg_color_button_red = check_dark_mode()
    for frame in frames:
        frame.frame.configure(bg=bg_color_frame)
        frame.label.configure(bg=bg_color_frame, fg=fg_color_frame)
        frame.yes_button.configure(bg=bg_color_button, fg=fg_color_button_green)
        frame.no_button.configure(bg=bg_color_button, fg=fg_color_button_red)

def create_window():
    bg = '#d7d7d7'
    if not root.child_window:
        root.child_window = Toplevel(bg=bg)
    else:
        root.child_window.destroy()
        root.child_window = Toplevel(bg=bg)
    root.child_window.title('C by GE\u2122 Chernobyl Router Selector\u2122 Settings')
    root.child_window.geometry('450x200+5+100')
    root.child_window.focus_set()
    
    db_query = 'SELECT confirm, dark_mode from config'
    with Database(db_path, db_query) as db_settings:
        print(db_settings)
    confirm = db_settings[0]
    dark_mode = db_settings[1]
    
    confirm_state = IntVar()
    confirm_state.set(confirm)
    dark_mode_state = IntVar()
    dark_mode_state.set(dark_mode)
    height = 0.15
    width = 0.5
    offset = 0.05
    
    def save_option():
        # print(confirm_setting.get())
        with Database(db_path, 'UPDATE config SET confirm = ' + str(confirm_state.get())) as confirm_update:
            print('Updated confirn setting.')
        with Database(db_path, 'UPDATE config SET dark_mode = ' + str(dark_mode_state.get())) as dark_mode_update:
            print('Updated dark_mode setting.')
        settings_label = Label(root.child_window, text="Settings Saved!", pady=10)
        settings_label.place(relwidth=0.5, relheight=0.2, relx=0.25, rely=0.8)
#        settings_label.pack()
        update_root()
        root.child_window.destroy()
    
#    blank_label = Label(root.child_window, text='', bg=bg).pack()
    
    radio1 = Radiobutton(root.child_window, text="No Confirmation Required", pady=2, variable=confirm_state, value=0)
    radio1.place(relwidth=width, relheight=height, relx=0.25, rely=0 + offset)
#    radio1.pack()

    radio2 = Radiobutton(root.child_window, text="Confirm for OFF Only        ", pady=2, variable=confirm_state, value=1)
    radio2.place(relwidth=width, relheight=height, relx=0.25, rely=0.15 + offset)
#    radio2.pack()

    radio3 = Radiobutton(root.child_window, text="Confirm for ON and OFF   ", pady=2, variable=confirm_state, value=2)
    radio3.place(relwidth=width, relheight=height, relx=0.25, rely=0.3 + offset)
#    radio3.pack()
    
    check_dark_mode = Checkbutton(root.child_window, text="Dark Mode", pady=2, variable=dark_mode_state)
    check_dark_mode.place(relwidth=width, relheight=height, relx=0.24, rely=.45 + offset)
#    check_dark_mode.pack()
    
    apply_button = Button(root.child_window, text="Apply", pady=2, command=save_option)
    apply_button.place(relwidth=0.2, relheight=height, relx=0.4, rely=0.63 + offset)
#    apply_button.pack()
    
def on_close():
    if messagebox.askyesno("Quit C by GE\u2122 Chernobyl Router Selector\u2122", "Do you want to exit the C by GE\u2122 Chernobyl Router Selector\u2122?"):
        root.destroy()

menu = Menu(root)
new_item = Menu(menu)
menu.add_command(label='Settings', command=create_window)
root.config(menu=menu)

frame1 = Router(router.router1, bus)
frames.append(frame1)
frame2 = Router(router.router2, bus)
frames.append(frame2)
frame3 = Router(router.router3, bus)
frames.append(frame3)
frame4 = Router(router.router4, bus)
frames.append(frame4)
frame5 = Router(router.router5, bus)
frames.append(frame5)
frame6 = Router(router.router6, bus)
frames.append(frame6)
frame7 = Router(router.router7, bus)
frames.append(frame7)
frame8 = Router(router.router8, bus)
frames.append(frame8)
frame9 = Router(router.router9, bus)
frames.append(frame9)
frame10 = Router(router.router10, bus)
frames.append(frame10)
frame11 = Router(router.router11, bus)
frames.append(frame11)
frame12 = Router(router.router12, bus)
frames.append(frame12)
frame13 = Router(router.router13, bus)
frames.append(frame13)
frame14 = Router(router.router14, bus)
frames.append(frame14)
frame15 = Router(router.router15, bus)
frames.append(frame15)
frame16 = Router(router.router16, bus)
frames.append(frame16)
frame17 = Router(router.router17, bus)
frames.append(frame17)
frame18 = Router(router.router18, bus)
frames.append(frame18)
frame19 = Router(router.router19, bus)
frames.append(frame19)
frame20 = Router(router.router20, bus)
frames.append(frame20)
frame21 = Router(router.router21, bus)
frames.append(frame21)
frame22 = Router(router.router22, bus)
frames.append(frame22)
frame23 = Router(router.router23, bus)
frames.append(frame23)
frame24 = Router(router.router24, bus)
frames.append(frame24)
frame25 = Router(router.router25, bus)
frames.append(frame25)
frame26 = Router(router.router26, bus)
frames.append(frame26)
frame27 = Router(router.router27, bus)
frames.append(frame27)
frame28 = Router(router.router28, bus)
frames.append(frame28)
frame29 = Router(router.router29, bus)
frames.append(frame29)
frame30 = Router(router.router30, bus)
frames.append(frame30)

root.protocol('WM_DELETE_WINDOW', on_close)
root.mainloop()
