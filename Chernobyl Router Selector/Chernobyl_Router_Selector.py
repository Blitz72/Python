#!/usr/bin/env python
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
# import smbus
import time
import sqlite3 as db
# from Router_Config import *
import asyncio

root = Tk()

root.state('zoomed')
root.title('C by GE\u2122 Chernobyl Router Selector\u2122')
# root.iconbitmap('./images/cropped_favicon_300x300_GT0_icon.ico')
root.geometry('1920x1080')

frameWidth = int(root.winfo_screenwidth()/6)
frameHeight = int(root.winfo_screenheight()/5) - 20

print(root.winfo_screenwidth())
print(root.winfo_screenheight())

confirmType = {
   'noConfirm': 0,
   'confirmOff': 1,
   'confirmOnOff': 2
}

# print(confirmType['confirmOnOff'])

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

fgColorFrame = FG_COLOR_LIGHT
bgColorFrame = BACKGROUND_LIGHT_FRAME
fgColorButton = LIGHT_BUTTON_GREEN
bgColorButton = BACKGROUND_LIGHT_BUTTON

borderStyle = RIDGE
borderWidth = 3
alpha = 170

infoBtnX = 0.78
infoBtnY = 0.2


# MCP23017 config variables
channel = 1
address1 = 0x20
address2 = 0x21
IODIRA = 0x00
IODIRB = 0x01
GPIOA = 0x12
GPIOB = 0x13

# try:
#   bus = smbus.SMBus(channel)
# except Exception as ex:
#   print(ex)
#   print("Tried to initialize i2c bus.")

# try:
#   # bus.write_byte_data(address1, IODIRA, 0x00)
#   # bus.write_byte_data(address1, IODIRB, 0x00)
# except Exception as ex:
#   print(ex)
#   print('An error occurred writing to:', hex(address1))
# try:
#   # bus.write_byte_data(address2, IODIRA, 0x00)
#   # bus.write_byte_data(address2, IODIRB, 0x00)
# except Exception as ex:
#   print(ex)
#   print('An error occurred writing to:', hex(address2))


# layout variables
# rows = 5
# columns = 6


# database creation and connection
path = './db/Chernobyl.db'
connection = db.connect(path)
c = connection.cursor()

#c.execute('DROP TABLE config')
#c.execute('CREATE TABLE config (gpioa1 INTEGER, gpiob1 INTEGER, gpioa2 INTEGER, gpiob2 INTEGER, power_flag INTEGER, confirm INTEGER, dark_mode INTEGER)')
#c.execute('INSERT INTO config VALUES(0x00, 0x00, 0x00, 0x00, 0, 0, 0)')

#connection.commit()


# render image function
# def renderImage(frameNum, imgURL, alpha):
#   img = Image.open(imgURL)
#   if img.mode != 'RGBA':
#     img.convert('RGBA')
#     img.putalpha(alpha)
#   img = img.resize((frameWidth-100, frameHeight-75), Image.ANTIALIAS)
#   render = ImageTk.PhotoImage(img)
#   image = Label(frameNum, image=render)
#   image.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.2)


# create Toplevel "Settings" window
def createSettingsWindow():
  settingsWindow = Toplevel()
  settingsWindow.title('C by GE\u2122 Chernobyl Router Selector\u2122 Settings')
  settingsWindow.iconbitmap('images/cropped_favicon_300x300_GT0_icon.ico')
  settingsWindow.geometry('450x200')
  settingsWindow.focus_set()

  dbConfirmSetting = c.execute("SELECT confirm FROM config").fetchone()[0]
  dbDarkModeSetting = c.execute("SELECT dark_mode FROM config").fetchone()[0]

  confirm1 = IntVar()
  confirm1.set(dbConfirmSetting)
  darkModeState = IntVar()
  darkModeState.set(dbDarkModeSetting)
  height = 0.15
  width = 0.5
  
  # settingsWindow.protocol('WM_DELETE_WINDOW', on_settings_close)


  def saveOption():
    # task1 = asyncio.create_task(printSaved())
    # task2 = asyncio.create_task(closeSettingsWindow())
    # print(confirm1.get())
    c.execute("UPDATE config SET confirm = " + str(confirm1.get()))
    c.execute("UPDATE config SET dark_mode = " + str(darkModeState.get()))
    connection.commit()
    updateRoot()
    printSaved()
    # time.sleep(0.25)
    # await task1
    # await task2
    # settingsWindow.destroy()
  

  def printSaved():
    # time.sleep(0.25)
    settingsLabel = Label(settingsWindow, text="Settings Saved!", pady=10)
    settingsLabel.place(relwidth=0.5, relheight=0.2, relx=0.25, rely=0.8)
    closeSettingsWindow()


  def closeSettingsWindow():
    # time.sleep(0.25)
    settingsWindow.destroy()


  radio1 = Radiobutton(settingsWindow, text="No Confirmation Required", pady=2, variable=confirm1, value=0)
  radio1.place(relwidth=width, relheight=height, relx=0.25, rely=0)

  radio2 = Radiobutton(settingsWindow, text="Confirm for OFF Only        ", pady=2, variable=confirm1, value=1)
  radio2.place(relwidth=width, relheight=height, relx=0.25, rely=0.15)

  radio3 = Radiobutton(settingsWindow, text="Confirm for ON and OFF   ", pady=2, variable=confirm1, value=2)
  radio3.place(relwidth=width, relheight=height, relx=0.25, rely=0.3)

  checkDarkMode = Checkbutton(settingsWindow, text="Dark Mode", pady=2, variable=darkModeState)
  checkDarkMode.place(relwidth=width, relheight=height, relx=0.24, rely=.45)

  applyButton = Button(settingsWindow, text="Apply", pady=2, command=saveOption)
  applyButton.place(relwidth=0.2, relheight=height, relx=0.4, rely=0.63)

  #updates root when settings window "X" is clicked
  # def on_settings_close():
  #   connection.commit()
  #   updateRoot()
  #   infoWindow.destroy()


def createInfoWindow(routerInfo):
  # print(Frame.config())
  x = int(root.winfo_screenwidth() / 2 - 225)
  y = int(root.winfo_screenheight() / 2 - 125)
  # print(x)
  # print(y)
  title = "Router Info"
  geom = '+' + str(x) + '+' + str(y)

  infoWindow = Toplevel()
  infoWindow.iconbitmap('images/cropped_favicon_300x300_GT0_icon.ico')
  infoWindow.geometry('450x250')
  infoWindow.geometry(geom)
  infoWindow.title(title)

  mfrText = 'Manufacturer: ' + routerInfo['manufacturer']
  modelText = 'Model: ' + routerInfo['model']
  ssidText = 'SSID: ' + routerInfo['SSID']
  pwdText = 'Password: ' + routerInfo['password']
  
  myLabel = Label(infoWindow, text='')
  myLabel.pack()
  myLabel = Label(infoWindow, text='')
  myLabel.pack()
  mfrLabel = Label(infoWindow, text=mfrText, fg=FG_COLOR_LIGHT, font=('GE Inspira Sans', 14, 'bold'))
  mfrLabel.pack()
  modelLabel = Label(infoWindow, text=modelText, fg=FG_COLOR_LIGHT, font=('GE Inspira Sans', 14, 'bold'))
  modelLabel.pack()
  ssidLabel = Label(infoWindow, text=ssidText, fg=FG_COLOR_LIGHT, font=('GE Inspira Sans', 14, 'bold'))
  ssidLabel.pack()
  pwdLabel = Label(infoWindow, text=pwdText, fg=FG_COLOR_LIGHT, font=('GE Inspira Sans', 14, 'bold'))
  pwdLabel.pack()
  



# update root window after changing settings, called using "Refresh" menu button
def updateRoot():
  frames = [
    frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8, frame9, frame10,
    frame11, frame12, frame13, frame14, frame15, frame16, frame17, frame18,frame19, frame20,
    frame21, frame22, frame23, frame24, frame25, frame26, frame27, frame28, frame29, frame30
  ]

  labels = [
    myLabel1, myLabel2, myLabel3, myLabel4, myLabel5, myLabel6, myLabel7, myLabel8, myLabel9, myLabel10,
    myLabel11, myLabel12, myLabel13, myLabel14, myLabel15, myLabel16, myLabel17, myLabel18,myLabel19, myLabel20,
    myLabel21, myLabel22, myLabel23, myLabel24, myLabel25, myLabel26, myLabel27, myLabel28, myLabel29, myLabel30
  ]

  infoButtons = [
    infoButton1, infoButton2, infoButton3, infoButton4, infoButton5, infoButton6, infoButton7, infoButton8, 
    infoButton9, infoButton10, infoButton11, infoButton12, infoButton13, infoButton14, infoButton15, 
    infoButton16, infoButton17, infoButton18, infoButton19, infoButton20, infoButton21, infoButton22, 
    infoButton23, infoButton24, infoButton25, infoButton26, infoButton27, infoButton28, 
    infoButton29, infoButton30
  ]

  yesButtons = [
    yesButton1, yesButton2, yesButton3, yesButton4, yesButton5, yesButton6, yesButton7, yesButton8, yesButton9, yesButton10,
    yesButton11, yesButton12, yesButton13, yesButton14, yesButton15, yesButton16, yesButton17, yesButton18,yesButton19, yesButton20,
    yesButton21, yesButton22, yesButton23, yesButton24, yesButton25, yesButton26, yesButton27, yesButton28, yesButton29, yesButton30
  ]

  noButtons = [
    noButton1, noButton2, noButton3, noButton4, noButton5, noButton6, noButton7, noButton8, noButton9, noButton10,
    noButton11, noButton12, noButton13, noButton14, noButton15, noButton16, noButton17, noButton18,noButton19, noButton20,
    noButton21, noButton22, noButton23, noButton24, noButton25, noButton26, noButton27, noButton28, noButton29, noButton30
  ]

  darkMode = c.execute("SELECT dark_mode FROM config").fetchone()[0]
  if darkMode:
    bgColorFrame = BACKGROUND_DARK_FRAME
    fgColor = FG_COLOR_DARK
    bgColorButton = BACKGROUND_DARK_BUTTON
    fgColorButtonGreen = DARK_BUTTON_GREEN
    fgColorButtonRed = DARK_BUTTON_RED
  else:
    bgColorFrame = BACKGROUND_LIGHT_FRAME
    fgColor = FG_COLOR_LIGHT
    bgColorButton = BACKGROUND_LIGHT_BUTTON
    fgColorButtonGreen = LIGHT_BUTTON_GREEN
    fgColorButtonRed = LIGHT_BUTTON_RED

  for frame in frames:
    frame.configure(bg=bgColorFrame)

  for label in labels:
    label.configure(bg=bgColorFrame, fg=fgColor)

  for button in infoButtons:
    button.configure(bg=bgColorFrame, fg=fgColor)
  for button in yesButtons:
    button.configure(bg=bgColorButton, fg=fgColorButtonGreen)

  for button in noButtons:
    button.configure(bg=bgColorButton, fg=fgColorButtonRed)


# turns on selected relays, called by pressing individual frame "ON" buttons
def relayON(frameNum, labelNum, image, relayNum):
  dbValues = c.execute("SELECT * FROM config").fetchone()
  confirm = dbValues[5]
  gpioa1Value = dbValues[0]
  gpiob1Value = dbValues[1]
  gpioa2Value = dbValues[2]
  gpiob2Value = dbValues[3]
  if (1 <= relayNum <= 8):
    if gpioa1Value & (1 << (relayNum - 1)):
      return
    else:
      if confirm < 2:
        confirmation = True
      else:
        if messagebox.askyesno("Confirm to energize relay", "Do you want energize the relay?"):
          confirmation = True
        else:
          confirmation = False
    if confirmation:
      newValue = gpioa1Value | (1 << (relayNum - 1))
      c.execute('UPDATE config SET gpioa1 = ' + str(newValue))
      # try:
      #   # bus.write_byte_data(address1, GPIOA, newValue)
      # except Exception as ex:
      #   print(ex)
        # print('An error occurred writing to:', hex(address1))
      print('GPIOA1 = ', newValue)
      image.configure(bg=IMG_BACKGROUND_GREEN)
  elif (9 <= relayNum <= 15):
    if gpiob1Value & (1 << (relayNum - 9)):
      return
    else:
      if confirm < 2:
        confirmation = True
      else:
        if messagebox.askyesno("Confirm to energize relay", "Do you want energize the relay?"):
          confirmation = True
        else:
          confirmation = False
    if confirmation:
      newValue = gpiob1Value | (1 << (relayNum - 9))
      c.execute('UPDATE config SET gpiob1 = ' + str(newValue))
      # try:
      #   # bus.write_byte_data(address1, GPIOB, newValue)
      # except Exception as ex:
      #   print(ex)
        # print('An error occurred writing to:', hex(address1))
      print('GPIOB1 = ', newValue)
      image.configure(bg=IMG_BACKGROUND_GREEN)
  elif (16 <= relayNum <= 23):
    if gpioa2Value & (1 << (relayNum - 16)):
      return
    else:
      if confirm < 2:
        confirmation = True
      else:
        if messagebox.askyesno("Confirm to energize relay", "Do you want energize the relay?"):
          confirmation = True
        else:
          confirmation = False
    if confirmation:
      newValue = gpioa2Value | (1 << (relayNum - 16))
      c.execute('UPDATE config SET gpioa2 = ' + str(newValue))
      # try:
      #   # bus.write_byte_data(address2, GPIOA, newValue)
      # except Exception as ex:
      #   print(ex)
        # print('An error occurred writing to:', hex(address2))
      print('GPIOA2 = ', newValue)
      image.configure(bg=IMG_BACKGROUND_GREEN)
  elif (24 <= relayNum <= 30):
    if gpiob2Value & (1 << (relayNum -24)):
      return
    else:
      if confirm < 2:
        confirmation = True
      else:
        if messagebox.askyesno("Confirm to energize relay", "Do you want energize the relay?"):
          confirmation = True
        else:
          confirmation = False
    if confirmation:
      newValue = gpiob2Value | (1 << (relayNum - 24))
      c.execute('UPDATE config SET gpiob2 = ' + str(newValue))
      # try:
      #   # bus.write_byte_data(address2, GPIOB, newValue)
      # except Exception as ex:
      #   print(ex)
        # print('An error occurred writing to:', hex(address2))
      print('GPIOB2 = ', newValue)
      image.configure(bg=IMG_BACKGROUND_GREEN)
  connection.commit()
  return


# turns off selected relays, called by pressing individual frame "OFF" buttons
def relayOFF(frameNum, labelNum, image, relayNum):
  dbValues = c.execute("SELECT * FROM config").fetchone()
  confirm = dbValues[5]
  gpioa1Value = dbValues[0]
  gpiob1Value = dbValues[1]
  gpioa2Value = dbValues[2]
  gpiob2Value = dbValues[3]
#  print((gpioa1Value >> (relayNum - 1)) & 1)
  if (1 <= relayNum <= 8):
    if (gpioa1Value >> (relayNum - 1)) & 1 == 0:
      return
    else:
      if confirm < 1:
        confirmation = True
      else:
        if messagebox.askyesno("Confirm to energize relay", "Do you want energize the relay?"):
          confirmation = True
        else:
          confirmation = False
    if confirmation:
      newValue =  gpioa1Value & ~(1 << (relayNum - 1))
      c.execute('UPDATE config SET gpioa1 = ' + str(newValue))
      # try:
      #   # bus.write_byte_data(address1, GPIOA, newValue)
      # except Exception as ex:
      #   print(ex)
        # print('An error occurred writing to:', hex(address1))
      print('GPIOA1 = ', newValue)
      image.configure(bg=IMG_BACKGROUND_RED)
  elif (9 <= relayNum <= 15):
    if (gpiob1Value >> (relayNum - 9)) & 1 == 0:
      return
    else:
      if confirm < 1:
        confirmation = True
      else:
        if messagebox.askyesno("Confirm to energize relay", "Do you want energize the relay?"):
          confirmation = True
        else:
          confirmation = False
    if confirmation:
      newValue = gpiob1Value & ~(1 << (relayNum - 9))
      c.execute('UPDATE config SET gpiob1 = ' + str(newValue))
      # try:
      #   # bus.write_byte_data(address1, GPIOB, newValue)
      # except Exception as ex:
      #   print(ex)
        # print('An error occurred writing to:', hex(address1))
      print('GPIOB1 = ', newValue)
      image.configure(bg=IMG_BACKGROUND_RED)
  elif (16 <= relayNum <= 23):
    if (gpioa2Value >> (relayNum - 16)) & 1 == 0:
      return
    else:
      if confirm < 1:
        confirmation = True
      else:
        if messagebox.askyesno("Confirm to energize relay", "Do you want energize the relay?"):
          confirmation = True
        else:
          confirmation = False
    if confirmation:
      newValue = gpioa2Value & ~(1 << (relayNum - 16))
      c.execute('UPDATE config SET gpioa2 = ' + str(newValue))
      # try:
      #   # bus.write_byte_data(address2, GPIOA, mcpValue)
      # except Exception as ex:
      #   print(ex)
        # print('An error occurred writing to:', hex(address2))
      print('GPIOA2 = ', newValue)
      image.configure(bg=IMG_BACKGROUND_RED)
  elif (24 <= relayNum <= 30):
    if (gpiob2Value >> (relayNum - 24)) & 1 == 0:
      return
    else:
      if confirm < 1:
        confirmation = True
      else:
        if messagebox.askyesno("Confirm to energize relay", "Do you want energize the relay?"):
          confirmation = True
        else:
          confirmation = False
    if confirmation:
      newValue = gpiob2Value & ~(1 << (relayNum - 24))
      c.execute('UPDATE config SET gpiob2 = ' + str(newValue))
      # try:
      #   # bus.write_byte_data(address2, GPIOB, mcpValue)
      # except Exception as ex:
      #   print(ex)
        # print('An error occurred writing to:', hex(address2))
      print('GPIOB2 = ', newValue)
      image.configure(bg=IMG_BACKGROUND_RED)
  connection.commit()
  return


# confirms terminating the app, and commits and closes db connection when "X" is clicked
def on_close():
  if messagebox.askyesno("Quit C by GE\u2122 Chernobyl Router Selector\u2122", "Do you want to exit the C by GE\u2122 Chernobyl Router Selector\u2122?"):
    connection.commit()
    connection.close()
    root.destroy()


# create the "Settings" and "Refresh" menu items
menu = Menu(root)
new_item = Menu(menu)
menu.add_command(label='Settings', command=createSettingsWindow)
# menu.add_command(label='Refresh', command=updateRoot)
root.config(menu=menu)


dbValues = c.execute("SELECT * FROM config").fetchone()
print(dbValues)
print(type(dbValues))
print('GPIOA1 = ', dbValues[0])
print('GPIOB1 = ', dbValues[1])
print('GPIOA2 = ', dbValues[2])
print('GPIOB2 = ', dbValues[3])
print()
print('Power Flag Status (has power failure outlasted UPS?) = ', dbValues[4])
print()
print('Confirmation Status = ', dbValues[5])
print('  0 = No Confirmation')
print('  1 = Conirm for OFF only')
print('  2 = Confirm for ON and OFF')
print()
print('Dark Mode Status = ', dbValues[6])
print()

_gpioa1 = dbValues[0]
_gpiob1 = dbValues[1]
_gpioa2 = dbValues[2]
_gpiob2 = dbValues[3]

powerFlag = dbValues[4]
darkMode = dbValues[6]


# if db power_flag = 1 reset all gpio values to 0x00
# print(type(powerFlag))
if powerFlag == 1:
  c.execute("UPDATE config SET gpioa1 = 0x00")
  c.execute("UPDATE config SET gpiob1 = 0x00")
  c.execute("UPDATE config SET gpioa2 = 0x00")
  c.execute("UPDATE config SET gpiob2 = 0x00")
  print(c.execute("SELECT * FROM config").fetchone())
  connection.commit()
# else:
#   try:
#     bus.write_byte_data(address1, GPIOA, _gpioa1)
#     bus.write_byte_data(address1, GPIOB, _gpiob1)
#   except Exception as ex:
#     print(ex)
#     print('An error occurred writing to:', hex(address1))
#   try:
#     bus.write_byte_data(address2, GPIOA, _gpioa2)
#     bus.write_byte_data(address2, GPIOB, _gpiob2)
#   except Exception as ex:
#     print(ex)
#     print('An error occurred writing to:', hex(address2))


# check db for dark mode and set colors appropriately
darkMode = c.execute("SELECT dark_mode FROM config").fetchone()[0]

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
  fgColor = FG_COLOR_LIGHT
  bgColorButton = BACKGROUND_LIGHT_BUTTON
  fgColorButtonGreen = LIGHT_BUTTON_GREEN
  fgColorButtonRed = LIGHT_BUTTON_RED


# frame specific configuration

if _gpioa1 & (1 << 0):
  bgColor = IMG_BACKGROUND_GREEN
else:
  bgColor = IMG_BACKGROUND_RED
frame1 = Frame(root, height=frameHeight, width=frameWidth, bd=borderWidth, bg=bgColorFrame, relief=borderStyle)
frame1.grid(column=0, row=0)

imgURL = routerInfo1['imageURL']
img1 = Image.open(imgURL)
if img1.mode != 'RGBA':
  img1.convert('RGBA')
  img1.putalpha(alpha)

img1 = img1.resize((frameWidth-100, frameHeight-65), Image.ANTIALIAS)
render1 = ImageTk.PhotoImage(img1)
image1 = Label(frame1, image=render1, bg=bgColor)
image1.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.2)

# infoImage = Image.open('./images/infoButton.png')
# if infoImage.mode != 'RGBA':
#   infoImage.convert('RGBA')
#   infoImage.putalpha(alpha)

# infoImage = infoImage.resize((20, 20), Image.ANTIALIAS)
# infoRender = ImageTk.PhotoImage(infoImage)
# infoLabel = Label(frame1, image=infoRender, bg='black').place(relx=infoBtnX, rely=infoBtnY)


myLabel1 = Label(frame1, text=routerInfo1['labelText'], bg=bgColorFrame, fg=fgColorFrame)
myLabel1.place(relwidth=0.9, relheight=0.2, relx=0.05)
infoButton1 = Button(frame1, text="  i  ", cursor="hand2", bg=bgColorFrame, fg=fgColorFrame, command=lambda: createInfoWindow(routerInfo1))
infoButton1.place(relx=infoBtnX, rely=infoBtnY)
yesButton1 = Button(frame1, text="ON", fg=fgColorButtonGreen, bg=bgColorButton, cursor='hand2', command=lambda: relayON(frame1, myLabel1, image1, 1))
yesButton1.place(relwidth=0.3, relheight=0.2, relx=0.15, rely=0.75)
noButton1 = Button(frame1, text="OFF",  fg=fgColorButtonRed, bg=bgColorButton, cursor='hand2', command=lambda: relayOFF(frame1, myLabel1, image1, 1))
noButton1.place(relwidth=0.3, relheight=0.2, relx=0.55, rely=0.75)


if _gpioa1 & (1 << 1):
  bgColor = IMG_BACKGROUND_GREEN
else:
  bgColor = IMG_BACKGROUND_RED
frame2 = Frame(root, height=frameHeight, width = frameWidth, bd=borderWidth, bg=bgColorFrame, relief=borderStyle)
frame2.grid(column=1, row=0)

imgURL = './images/Google_WiFi.jpg'
img2 = Image.open(imgURL)
if img2.mode != 'RGBA':
  img2.convert('RGBA')
  img2.putalpha(alpha)

img2 = img2.resize((frameWidth-100, frameHeight-65), Image.ANTIALIAS)
render2 = ImageTk.PhotoImage(img2)
image2 = Label(frame2, image=render2, bg=bgColor)
image2.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.2)

myLabel2 = Label(frame2, text='Google WiFi', bg=bgColorFrame, fg=fgColorFrame)
myLabel2.place(relwidth=0.9, relheight=0.2, relx=0.05)
infoButton2 = Button(frame2, text="  i  ", cursor="hand2", bg=bgColorFrame, fg=fgColorFrame, command=lambda: createInfoWindow(frame2))
infoButton2.place(relx=infoBtnX, rely=infoBtnY)
yesButton2 = Button(frame2, text="ON", fg=fgColorButtonGreen, bg=bgColorButton, cursor='hand2', command=lambda: relayON(frame2, myLabel2, image2, 2))
yesButton2.place(relwidth=0.3, relheight=0.2, relx=0.15, rely=0.75)
noButton2 = Button(frame2, text="OFF", fg=fgColorButtonRed, bg=bgColorButton, cursor='hand2', command=lambda: relayOFF(frame2, myLabel2, image2, 2))
noButton2.place(relwidth=0.3, relheight=0.2, relx=0.55, rely=0.75)


if _gpioa1 & (1 << 2):
  bgColor = IMG_BACKGROUND_GREEN
else:
  bgColor = IMG_BACKGROUND_RED
frame3 = Frame(root, height=frameHeight, width = frameWidth, bd=borderWidth, bg=bgColorFrame, relief=borderStyle)
frame3.grid(column=2, row=0)

imgURL = './images/TP_Link_Archer_C7_AC1750.jpg'
img3 = Image.open(imgURL)
if img3.mode != 'RGBA':
  img3.convert('RGBA')
  img3.putalpha(alpha)

img3 = img3.resize((frameWidth-100, frameHeight-65), Image.ANTIALIAS)
render3 = ImageTk.PhotoImage(img3)
image3 = Label(frame3, image=render3, bg=bgColor)
image3.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.2)

myLabel3 = Label(frame3, text='TP Link Archer C7 AC1750', bg=bgColorFrame, fg=fgColorFrame)
myLabel3.place(relwidth=0.9, relheight=0.2, relx=0.05)
infoButton3 = Button(frame3, text="  i  ", cursor="hand2", bg=bgColorFrame, fg=fgColorFrame, command=lambda: createInfoWindow(frame3))
infoButton3.place(relx=infoBtnX, rely=infoBtnY)
yesButton3 = Button(frame3, text="ON", fg=fgColorButtonGreen, bg=bgColorButton, cursor='hand2', command=lambda: relayON(frame3, myLabel3, image3, 3))
yesButton3.place(relwidth=0.3, relheight=0.2, relx=0.15, rely=0.75)
noButton3 = Button(frame3, text="OFF", fg=fgColorButtonRed, bg=bgColorButton, cursor='hand2', command=lambda: relayOFF(frame3, myLabel3, image3, 3))
noButton3.place(relwidth=0.3, relheight=0.2, relx=0.55, rely=0.75)


if _gpioa1 & (1 << 3):
  bgColor = IMG_BACKGROUND_GREEN
else:
  bgColor = IMG_BACKGROUND_RED
frame4 = Frame(root, height=frameHeight, width = frameWidth, bd=borderWidth, bg=bgColorFrame, relief=borderStyle)
frame4.grid(column=3, row=0)

imgURL = './images/eero_WiFi.jpg'
img4 = Image.open(imgURL)
if img4.mode != 'RGBA':
  img4.convert('RGBA')
  img4.putalpha(alpha)

img4 = img4.resize((frameWidth-100, frameHeight-65), Image.ANTIALIAS)
render4 = ImageTk.PhotoImage(img4)
image4 = Label(frame4, image=render4, bg=bgColor)
image4.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.2)

myLabel4 = Label(frame4, text='eero Pro Mesh WiFi', bg=bgColorFrame, fg=fgColorFrame)
myLabel4.place(relwidth=0.9, relheight=0.2, relx=0.05)
infoButton4 = Button(frame4, text="  i  ", cursor="hand2", bg=bgColorFrame, fg=fgColorFrame, command=lambda: createInfoWindow(frame4))
infoButton4.place(relx=infoBtnX, rely=infoBtnY)
yesButton4 = Button(frame4, text="ON", fg=fgColorButtonGreen, bg=bgColorButton, cursor='hand2', command=lambda: relayON(frame4, myLabel4, image4, 4))
yesButton4.place(relwidth=0.3, relheight=0.2, relx=0.15, rely=0.75)
noButton4 = Button(frame4, text="OFF", fg=fgColorButtonRed, bg=bgColorButton, cursor='hand2', command=lambda: relayOFF(frame4, myLabel4, image4, 4))
noButton4.place(relwidth=0.3, relheight=0.2, relx=0.55, rely=0.75)


if _gpioa1 & (1 << 4):
  bgColor = IMG_BACKGROUND_GREEN
else:
  bgColor = IMG_BACKGROUND_RED
frame5 = Frame(root, height=frameHeight, width = frameWidth, bd=borderWidth, bg=bgColorFrame, relief=borderStyle)
frame5.grid(column=4, row=0)

imgURL = './images/TP_Link_Archer_C50_AC1200.jpg'
img5 = Image.open(imgURL)
if img5.mode != 'RGBA':
  img5.convert('RGBA')
  img5.putalpha(alpha)

img5 = img5.resize((frameWidth-100, frameHeight-65), Image.ANTIALIAS)
render5 = ImageTk.PhotoImage(img5)
image5 = Label(frame5, image=render5, bg=bgColor)
image5.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.2)

myLabel5 = Label(frame5, text='TP Link Archer C50 AC1200', bg=bgColorFrame, fg=fgColorFrame)
myLabel5.place(relwidth=0.9, relheight=0.2, relx=0.05)
infoButton5 = Button(frame5, text="  i  ", cursor="hand2", bg=bgColorFrame, fg=fgColorFrame, command=lambda: createInfoWindow(frame5))
infoButton5.place(relx=infoBtnX, rely=infoBtnY)
yesButton5 = Button(frame5, text="ON", fg=fgColorButtonGreen, bg=bgColorButton, cursor='hand2', command=lambda: relayON(frame5, myLabel5, image5, 5))
yesButton5.place(relwidth=0.3, relheight=0.2, relx=0.15, rely=0.75)
noButton5 = Button(frame5, text="OFF", fg=fgColorButtonRed, bg=bgColorButton, cursor='hand2', command=lambda: relayOFF(frame5, myLabel5, image5, 5))
noButton5.place(relwidth=0.3, relheight=0.2, relx=0.55, rely=0.75)


if _gpioa1 & (1 << 5):
  bgColor = IMG_BACKGROUND_GREEN
else:
  bgColor = IMG_BACKGROUND_RED
frame6 = Frame(root, height=frameHeight, width = frameWidth, bd=borderWidth, bg=bgColorFrame, relief=borderStyle)
frame6.grid(column=5, row=0)

imgURL = './images/Netgear_Nighthawk_X6S.jpg'
img6 = Image.open(imgURL)
if img6.mode != 'RGBA':
  img6.convert('RGBA')
  img6.putalpha(alpha)

img6 = img6.resize((frameWidth-100, frameHeight-65), Image.ANTIALIAS)
render6 = ImageTk.PhotoImage(img6)
image6 = Label(frame6, image=render6, bg=bgColor)
image6.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.2)

myLabel6 = Label(frame6, text='Netgear Nighthawk X6S', bg=bgColorFrame, fg=fgColorFrame)
myLabel6.place(relwidth=0.9, relheight=0.2, relx=0.05)
infoButton6 = Button(frame6, text="  i  ", cursor="hand2", bg=bgColorFrame, fg=fgColorFrame, command=lambda: createInfoWindow(frame6))
infoButton6.place(relx=infoBtnX, rely=infoBtnY)
yesButton6 = Button(frame6, text="ON", fg=fgColorButtonGreen, bg=bgColorButton, cursor='hand2', command=lambda: relayON(frame6, myLabel6, image6, 6))
yesButton6.place(relwidth=0.3, relheight=0.2, relx=0.15, rely=0.75)
noButton6 = Button(frame6, text="OFF", fg=fgColorButtonRed, bg=bgColorButton, cursor='hand2', command=lambda: relayOFF(frame6, myLabel6, image6, 6))
noButton6.place(relwidth=0.3, relheight=0.2, relx=0.55, rely=0.75)


if _gpioa1 & (1 << 6):
  bgColor = IMG_BACKGROUND_GREEN
else:
  bgColor = IMG_BACKGROUND_RED
frame7 = Frame(root, height=frameHeight, width = frameWidth, bd=borderWidth, bg=bgColorFrame, relief=borderStyle)
frame7.grid(column=0, row=1)

imgURL = './images/TP_Link_Archer_CR700_AC1750.jpg'
img7 = Image.open(imgURL)
if img7.mode != 'RGBA':
  img7.convert('RGBA')
  img7.putalpha(alpha)

img7 = img7.resize((frameWidth-100, frameHeight-65), Image.ANTIALIAS)
render7 = ImageTk.PhotoImage(img7)
image7 = Label(frame7, image=render7, bg=bgColor)
image7.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.2)

myLabel7 = Label(frame7, text='TP Link Archer CR700 AC1750', bg=bgColorFrame, fg=fgColorFrame)
myLabel7.place(relwidth=0.9, relheight=0.2, relx=0.05)
infoButton7 = Button(frame7, text="  i  ", cursor="hand2", bg=bgColorFrame, fg=fgColorFrame, command=lambda: createInfoWindow(frame7))
infoButton7.place(relx=infoBtnX, rely=infoBtnY)
yesButton7 = Button(frame7, text="ON", fg=fgColorButtonGreen, bg=bgColorButton, cursor='hand2', command=lambda: relayON(frame7, myLabel7, image7, 7))
yesButton7.place(relwidth=0.3, relheight=0.2, relx=0.15, rely=0.75)
noButton7 = Button(frame7, text="OFF", fg=fgColorButtonRed, bg=bgColorButton, cursor='hand2', command=lambda: relayOFF(frame7, myLabel7, image7, 7))
noButton7.place(relwidth=0.3, relheight=0.2, relx=0.55, rely=0.75)


if _gpioa1 & (1 << 7):
  bgColor = IMG_BACKGROUND_GREEN
else:
  bgColor = IMG_BACKGROUND_RED
frame8 = Frame(root, height=frameHeight, width = frameWidth, bd=borderWidth, bg=bgColorFrame, relief=borderStyle)
frame8.grid(column=1, row=1)

imgURL = './images/Linksys_AC1900_EA7500.jpg'
img8 = Image.open(imgURL)
if img8.mode != 'RGBA':
  img8.convert('RGBA')
  img8.putalpha(alpha)

img8 = img8.resize((frameWidth-100, frameHeight-65), Image.ANTIALIAS)
render8 = ImageTk.PhotoImage(img8)
image8 = Label(frame8, image=render8, bg=bgColor)
image8.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.2)

myLabel8 = Label(frame8, text='Linksys EA7500 AC1900', bg=bgColorFrame, fg=fgColorFrame)
myLabel8.place(relwidth=0.9, relheight=0.2, relx=0.05)
infoButton8 = Button(frame8, text="  i  ", cursor="hand2", bg=bgColorFrame, fg=fgColorFrame, command=lambda: createInfoWindow(frame8))
infoButton8.place(relx=infoBtnX, rely=infoBtnY)
yesButton8 = Button(frame8, text="ON", fg=fgColorButtonGreen, bg=bgColorButton, cursor='hand2', command=lambda: relayON(frame8, myLabel8, image8, 8))
yesButton8.place(relwidth=0.3, relheight=0.2, relx=0.15, rely=0.75)
noButton8 = Button(frame8, text="OFF", fg=fgColorButtonRed, bg=bgColorButton, cursor='hand2', command=lambda: relayOFF(frame8, myLabel8, image8, 8))
noButton8.place(relwidth=0.3, relheight=0.2, relx=0.55, rely=0.75)


if _gpiob1 & (1 << 0):
  bgColor = IMG_BACKGROUND_GREEN
else:
  bgColor = IMG_BACKGROUND_RED
frame9 = Frame(root, height=frameHeight, width = frameWidth, bd=borderWidth, bg=bgColorFrame, relief=borderStyle)
frame9.grid(column=2, row=1)

imgURL = './images/Netgear_Nighthawk_AC3200.jpg'
img9 = Image.open(imgURL)
if img9.mode != 'RGBA':
  img9.convert('RGBA')
  img9.putalpha(alpha)

img9 = img9.resize((frameWidth-100, frameHeight-65), Image.ANTIALIAS)
render9 = ImageTk.PhotoImage(img9)
image9 = Label(frame9, image=render9, bg=bgColor)
image9.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.2)

myLabel9 = Label(frame9, text='Netgear Nighthawk X6 AC3200', bg=bgColorFrame, fg=fgColorFrame)
myLabel9.place(relwidth=0.9, relheight=0.2, relx=0.05)
infoButton9 = Button(frame9, text="  i  ", cursor="hand2", bg=bgColorFrame, fg=fgColorFrame, command=lambda: createInfoWindow(frame9))
infoButton9.place(relx=infoBtnX, rely=infoBtnY)
yesButton9 = Button(frame9, text="ON", fg=fgColorButtonGreen, bg=bgColorButton, cursor='hand2', command=lambda: relayON(frame9, myLabel9, image9, 9))
yesButton9.place(relwidth=0.3, relheight=0.2, relx=0.15, rely=0.75)
noButton9 = Button(frame9, text="OFF", fg=fgColorButtonRed, bg=bgColorButton, cursor='hand2', command=lambda: relayOFF(frame9, myLabel9, image9, 9))
noButton9.place(relwidth=0.3, relheight=0.2, relx=0.55, rely=0.75)


if _gpiob1 & (1 << 1):
  bgColor = IMG_BACKGROUND_GREEN
else:
  bgColor = IMG_BACKGROUND_RED
frame10 = Frame(root, height=frameHeight, width = frameWidth, bd=borderWidth, bg=bgColorFrame, relief=borderStyle)
frame10.grid(column=3, row=1)

imgURL = './images/TP_Link_Archer_C90_AC1900.jpg'
img10 = Image.open(imgURL)
if img10.mode != 'RGBA':
  img10.convert('RGBA')
  img10.putalpha(alpha)

img10 = img10.resize((frameWidth-100, frameHeight-65), Image.ANTIALIAS)
render10 = ImageTk.PhotoImage(img10)
image10 = Label(frame10, image=render10, bg=bgColor)
image10.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.2)

myLabel10 = Label(frame10, text='TP Link Archer C90 AC1900', bg=bgColorFrame, fg=fgColorFrame)
myLabel10.place(relwidth=0.9, relheight=0.2, relx=0.05)
infoButton10 = Button(frame10, text="  i  ", cursor="hand2", bg=bgColorFrame, fg=fgColorFrame, command=lambda: createInfoWindow(frame10))
infoButton10.place(relx=infoBtnX, rely=infoBtnY)
yesButton10 = Button(frame10, text="ON", fg=fgColorButtonGreen, bg=bgColorButton, cursor='hand2', command=lambda: relayON(frame10, myLabel10, image10, 10))
yesButton10.place(relwidth=0.3, relheight=0.2, relx=0.15, rely=0.75)
noButton10 = Button(frame10, text="OFF", fg=fgColorButtonRed, bg=bgColorButton, cursor='hand2', command=lambda: relayOFF(frame10, myLabel10, image10, 10))
noButton10.place(relwidth=0.3, relheight=0.2, relx=0.55, rely=0.75)


if _gpiob1 & (1 << 2):
  bgColor = IMG_BACKGROUND_GREEN
else:
  bgColor = IMG_BACKGROUND_RED
frame11 = Frame(root, height=frameHeight, width = frameWidth, bd=borderWidth, bg=bgColorFrame, relief=borderStyle)
frame11.grid(column=4, row=1)

imgURL = './images/Netgear_Nighthawk_AX8.jpg'
img11 = Image.open(imgURL)
if img11.mode != 'RGBA':
  img11.convert('RGBA')
  img11.putalpha(alpha)

img11 = img11.resize((frameWidth-100, frameHeight-65), Image.ANTIALIAS)
render11 = ImageTk.PhotoImage(img11)
image11 = Label(frame11, image=render11, bg=bgColor)
image11.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.2)

myLabel11 = Label(frame11, text='Netgear Nighthawk AX8', bg=bgColorFrame, fg=fgColorFrame)
myLabel11.place(relwidth=0.9, relheight=0.2, relx=0.05)
infoButton11 = Button(frame11, text="  i  ", cursor="hand2", bg=bgColorFrame, fg=fgColorFrame, command=lambda: createInfoWindow(frame11))
infoButton11.place(relx=infoBtnX, rely=infoBtnY)
yesButton11 = Button(frame11, text="ON", fg=fgColorButtonGreen, bg=bgColorButton, cursor='hand2', command=lambda: relayON(frame11, myLabel11, image11, 11))
yesButton11.place(relwidth=0.3, relheight=0.2, relx=0.15, rely=0.75)
noButton11 = Button(frame11, text="OFF", fg=fgColorButtonRed, bg=bgColorButton, cursor='hand2', command=lambda: relayOFF(frame11, myLabel11, image11, 11))
noButton11.place(relwidth=0.3, relheight=0.2, relx=0.55, rely=0.75)


if _gpiob1 & (1 << 3):
  bgColor = IMG_BACKGROUND_GREEN
else:
  bgColor = IMG_BACKGROUND_RED
frame12 = Frame(root, height=frameHeight, width = frameWidth, bd=borderWidth, bg=bgColorFrame, relief=borderStyle)
frame12.grid(column=5, row=1)

imgURL = './images/Netgear_Nighthawk_AC1900.jpg'
img12 = Image.open(imgURL)
if img12.mode != 'RGBA':
  img12.convert('RGBA')
  img12.putalpha(alpha)

img12 = img12.resize((frameWidth-100, frameHeight-65), Image.ANTIALIAS)
render12 = ImageTk.PhotoImage(img12)
image12 = Label(frame12, image=render12, bg=bgColor)
image12.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.2)

myLabel12 = Label(frame12, text='Netgear Nighthawk AC1900', bg=bgColorFrame, fg=fgColorFrame)
myLabel12.place(relwidth=0.9, relheight=0.2, relx=0.05)
infoButton12 = Button(frame12, text="  i  ", cursor="hand2", bg=bgColorFrame, fg=fgColorFrame, command=lambda: createInfoWindow(frame12))
infoButton12.place(relx=infoBtnX, rely=infoBtnY)
yesButton12 = Button(frame12, text="ON", fg=fgColorButtonGreen, bg=bgColorButton, cursor='hand2', command=lambda: relayON(frame12, myLabel12, image12, 12))
yesButton12.place(relwidth=0.3, relheight=0.2, relx=0.15, rely=0.75)
noButton12 = Button(frame12, text="OFF", fg=fgColorButtonRed, bg=bgColorButton, cursor='hand2', command=lambda: relayOFF(frame12, myLabel12, image12, 12))
noButton12.place(relwidth=0.3, relheight=0.2, relx=0.55, rely=0.75)


if _gpiob1 & (1 << 4):
  bgColor = IMG_BACKGROUND_GREEN
else:
  bgColor = IMG_BACKGROUND_RED
frame13 = Frame(root, height=frameHeight, width = frameWidth, bd=borderWidth, bg=bgColorFrame, relief=borderStyle)
frame13.grid(column=0, row=2)

imgURL = './images/Cisco_RV320K9NA.jpg'
img13 = Image.open(imgURL)
if img13.mode != 'RGBA':
  img13.convert('RGBA')
  img13.putalpha(alpha)

img13 = img13.resize((frameWidth-100, frameHeight-65), Image.ANTIALIAS)
render13 = ImageTk.PhotoImage(img13)
image13 = Label(frame13, image=render13, bg=bgColor)
image13.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.2)

myLabel13 = Label(frame13, text='Cisco RV320 Dual WAN VPN Router', bg=bgColorFrame, fg=fgColorFrame)
myLabel13.place(relwidth=0.9, relheight=0.2, relx=0.05)
infoButton13 = Button(frame13, text="  i  ", cursor="hand2", bg=bgColorFrame, fg=fgColorFrame, command=lambda: createInfoWindow(frame13))
infoButton13.place(relx=infoBtnX, rely=infoBtnY)
yesButton13 = Button(frame13, text="ON", fg=fgColorButtonGreen, bg=bgColorButton, cursor='hand2', command=lambda: relayON(frame13, myLabel13, image13, 13))
yesButton13.place(relwidth=0.3, relheight=0.2, relx=0.15, rely=0.75)
noButton13 = Button(frame13, text="OFF", fg=fgColorButtonRed, bg=bgColorButton, cursor='hand2', command=lambda: relayOFF(frame13, myLabel13, image13, 13))
noButton13.place(relwidth=0.3, relheight=0.2, relx=0.55, rely=0.75)


if _gpiob1 & (1 << 5):
  bgColor = IMG_BACKGROUND_GREEN
else:
  bgColor = IMG_BACKGROUND_RED
frame14 = Frame(root, height=frameHeight, width=frameWidth, bd=borderWidth, bg=bgColorFrame, relief=borderStyle)
frame14.grid(column=1, row=2)

imgURL = './images/Spectrum_Netgear_N600_WNDR3800-100NAS.jpg'
img14 = Image.open(imgURL)
if img14.mode != 'RGBA':
  img14.convert('RGBA')
  img14.putalpha(alpha)

img14 = img14.resize((frameWidth-100, frameHeight-65), Image.ANTIALIAS)
render14 = ImageTk.PhotoImage(img14)
image14 = Label(frame14, image=render14, bg=bgColor)
image14.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.2)

myLabel14 = Label(frame14, text='Spectrum Netgear N600 WNDR3800', bg=bgColorFrame, fg=fgColorFrame)
myLabel14.place(relwidth=0.9, relheight=0.2, relx=0.05)
infoButton14 = Button(frame14, text="  i  ", cursor="hand2", bg=bgColorFrame, fg=fgColorFrame, command=lambda: createInfoWindow(frame14))
infoButton14.place(relx=infoBtnX, rely=infoBtnY)
yesButton14 = Button(frame14, text="ON", fg=fgColorButtonGreen, bg=bgColorButton, cursor='hand2', command=lambda: relayON(frame14, myLabel14, image14, 14))
yesButton14.place(relwidth=0.3, relheight=0.2, relx=0.15, rely=0.75)
noButton14 = Button(frame14, text="OFF", fg=fgColorButtonRed, bg=bgColorButton, cursor='hand2', command=lambda: relayOFF(frame14, myLabel14, image14, 14))
noButton14.place(relwidth=0.3, relheight=0.2, relx=0.55, rely=0.75)


if _gpiob1 & (1 << 6):
  bgColor = IMG_BACKGROUND_GREEN
else:
  bgColor = IMG_BACKGROUND_RED
frame15 = Frame(root, height=frameHeight, width = frameWidth, bd=borderWidth, bg=bgColorFrame, relief=borderStyle)
frame15.grid(column=2, row=2)

imgURL = './images/Spectrum_Technicolor_TC4400.jpg'
img15 = Image.open(imgURL)
if img15.mode != 'RGBA':
  img15.convert('RGBA')
  img15.putalpha(alpha)

img15 = img15.resize((frameWidth-100, frameHeight-65), Image.ANTIALIAS)
render15 = ImageTk.PhotoImage(img15)
image15 = Label(frame15, image=render15, bg=bgColor)
image15.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.2)

myLabel15 = Label(frame15, text='Spectrum Technicolor TC4400', bg=bgColorFrame, fg=fgColorFrame)
myLabel15.place(relwidth=0.9, relheight=0.2, relx=0.05)
infoButton15 = Button(frame15, text="  i  ", cursor="hand2", bg=bgColorFrame, fg=fgColorFrame, command=lambda: createInfoWindow(frame15))
infoButton15.place(relx=infoBtnX, rely=infoBtnY)
yesButton15 = Button(frame15, text="ON", fg=fgColorButtonGreen, bg=bgColorButton, cursor='hand2', command=lambda: relayON(frame15, myLabel15, image15, 15))
yesButton15.place(relwidth=0.3, relheight=0.2, relx=0.15, rely=0.75)
noButton15 = Button(frame15, text="OFF", fg=fgColorButtonRed, bg=bgColorButton, cursor='hand2', command=lambda: relayOFF(frame15, myLabel15, image15, 15))
noButton15.place(relwidth=0.3, relheight=0.2, relx=0.55, rely=0.75)


if _gpioa2 & (1 << 0):
  bgColor = IMG_BACKGROUND_GREEN
else:
  bgColor = IMG_BACKGROUND_RED
frame16 = Frame(root, height=frameHeight, width = frameWidth, bd=borderWidth, bg=bgColorFrame, relief=borderStyle)
frame16.grid(column=3, row=2)

imgURL = './images/Spectrum_Netgear_R6300-100PAS.jpg'
img16 = Image.open(imgURL)
if img16.mode != 'RGBA':
  img16.convert('RGBA')
  img16.putalpha(alpha)

img16 = img16.resize((frameWidth-100, frameHeight-65), Image.ANTIALIAS)
render16 = ImageTk.PhotoImage(img16)
image16 = Label(frame16, image=render16, bg=bgColor)
image16.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.2)

myLabel16 = Label(frame16, text='Spectrum Netgear R6300v2', bg=bgColorFrame, fg=fgColorFrame)
myLabel16.place(relwidth=0.9, relheight=0.2, relx=0.05)
infoButton16 = Button(frame16, text="  i  ", cursor="hand2", bg=bgColorFrame, fg=fgColorFrame, command=lambda: createInfoWindow(frame16))
infoButton16.place(relx=infoBtnX, rely=infoBtnY)
yesButton16 = Button(frame16, text="ON", fg=fgColorButtonGreen, bg=bgColorButton, cursor='hand2', command=lambda: relayON(frame16, myLabel16, image16, 16))
yesButton16.place(relwidth=0.3, relheight=0.2, relx=0.15, rely=0.75)
noButton16 = Button(frame16, text="OFF", fg=fgColorButtonRed, bg=bgColorButton, cursor='hand2', command=lambda: relayOFF(frame16, myLabel16, image16, 16))
noButton16.place(relwidth=0.3, relheight=0.2, relx=0.55, rely=0.75)


if _gpioa2 & (1 << 1):
  bgColor = IMG_BACKGROUND_GREEN
else:
  bgColor = IMG_BACKGROUND_RED
frame17 = Frame(root, height=frameHeight, width = frameWidth, bd=borderWidth, bg=bgColorFrame, relief=borderStyle)
frame17.grid(column=4, row=2)

imgURL = './images/Spectrum_Wave_2_RAC2V1S.jpg'
img17 = Image.open(imgURL)
if img17.mode != 'RGBA':
  img17.convert('RGBA')
  img17.putalpha(alpha)

img17 = img17.resize((frameWidth-100, frameHeight-65), Image.ANTIALIAS)
render17 = ImageTk.PhotoImage(img17)
image17 = Label(frame17, image=render17, bg=bgColor)
image17.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.2)

myLabel17 = Label(frame17, text='Spectrum Wave 2 RAC2V1S', bg=bgColorFrame, fg=fgColorFrame)
myLabel17.place(relwidth=0.9, relheight=0.2, relx=0.05)
infoButton17 = Button(frame17, text="  i  ", cursor="hand2", bg=bgColorFrame, fg=fgColorFrame, command=lambda: createInfoWindow(frame17))
infoButton17.place(relx=infoBtnX, rely=infoBtnY)
yesButton17 = Button(frame17, text="ON", fg=fgColorButtonGreen, bg=bgColorButton, cursor='hand2', command=lambda: relayON(frame17, myLabel17, image17, 17))
yesButton17.place(relwidth=0.3, relheight=0.2, relx=0.15, rely=0.75)
noButton17 = Button(frame17, text="OFF", fg=fgColorButtonRed, bg=bgColorButton, cursor='hand2', command=lambda: relayOFF(frame17, myLabel17, image17, 17))
noButton17.place(relwidth=0.3, relheight=0.2, relx=0.55, rely=0.75)


if _gpioa2 & (1 << 2):
  bgColor = IMG_BACKGROUND_GREEN
else:
  bgColor = IMG_BACKGROUND_RED
frame18 = Frame(root, height=frameHeight, width = frameWidth, bd=borderWidth, bg=bgColorFrame, relief=borderStyle)
frame18.grid(column=5, row=2)

imgURL = './images/Cisco_RV325K9NA.jpg'
img18 = Image.open(imgURL)
if img18.mode != 'RGBA':
  img18.convert('RGBA')
  img18.putalpha(alpha)

img18 = img18.resize((frameWidth-100, frameHeight-65), Image.ANTIALIAS)
render18 = ImageTk.PhotoImage(img18)
image18 = Label(frame18, image=render18, bg=bgColor)
image18.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.2)

myLabel18 = Label(frame18, text='Cisco RV325 Dual WAN VPN Router', bg=bgColorFrame, fg=fgColorFrame)
myLabel18.place(relwidth=0.9, relheight=0.2, relx=0.05)
infoButton18 = Button(frame18, text="  i  ", cursor="hand2", bg=bgColorFrame, fg=fgColorFrame, command=lambda: createInfoWindow(frame18))
infoButton18.place(relx=infoBtnX, rely=infoBtnY)
yesButton18 = Button(frame18, text="ON", fg=fgColorButtonGreen, bg=bgColorButton, cursor='hand2', command=lambda: relayON(frame18, myLabel18, image18, 18))
yesButton18.place(relwidth=0.3, relheight=0.2, relx=0.15, rely=0.75)
noButton18 = Button(frame18, text="OFF", fg=fgColorButtonRed, bg=bgColorButton, cursor='hand2', command=lambda: relayOFF(frame18, myLabel18, image18, 18))
noButton18.place(relwidth=0.3, relheight=0.2, relx=0.55, rely=0.75)


if _gpioa2 & (1 << 3):
  bgColor = IMG_BACKGROUND_GREEN
else:
  bgColor = IMG_BACKGROUND_RED
frame19 = Frame(root, height=frameHeight, width = frameWidth, bd=borderWidth, bg=bgColorFrame, relief=borderStyle)
frame19.grid(column=0, row=3)

imgURL = './images/C_by_GE_logo.jpg'
img19 = Image.open(imgURL)
if img19.mode != 'RGBA':
  img19.convert('RGBA')
  img19.putalpha(alpha)

img19 = img19.resize((frameWidth-100, frameHeight-65), Image.ANTIALIAS)
render19 = ImageTk.PhotoImage(img19)
image19 = Label(frame19, image=render19, bg=bgColor)
image19.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.2)

myLabel19 = Label(frame19, text='', bg=bgColorFrame, fg=fgColorFrame)
myLabel19.place(relwidth=0.9, relheight=0.2, relx=0.05)
infoButton19 = Button(frame19, text="  i  ", cursor="hand2", bg=bgColorFrame, fg=fgColorFrame, command=lambda: createInfoWindow(frame19))
infoButton19.place(relx=infoBtnX, rely=infoBtnY)
yesButton19 = Button(frame19, text="ON", fg=fgColorButtonGreen, bg=bgColorButton, cursor='hand2', command=lambda: relayON(frame19, myLabel19, image19, 19))
yesButton19.place(relwidth=0.3, relheight=0.2, relx=0.15, rely=0.75)
noButton19 = Button(frame19, text="OFF", fg=fgColorButtonRed, bg=bgColorButton, cursor='hand2', command=lambda: relayOFF(frame19, myLabel19, image19, 19))
noButton19.place(relwidth=0.3, relheight=0.2, relx=0.55, rely=0.75)


if _gpioa2 & (1 << 4):
  bgColor = IMG_BACKGROUND_GREEN
else:
  bgColor = IMG_BACKGROUND_RED
frame20 = Frame(root, height=frameHeight, width = frameWidth, bd=borderWidth, bg=bgColorFrame, relief=borderStyle)
frame20.grid(column=1, row=3)

imgURL = './images/GE_logo.jpg'
img20 = Image.open(imgURL)
if img20.mode != 'RGBA':
  img20.convert('RGBA')
  img20.putalpha(alpha)

img20 = img20.resize((frameWidth-100, frameHeight-65), Image.ANTIALIAS)
render20 = ImageTk.PhotoImage(img20)
image20 = Label(frame20, image=render20, bg=bgColor)
image20.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.2)

myLabel20 = Label(frame20, text='', bg=bgColorFrame, fg=fgColorFrame)
myLabel20.place(relwidth=0.9, relheight=0.2, relx=0.05)
infoButton20 = Button(frame20, text="  i  ", cursor="hand2", bg=bgColorFrame, fg=fgColorFrame, command=lambda: createInfoWindow(frame20))
infoButton20.place(relx=infoBtnX, rely=infoBtnY)
yesButton20 = Button(frame20, text="ON", fg=fgColorButtonGreen, bg=bgColorButton, cursor='hand2', command=lambda: relayON(frame20, myLabel20, image20, 20))
yesButton20.place(relwidth=0.3, relheight=0.2, relx=0.15, rely=0.75)
noButton20 = Button(frame20, text="OFF", fg=fgColorButtonRed, bg=bgColorButton, cursor='hand2', command=lambda: relayOFF(frame20, myLabel20, image20, 20))
noButton20.place(relwidth=0.3, relheight=0.2, relx=0.55, rely=0.75)


if _gpioa2 & (1 << 5):
  bgColor = IMG_BACKGROUND_GREEN
else:
  bgColor = IMG_BACKGROUND_RED
frame21 = Frame(root, height=frameHeight, width = frameWidth, bd=borderWidth, bg=bgColorFrame, relief=borderStyle)
frame21.grid(column=2, row=3)

imgURL = './images/C_by_GE_logo.jpg'
img21 = Image.open(imgURL)
if img21.mode != 'RGBA':
  img21.convert('RGBA')
  img21.putalpha(alpha)

img21 = img21.resize((frameWidth-100, frameHeight-65), Image.ANTIALIAS)
render21 = ImageTk.PhotoImage(img21)
image21 = Label(frame21, image=render21, bg=bgColor)
image21.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.2)

myLabel21 = Label(frame21, text='', bg=bgColorFrame, fg=fgColorFrame)
myLabel21.place(relwidth=0.9, relheight=0.2, relx=0.05)
infoButton21 = Button(frame21, text="  i  ", cursor="hand2", bg=bgColorFrame, fg=fgColorFrame, command=lambda: createInfoWindow(frame21))
infoButton21.place(relx=infoBtnX, rely=infoBtnY)
yesButton21 = Button(frame21, text="ON", fg=fgColorButtonGreen, bg=bgColorButton, cursor='hand2', command=lambda: relayON(frame21, myLabel21, image21, 21))
yesButton21.place(relwidth=0.3, relheight=0.2, relx=0.15, rely=0.75)
noButton21 = Button(frame21, text="OFF", fg=fgColorButtonRed, bg=bgColorButton, cursor='hand2', command=lambda: relayOFF(frame21, myLabel21, image21, 21))
noButton21.place(relwidth=0.3, relheight=0.2, relx=0.55, rely=0.75)


if _gpioa2 & (1 << 6):
  bgColor = IMG_BACKGROUND_GREEN
else:
  bgColor = IMG_BACKGROUND_RED
frame22 = Frame(root, height=frameHeight, width = frameWidth, bd=borderWidth, bg=bgColorFrame, relief=borderStyle)
frame22.grid(column=3, row=3)

imgURL = './images/GE_logo.jpg'
img22 = Image.open(imgURL)
if img22.mode != 'RGBA':
  img22.convert('RGBA')
  img22.putalpha(alpha)

img22 = img22.resize((frameWidth-100, frameHeight-65), Image.ANTIALIAS)
render22 = ImageTk.PhotoImage(img22)
image22 = Label(frame22, image=render22, bg=bgColor)
image22.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.2)

myLabel22 = Label(frame22, text='', bg=bgColorFrame, fg=fgColorFrame)
myLabel22.place(relwidth=0.9, relheight=0.2, relx=0.05)
infoButton22 = Button(frame22, text="  i  ", cursor="hand2", bg=bgColorFrame, fg=fgColorFrame, command=lambda: createInfoWindow(frame22))
infoButton22.place(relx=infoBtnX, rely=infoBtnY)
yesButton22 = Button(frame22, text="ON", fg=fgColorButtonGreen, bg=bgColorButton, cursor='hand2', command=lambda: relayON(frame22, myLabel22, image22, 22))
yesButton22.place(relwidth=0.3, relheight=0.2, relx=0.15, rely=0.75)
noButton22 = Button(frame22, text="OFF", fg=fgColorButtonRed, bg=bgColorButton, cursor='hand2', command=lambda: relayOFF(frame22, myLabel22, image22, 22))
noButton22.place(relwidth=0.3, relheight=0.2, relx=0.55, rely=0.75)


if _gpioa2 & (1 << 7):
  bgColor = IMG_BACKGROUND_GREEN
else:
  bgColor = IMG_BACKGROUND_RED
frame23 = Frame(root, height=frameHeight, width = frameWidth, bd=borderWidth, bg=bgColorFrame, relief=borderStyle)
frame23.grid(column=4, row=3)

imgURL = './images/C_by_GE_logo.jpg'
img23 = Image.open(imgURL)
if img23.mode != 'RGBA':
  img23.convert('RGBA')
  img23.putalpha(alpha)

img23 = img23.resize((frameWidth-100, frameHeight-65), Image.ANTIALIAS)
render23 = ImageTk.PhotoImage(img23)
image23 = Label(frame23, image=render23, bg=bgColor)
image23.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.2)

myLabel23 = Label(frame23, text='', bg=bgColorFrame, fg=fgColorFrame)
myLabel23.place(relwidth=0.9, relheight=0.2, relx=0.05)
infoButton23 = Button(frame23, text="  i  ", cursor="hand2", bg=bgColorFrame, fg=fgColorFrame, command=lambda: createInfoWindow(frame23))
infoButton23.place(relx=infoBtnX, rely=infoBtnY)
yesButton23 = Button(frame23, text="ON", fg=fgColorButtonGreen, bg=bgColorButton, cursor='hand2', command=lambda: relayON(frame23, myLabel23, image23, 23))
yesButton23.place(relwidth=0.3, relheight=0.2, relx=0.15, rely=0.75)
noButton23 = Button(frame23, text="OFF", fg=fgColorButtonRed, bg=bgColorButton, cursor='hand2', command=lambda: relayOFF(frame23, myLabel23, image23, 23))
noButton23.place(relwidth=0.3, relheight=0.2, relx=0.55, rely=0.75)


if _gpiob2 & (1 << 0):
  bgColor = IMG_BACKGROUND_GREEN
else:
  bgColor = IMG_BACKGROUND_RED
frame24 = Frame(root, height=frameHeight, width = frameWidth, bd=borderWidth, bg=bgColorFrame, relief=borderStyle)
frame24.grid(column=5, row=3)

imgURL = './images/GE_logo.jpg'
img24 = Image.open(imgURL)
if img24.mode != 'RGBA':
  img24.convert('RGBA')
  img24.putalpha(alpha)

img24 = img24.resize((frameWidth-100, frameHeight-65), Image.ANTIALIAS)
render24 = ImageTk.PhotoImage(img24)
image24 = Label(frame24, image=render24, bg=bgColor)
image24.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.2)

myLabel24 = Label(frame24, text='', bg=bgColorFrame, fg=fgColorFrame)
myLabel24.place(relwidth=0.9, relheight=0.2, relx=0.05)
infoButton24 = Button(frame24, text="  i  ", cursor="hand2", bg=bgColorFrame, fg=fgColorFrame, command=lambda: createInfoWindow(frame24))
infoButton24.place(relx=infoBtnX, rely=infoBtnY)
yesButton24 = Button(frame24, text="ON", fg=fgColorButtonGreen, bg=bgColorButton, cursor='hand2', command=lambda: relayON(frame24, myLabel24, image24, 24))
yesButton24.place(relwidth=0.3, relheight=0.2, relx=0.15, rely=0.75)
noButton24 = Button(frame24, text="OFF", fg=fgColorButtonRed, bg=bgColorButton, cursor='hand2', command=lambda: relayOFF(frame24, myLabel24, image24, 24))
noButton24.place(relwidth=0.3, relheight=0.2, relx=0.55, rely=0.75)


if _gpiob2 & (1 << 1):
  bgColor = IMG_BACKGROUND_GREEN
else:
  bgColor = IMG_BACKGROUND_RED
frame25 = Frame(root, height=frameHeight, width = frameWidth, bd=borderWidth, bg=bgColorFrame, relief=borderStyle)
frame25.grid(column=0, row=4)

imgURL = './images/GE_logo.jpg'
img25 = Image.open(imgURL)
if img25.mode != 'RGBA':
  img25.convert('RGBA')
  img25.putalpha(alpha)

img25 = img25.resize((frameWidth-100, frameHeight-65), Image.ANTIALIAS)
render25 = ImageTk.PhotoImage(img25)
image25 = Label(frame25, image=render25, bg=bgColor)
image25.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.2)

myLabel25 = Label(frame25, text='', bg=bgColorFrame, fg=fgColorFrame)
myLabel25.place(relwidth=0.9, relheight=0.2, relx=0.05)
infoButton25 = Button(frame25, text="  i  ", cursor="hand2", bg=bgColorFrame, fg=fgColorFrame, command=lambda: createInfoWindow(frame25))
infoButton25.place(relx=infoBtnX, rely=infoBtnY)
yesButton25 = Button(frame25, text="ON", fg=fgColorButtonGreen, bg=bgColorButton, cursor='hand2', command=lambda: relayON(frame25, myLabel25, image25, 25))
yesButton25.place(relwidth=0.3, relheight=0.2, relx=0.15, rely=0.75)
noButton25 = Button(frame25, text="OFF", fg=fgColorButtonRed, bg=bgColorButton, cursor='hand2', command=lambda: relayOFF(frame25, myLabel25, image25, 25))
noButton25.place(relwidth=0.3, relheight=0.2, relx=0.55, rely=0.75)


if _gpiob2 & (1 << 2):
  bgColor = IMG_BACKGROUND_GREEN
else:
  bgColor = IMG_BACKGROUND_RED
frame26 = Frame(root, height=frameHeight, width = frameWidth, bd=borderWidth, bg=bgColorFrame, relief=borderStyle)
frame26.grid(column=1, row=4)

imgURL = './images/C_by_GE_Spark.jpg'
img26 = Image.open(imgURL)
if img26.mode != 'RGBA':
  img26.convert('RGBA')
  img26.putalpha(alpha)

img26 = img26.resize((frameWidth-100, frameHeight-65), Image.ANTIALIAS)
render26 = ImageTk.PhotoImage(img26)
image26 = Label(frame26, image=render26, bg=bgColor)
image26.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.2)

myLabel26 = Label(frame26, text='', bg=bgColorFrame, fg=fgColorFrame)
myLabel26.place(relwidth=0.9, relheight=0.2, relx=0.05)
infoButton26 = Button(frame26, text="  i  ", cursor="hand2", bg=bgColorFrame, fg=fgColorFrame, command=lambda: createInfoWindow(frame26))
infoButton26.place(relx=infoBtnX, rely=infoBtnY)
yesButton26 = Button(frame26, text="ON", fg=fgColorButtonGreen, bg=bgColorButton, cursor='hand2', command=lambda: relayON(frame26, myLabel26, image26, 26))
yesButton26.place(relwidth=0.3, relheight=0.2, relx=0.15, rely=0.75)
noButton26 = Button(frame26, text="OFF", fg=fgColorButtonRed, bg=bgColorButton, cursor='hand2', command=lambda: relayOFF(frame26, myLabel26, image26, 26))
noButton26.place(relwidth=0.3, relheight=0.2, relx=0.55, rely=0.75)


if _gpiob2 & (1 << 3):
  bgColor = IMG_BACKGROUND_GREEN
else:
  bgColor = IMG_BACKGROUND_RED
frame27 = Frame(root, height=frameHeight, width = frameWidth, bd=borderWidth, bg=bgColorFrame, relief=borderStyle)
frame27.grid(column=2, row=4)

imgURL = './images/GE_logo.jpg'
img27 = Image.open(imgURL)
if img27.mode != 'RGBA':
  img27.convert('RGBA')
  img27.putalpha(alpha)

img27 = img27.resize((frameWidth-100, frameHeight-65), Image.ANTIALIAS)
render27 = ImageTk.PhotoImage(img27)
image27 = Label(frame27, image=render27, bg=bgColor)
image27.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.2)

myLabel27 = Label(frame27, text='', bg=bgColorFrame, fg=fgColorFrame)
myLabel27.place(relwidth=0.9, relheight=0.2, relx=0.05)
infoButton27 = Button(frame27, text="  i  ", cursor="hand2", bg=bgColorFrame, fg=fgColorFrame, command=lambda: createInfoWindow(frame27))
infoButton27.place(relx=infoBtnX, rely=infoBtnY)
yesButton27 = Button(frame27, text="ON", fg=fgColorButtonGreen, bg=bgColorButton, cursor='hand2', command=lambda: relayON(frame27, myLabel27, image27, 27))
yesButton27.place(relwidth=0.3, relheight=0.2, relx=0.15, rely=0.75)
noButton27 = Button(frame27, text="OFF", fg=fgColorButtonRed, bg=bgColorButton, cursor='hand2', command=lambda: relayOFF(frame27, myLabel27, image27, 27))
noButton27.place(relwidth=0.3, relheight=0.2, relx=0.55, rely=0.75)


if _gpiob2 & (1 << 4):
  bgColor = IMG_BACKGROUND_GREEN
else:
  bgColor = IMG_BACKGROUND_RED
frame28 = Frame(root, height=frameHeight, width = frameWidth, bd=borderWidth, bg=bgColorFrame, relief=borderStyle)
frame28.grid(column=3, row=4)

imgURL = './images/C_by_GE_Spark.jpg'
img28 = Image.open(imgURL)
if img28.mode != 'RGBA':
  img28.convert('RGBA')
  img28.putalpha(alpha)

img28 = img28.resize((frameWidth-100, frameHeight-65), Image.ANTIALIAS)
render28 = ImageTk.PhotoImage(img28)
image28 = Label(frame28, image=render28, bg=bgColor)
image28.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.2)

myLabel28 = Label(frame28, text='', bg=bgColorFrame, fg=fgColorFrame)
myLabel28.place(relwidth=0.9, relheight=0.2, relx=0.05)
infoButton28 = Button(frame28, text="  i  ", cursor="hand2", bg=bgColorFrame, fg=fgColorFrame, command=lambda: createInfoWindow(frame28))
infoButton28.place(relx=infoBtnX, rely=infoBtnY)
yesButton28 = Button(frame28, text="ON", fg=fgColorButtonGreen, bg=bgColorButton, cursor='hand2', command=lambda: relayON(frame28, myLabel28, image28, 28))
yesButton28.place(relwidth=0.3, relheight=0.2, relx=0.15, rely=0.75)
noButton28 = Button(frame28, text="OFF", fg=fgColorButtonRed, bg=bgColorButton, cursor='hand2', command=lambda: relayOFF(frame28, myLabel28, image28, 28))
noButton28.place(relwidth=0.3, relheight=0.2, relx=0.55, rely=0.75)


if _gpiob2 & (1 << 5):
  bgColor = IMG_BACKGROUND_GREEN
else:
  bgColor = IMG_BACKGROUND_RED
frame29 = Frame(root, height=frameHeight, width = frameWidth, bd=borderWidth, bg=bgColorFrame, relief=borderStyle)
frame29.grid(column=4, row=4)

imgURL = './images/GE_logo.jpg'
img29 = Image.open(imgURL)
if img29.mode != 'RGBA':
  img29.convert('RGBA')
  img29.putalpha(alpha)

img29 = img29.resize((frameWidth-100, frameHeight-65), Image.ANTIALIAS)
render29 = ImageTk.PhotoImage(img29)
image29 = Label(frame29, image=render29, bg=bgColor)
image29.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.2)

myLabel29 = Label(frame29, text='', bg=bgColorFrame, fg=fgColorFrame)
myLabel29.place(relwidth=0.9, relheight=0.2, relx=0.05)
infoButton29 = Button(frame29, text="  i  ", cursor="hand2", bg=bgColorFrame, fg=fgColorFrame, command=lambda: createInfoWindow(frame29))
infoButton29.place(relx=infoBtnX, rely=infoBtnY)
yesButton29 = Button(frame29, text="ON", fg=fgColorButtonGreen, bg=bgColorButton, cursor='hand2', command=lambda: relayON(frame29, myLabel29, image29, 29))
yesButton29.place(relwidth=0.3, relheight=0.2, relx=0.15, rely=0.75)
noButton29 = Button(frame29, text="OFF", fg=fgColorButtonRed, bg=bgColorButton, cursor='hand2', command=lambda: relayOFF(frame29, myLabel29, image29, 29))
noButton29.place(relwidth=0.3, relheight=0.2, relx=0.55, rely=0.75)


if _gpiob2 & (1 << 6):
  bgColor = IMG_BACKGROUND_GREEN
else:
  bgColor = IMG_BACKGROUND_RED
frame30 = Frame(root, height=frameHeight, width = frameWidth, bd=borderWidth, bg=bgColorFrame, relief=borderStyle)
frame30.grid(column=5, row=4)

imgURL = './images/C_by_GE_Spark.jpg'
img30 = Image.open(imgURL)
if img30.mode != 'RGBA':
  img30.convert('RGBA')
  img30.putalpha(alpha)

img30 = img30.resize((frameWidth-100, frameHeight-65), Image.ANTIALIAS)
render30 = ImageTk.PhotoImage(img30)
image30 = Label(frame30, image=render30, bg=bgColor)
image30.place(relwidth=0.5, relheight=0.5, relx=0.25, rely=0.2)

myLabel30 = Label(frame30, text='', bg=bgColorFrame, fg=fgColorFrame)
myLabel30.place(relwidth=0.9, relheight=0.2, relx=0.05)
infoButton30 = Button(frame30, text="  i  ", cursor="hand2", bg=bgColorFrame, fg=fgColorFrame, command=lambda: createInfoWindow(frame30))
infoButton30.place(relx=infoBtnX, rely=infoBtnY)
yesButton30 = Button(frame30, text="ON", fg=fgColorButtonGreen, bg=bgColorButton, cursor='hand2', command=lambda: relayON(frame30, myLabel30, image30, 30))
yesButton30.place(relwidth=0.3, relheight=0.2, relx=0.15, rely=0.75)
noButton30 = Button(frame30, text="OFF", fg=fgColorButtonRed, bg=bgColorButton, cursor='hand2', command=lambda: relayOFF(frame30, myLabel30, image30, 30))
noButton30.place(relwidth=0.3, relheight=0.2, relx=0.55, rely=0.75)


# Davey's playground!!!

# for x in range(30):
#   print(hex(x))

# for character in('Hello World!'):
#   print(hex(ord(character)), character)

# now = time.time()

# print(now)
# print(time.asctime(time.gmtime(now)))
# print(time.asctime(time.localtime(now)))

# x = 0x20
# print(type(x))
# print(bin(x | 1))
# x |= 1
# print(hex(x))

# x = 346589367
# print(x)
# x &= 0xff
# print(x)

# x = 0x01
# x <<= 2
# print(x)

# x = 12
# print(0 < x < 10)

# print(chr(65))

# for y in range(rows):
#   for x in range(columns):
#     print((columns * y) + x + 1)



root.protocol('WM_DELETE_WINDOW', on_close)
root.mainloop()