from PIL import Image

def stegoxy(xy_file):
    with open(xy_file, 'r') as file:
        lines = file.readlines()
    
    xy_list = []
    
    for line in lines:
        xy_split = line.strip().split(', ')
        for coord in xy_split:
            x, y = map(int, coord.strip('()').split(','))
            xy_list.append((x, y))
    
    for (x, y) in xy_list:
        new_image.putpixel((x, y), (0, 0, 0))
    
    return new_image

xy_file = "C:\\xy_file.txt"

image_width = 800
image_height = 600

new_image = Image.new("RGB", (image_width, image_height), (255, 255, 255)) 

new_image = stegoxy(xy_file)

new_image.save("C:\\flag_image.png")
