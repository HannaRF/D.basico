from PIL import Image, ImageDraw
'''
O número de iterações se limita a naturais menores que 10,incluindo o 0
'''
def concat_h(im1, im2):
    image = Image.new('RGB', (im1.width + im2.width, im1.height))
    image.paste(im1, (0, 0))
    image.paste(im2, (im1.width, 0))
    return image

def concat_v(im1, im2):
    image = Image.new('RGB', (im1.width, im1.height + im2.height))
    image.paste(im1, (0, 0))
    image.paste(im2, (0, im1.height))
    return image

def Peano(iterations = 5):
    b = 5
    dimx = 20
    dimy = 20
    color1 = (0,255,255)
    color = (255,0,255)

    image = Image.new("RGB", (dimx, dimy))
    draw = ImageDraw.Draw(image)
    draw.line([b, b, b + 10, b], fill=color1, width=1)
    draw.line([b, b, b, b + 10], fill=color1, width=1)
    draw.line([b + 10, b, b + 10, b + 10], fill=color1, width=1)

    for i in range(iterations):
        image0 = concat_h(image,image)
        image1 = concat_h(image.rotate(-90),image.rotate(90))
        image = concat_v(image0,image1)

        draw = ImageDraw.Draw(image)
        x =  40*(2**i)
        draw.line([(x/2) - b,(x/2) - b,(x/2) + b,(x/2) - b],fill=color, width=1)
        draw.line([b,(x/2) - b,b,(x/2) + b], fill=color, width=1)
        draw.line([x - b,(x/2) - b,x - b,(x/2) + b], fill=color, width=1)
    image.show()


Peano()