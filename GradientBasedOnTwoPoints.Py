from PIL import Image
import random

def create_gradient_image(width, height):
    
    image = Image.new("RGB", (width, height))
    pixels = image.load()

    
    x1, y1 = 0,0
    x2,y2 = 255,0
    
    for x in range(width):
        for y in range(height):
            
            t = ((x - x1) * (x2 - x1) + (y - y1) * (y2 - y1)) / float((x2 - x1)**2 + (y2 - y1)**2)
            t = max(0, min(1, t))
            
            color = int(t*255)                      
            pixels[x, y] = (255, color, color)    
    

    return image

width, height = 256, 256

gradient_image = create_gradient_image(width, height)

gradient_image.save("gradient_image.png")

print("Gradient image created and saved as gradient_image.png")

gradient_image.show()