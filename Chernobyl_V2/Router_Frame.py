from tkinter import Frame, Label, Button, Tk
import router_info as router
from PIL import Image, ImageTk

root = Tk()

root.state('normal')
root.title('C by GE\u2122 Chernobyl Router Selector\u2122')

root.geometry(str(root.winfo_screenwidth()) + 'x' + str(root.winfo_screenheight()))

frameWidth = int(root.winfo_screenwidth()/6)
frameHeight = int(root.winfo_screenheight()/5) - 20

scale_ratio = root.winfo_screenheight()/1080

# style variables
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
IMG_BACKGROUND_RED = '#bb0000'

bgColorImage = IMG_BACKGROUND_GREEN

darkMode = True
if darkMode:
  bgColorFrame = BACKGROUND_DARK_FRAME
  fgColorFrame = FG_COLOR_DARK
  bgColorButton = BACKGROUND_DARK_BUTTON
  fgColorButtonGreen = DARK_BUTTON_GREEN
  fgColorButtonRed = DARK_BUTTON_RED
  # root.configure(bg=BACKGROUND_DARK_BUTTON)
  # root.configure(fg=FG_COLOR_DARK)
else:
  bgColorFrame = BACKGROUND_LIGHT_FRAME
  fgColorFrame = FG_COLOR_LIGHT
  bgColorButton = BACKGROUND_LIGHT_BUTTON
  fgColorButtonGreen = LIGHT_BUTTON_GREEN
  fgColorButtonRed = LIGHT_BUTTON_RED

borderStyle = 'ridge'
borderWidth = 3
alpha = 170

frames = []

class Router_Frame:
    
    def __init__(self, router_info):
        
        self.router_info = router_info
        self.frame = Frame(root, height=frameHeight, width=frameWidth, bd=borderWidth, bg=bgColorFrame, relief=borderStyle)
        self.frame.grid(column=self.router_info['x_pos'], row=self.router_info['y_pos'])
        
        self.img_URL = self.router_info['img_URL']
        self.img = Image.open(self.img_URL)
        if self.img.mode != 'RGBA':
            self.img.convert('RGBA')
            self.img.putalpha(alpha)
        
        self.img = self.img.resize((int(frameWidth-self.router_info['width_adjust'] * scale_ratio), int(frameHeight-self.router_info['height_adjust'] * scale_ratio)), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.img)
        self.image = Label(self.frame, image=self.render, bg=bgColorImage)
        self.image.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.2)
        
        self.label = Label(self.frame, text=self.router_info['label_text'], bg=bgColorFrame, fg=fgColorFrame)
        self.label.place(relwidth=0.9, relheight=0.2, relx=0.05)
        
        self.yesButton = Button(self.frame, text="ON", fg=fgColorButtonGreen, bg=bgColorButton, cursor='hand2', command=lambda: self.relay_on())
        self.yesButton.place(relwidth=0.3, relheight=0.2, relx=0.15, rely=0.75)
        self.noButton = Button(self.frame, text="OFF",  fg=fgColorButtonRed, bg=bgColorButton, cursor='hand2', command=lambda: self.relay_off())
        self.noButton.place(relwidth=0.3, relheight=0.2, relx=0.55, rely=0.75)
    
    
    def relay_on(self):
        self.image.config(bg=IMG_BACKGROUND_GREEN)
    
    
    def relay_off(self):
        self.image.config(bg=IMG_BACKGROUND_RED)
    
    
    def print_info(self):
        print(self.router_info)


frame1 = Router_Frame(router.router1)
frames.append(frame1)
frame2 = Router_Frame(router.router2)
frames.append(frame2)
frame3 = Router_Frame(router.router3)
frames.append(frame3)
frame4 = Router_Frame(router.router4)
frames.append(frame4)
frame5 = Router_Frame(router.router5)
frames.append(frame5)
frame6 = Router_Frame(router.router6)
frames.append(frame6)
frame7 = Router_Frame(router.router7)
frames.append(frame7)
frame8 = Router_Frame(router.router8)
frames.append(frame8)
frame9 = Router_Frame(router.router9)
frames.append(frame9)
frame10 = Router_Frame(router.router10)
frames.append(frame10)
frame11 = Router_Frame(router.router11)
frames.append(frame11)
frame12 = Router_Frame(router.router12)
frames.append(frame12)
frame13 = Router_Frame(router.router13)
frames.append(frame13)
frame14 = Router_Frame(router.router14)
frames.append(frame14)
frame15 = Router_Frame(router.router15)
frames.append(frame15)
frame16 = Router_Frame(router.router16)
frames.append(frame16)
frame17 = Router_Frame(router.router17)
frames.append(frame17)
frame18 = Router_Frame(router.router18)
frames.append(frame18)
frame19 = Router_Frame(router.router19)
frames.append(frame19)
frame20 = Router_Frame(router.router20)
frames.append(frame20)
frame21 = Router_Frame(router.router21)
frames.append(frame21)
frame22 = Router_Frame(router.router22)
frames.append(frame22)
frame23 = Router_Frame(router.router23)
frames.append(frame23)
frame24 = Router_Frame(router.router24)
frames.append(frame24)
frame25 = Router_Frame(router.router25)
frames.append(frame25)
frame26 = Router_Frame(router.router26)
frames.append(frame26)
frame27 = Router_Frame(router.router27)
frames.append(frame27)
frame28 = Router_Frame(router.router28)
frames.append(frame28)
frame29 = Router_Frame(router.router29)
frames.append(frame29)
frame30 = Router_Frame(router.router30)
frames.append(frame30)

#for frame in frames:
#    print(frame.router_info['img_URL'])
#print(frame1.router_info)