from PIL import Image
from random import randint

def pinkfilter(img, blank):
    filtered_img = Image.new(mode="RGB", size=(img.width, img.height), color = (255, 255, 255))
    for y in range(img.height):
        for x in range(img.width):
            (r, g, b) = img.getpixel((x, y))
            r = r + 256
            b = b + 100
            g = g + 30
            filtered_img.putpixel((x,y), (r, g, b))
    #filtered_img.show()
    
    for y in range(filtered_img.height):
        for x in range(filtered_img.width):
            (r, g, b) = filtered_img.getpixel((x, y))
            blank.putpixel((filtered_img.width+x,y), (r, g, b))
            blank.putpixel((x,filtered_img.height+y), (r, g, b))
    
def purplefilter(img, blank):
    filtered_img = Image.new(mode="RGB", size=(img.width, img.height), color = (255, 255, 255))
    for y in range(img.height):
        for x in range(img.width):
            (r, g, b) = img.getpixel((x, y))
            b = b + 256
            r = r + 100
            g = g + 30
            filtered_img.putpixel((x,y), (r, g, b))
    #filtered_img.show()
    
    for y in range(filtered_img.height):
        for x in range(filtered_img.width):
            (r, g, b) = filtered_img.getpixel((x, y))
            blank.putpixel((x,y), (r, g, b))
            blank.putpixel((filtered_img.width+x,filtered_img.height+y), (r, g, b))

def center_img(img, blank):
    for y in range(img.height):
        for x in range(img.width):
            (r, g, b) = img.getpixel((x, y))
            blank.putpixel((int(img.width/2)+x,int(img.height/2)+y), (r, g, b))
            
def main():
    my_img = Image.open("cat.jpg")
    my_img.show()
    blank = Image.new(mode="RGB", size=(2*my_img.width, 2*my_img.height), color = (255, 255, 255))
    #blank.show()
    
    pinkfilter(my_img, blank)
    purplefilter(my_img, blank)
    center_img(my_img, blank)
    blank.show()
    

main()
