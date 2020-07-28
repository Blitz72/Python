import board
import neopixel
import time


numPixels = 16
fadePixels = 12
cycles = 10
timeDelay = 0.005
count = 0

pixels = neopixel.NeoPixel(board.D18, numPixels)

#colorArray = [(255, 0, 0), (125, 125, 0), (0, 255, 0), (0, 0, 255)]

#pixels = [pixels[0], pixels[1], pixels[2], pixels[3]]

#while count < 10:
#    for i in range(4):
#        for j in range(16):
#            pixels[j] = colorArray[i]
#        time.sleep(1)
#        for j in range(16):
#            pixels[j] = (0, 0, 0)
#        time.sleep(1)
#    count += 1

# red to green
for x in range(cycles):
    for i in range(numPixels):
        for j in range(numPixels):
            red = (255 - int(j*255/fadePixels))
            if red < 0:
                red = 0
            red = int(red*((cycles-x)/cycles))
            green = int((255 - int(j*255/fadePixels))*x/cycles)
            if green < 0:
                green = 0
            index = j - i
            if index < 0:
                index += numPixels
            pixels[index] = (red, green, 0)
        time.sleep(timeDelay)

# green to blue
for x in range(cycles):
    for i in range(numPixels):
        for j in range(numPixels):
            green = (255 - int(j*255/fadePixels))
            if green < 0:
                green = 0
            green = int(green*((cycles-x)/cycles))
            blue = int((255 - int(j*255/fadePixels))*x/cycles)
            if blue < 0:
                blue = 0
            index = j - i
            if index < 0:
                index += numPixels
            pixels[index] = (0, green, blue)
        time.sleep(timeDelay)

# blue to red
for x in range(cycles):
    for i in range(numPixels):
        for j in range(numPixels):
            blue = (255 - int(j*255/fadePixels))
            if blue < 0:
                blue = 0
            blue = int(blue*((cycles-x)/cycles))
            red = int((255 - int(j*255/fadePixels))*x/cycles)
            if red < 0:
                red = 0
            index = j - i
            if index < 0:
                index += numPixels
            pixels[index] = (red, 0, blue)
        time.sleep(timeDelay)

for i in range(numPixels):
    pixels[i] = (0, 0, 0)
    