#Import statements
#Uses Image for creating the .jpg file
#Uses ImageDraw for creating the shapes that represent each checkerpiece
from PIL import Image, ImageDraw

#Generates the checkerboard pattern, for initialization and reset
#First creates a 8 by 8 pixel image, then upscales to correct size
def checkerboard():
    size = 8
    pix = Image.new("RGB", (size, size), "red")
    pixelmap = pix.load()

    for x in range(8):
        for y in range(8):
            if ((x%2==0 and y%2==1) or (x%2==1 and y%2==0)):
                for i in range(x,x+1):
                    for j in range(y,y+1):
                        pixelmap[i,j] = (50, 50, 50)

    pix = pix.resize((size*100,size*100),Image.NEAREST)
    pix.save("checkerboard.jpg")

#Code for drawing checkerpieces
#Size of canvas: 100 pixels: fits on current checkerboard scaling
#Draws the white checkerpiece
def whitecp():
    size = 100
    pix = Image.new("RGB", (size, size), (50,50,50))
    
    draw = ImageDraw.Draw(pix)
    draw.ellipse((5,5,95,95), fill=(256,256,256))
    draw.ellipse((7,7,93,93), fill=(0,0,0))
    draw.ellipse((9,9,91,91), fill=(256,256,256))
    
    del draw
    pix.save("whitecp.jpg")

#Draws the black checkerpiece
def blackcp():
    size = 100
    pix = Image.new("RGB", (size, size), (50,50,50))
    
    draw = ImageDraw.Draw(pix)
    draw.ellipse((5,5,95,95), fill=(0,0,0))
    draw.ellipse((7,7,93,93), fill=(256,256,256))
    draw.ellipse((9,9,91,91), fill=(0,0,0))
    
    del draw
    pix.save("blackcp.jpg")

#Draws the white king checkerpiece
def kingwhitecp():
    size = 100
    pix = Image.new("RGB", (size, size), (50,50,50))
    
    draw = ImageDraw.Draw(pix)
    draw.ellipse((5,5,95,95), fill=(256,256,256))
    draw.ellipse((7,7,93,93), fill=(0,0,0))
    draw.ellipse((9,9,91,91), fill=(256,256,256))
    draw.ellipse((20,20,80,80), fill=(0,0,0))

    del draw
    pix.save("kingwhitecp.jpg")

#Draws the black king checkerpiece
def kingblackcp():
    size = 100
    pix = Image.new("RGB", (size, size), (50,50,50))
    
    draw = ImageDraw.Draw(pix)
    draw.ellipse((5,5,95,95), fill=(0,0,0))
    draw.ellipse((7,7,93,93), fill=(256,256,256))
    draw.ellipse((9,9,91,91), fill=(0,0,0))
    draw.ellipse((20,20,80,80), fill=(256,256,256))
    
    del draw
    pix.save("kingblackcp.jpg")