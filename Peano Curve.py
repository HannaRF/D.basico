from PIL import Image, ImageDraw
import numpy as np

# rotaciona em sentido anti-horário

def rot(x,y,degree = np.pi/2):
    x = x*np.cos(degree) - y*np.sin(degree)
    y = x*np.sin(degree) + y*np.cos(degree)

def Peano(iterations = 1):
    b = 10
    dimx = 100
    dimy = 100

    for i in range(iterations):
        image = Image.new("RGB", (dimx, dimy))
        draw = ImageDraw.Draw(image)
        draw.line([b, b, b + 25, b], fill=128, width=5)
        draw.line([b, b, b , b + 25], fill=128, width=5)
        draw.line([b + 25, b, b + 25, b + 25], fill=128, width=5)
        image.show()


Peano()

#https://note.nkmk.me/en/python-pillow-concat-images/