import random
import operator
import PIL
from PIL import Image, ImageDraw, ImageFont
import sys

style = 1

def flower(x : int, y : int) :
    draw.ellipse((x - 2, y - 2, x + 2, y + 2), fill = (242, 53, 230), outline = (237, 37, 225))
    draw.ellipse((x - 5, y - 5, x - 1, y - 1), fill = (255, 244, 254), outline = (249, 232, 248))
    draw.ellipse((x + 1, y - 5, x + 5, y - 1), fill = (255, 244, 254), outline = (249, 232, 248))
    draw.ellipse((x - 5, y + 1, x - 1, y + 5), fill = (255, 244, 254), outline = (249, 232, 248))
    draw.ellipse((x + 1, y + 1, x + 5, y + 5), fill = (255, 244, 254), outline = (249, 232, 248))

def has_flowers(how_many : int) :
    does_have_flowers = True
    num_of_flowers = how_many

if __name__ == "__main__":
    if (style == 1) 
        defaultPreset = "birch"

        if len(sys.argv) > 1:
            preset = sys.argv[1]
        else:
            preset = defaultPreset

        does_have_flowers = False
        num_of_flowers = 0

        outline_width = 3 #the width of the tree outline
        treenoise = 60 #number of random details on the leaves
        trunknoise = 20 #number of random details on the trunk
        trunknoise_direction = 'h' #direction of trunk details (h - horizontal, v - vertical)
        trunk_detail_length = 5 #length of details on the tree's trunk
        detail_length = 15 #random details length in pixels
        increasing_lines = 0 #height of curvature at the bottom of the trunk
        sine_multiplier = 0 #curvature strength
        trunk_width = 2 #horizontal width of the trunk in pixels
        leaves_color = (252, 68, 163)
        detail_color = (249, 102, 178)
        leaf_outline_color = (211, 33, 125)
        trunk_color = (244, 207, 41)
        trunk_detail_color = (244, 207, 41)
        trunk_outline_color = (219, 180, 6)

        if (preset == "cedar") :
            outline_width = 2
            treenoise = 20
            trunknoise = 12
            trunknoise_direction = 'v' 
            trunk_detail_length = 8
            detail_length = 4
            increasing_lines = 10 
            sine_multiplier = 0.075
            trunk_width = 6
            leaves_color = (10, 206, 39)
            detail_color = (37, 221, 49)
            trunk_detail_color = (196, 122, 19)
            leaf_outline_color = (50, 150, 22)
            trunk_color = (173, 108, 17)
            trunk_outline_color = (119, 73, 9)

        if (preset == "cherry blossom") :
            outline_width = 2
            treenoise = 20
            trunknoise = 12
            trunknoise_direction = 'v' 
            trunk_detail_length = 8
            detail_length = 4
            increasing_lines = 10 
            sine_multiplier = 0.075
            trunk_width = 6
            leaves_color = (255, 211, 251)
            detail_color = (242, 196, 238)
            trunk_detail_color = (89, 54, 16)
            leaf_outline_color = (252, 189, 246)
            trunk_color = (68, 42, 14)
            trunk_outline_color = (45, 29, 11)
            does_have_flowers = True
            num_of_flowers = 8

        if (preset == "birch") :
            outline_width = 2
            treenoise = 20
            trunknoise = 7
            trunknoise_direction = 'h' 
            trunk_detail_length = 4
            detail_length = 3
            increasing_lines = 7 
            sine_multiplier = 0.075
            trunk_width = 3
            leaves_color = (69, 188, 22)
            detail_color = (78, 201, 30)
            trunk_detail_color = (38, 38, 38)
            leaf_outline_color = (61, 173, 17)
            trunk_color = (239, 239, 239)
            trunk_outline_color = (204, 204, 204)

        if (preset == "ice cream") :
            outline_width = 3
            treenoise = 60
            trunknoise = 0
            trunknoise_direction = 'h' 
            trunk_detail_length = 0 
            detail_length = 15
            increasing_lines = 0 
            sine_multiplier = 0
            trunk_width = 2
            leaves_color = (252, 68, 163)
            detail_color = (249, 102, 178)
            trunk_detail_color = (249, 102, 178)
            leaf_outline_color = (211, 33, 125)
            trunk_color = (244, 207, 41)
            trunk_outline_color = (219, 180, 6)

        pix = Image.new('RGB', (150, 150), color = 'white')
        pixmap = pix.load()
        draw = ImageDraw.Draw(pix)


        draw.rectangle(((50 - outline_width, 70 - outline_width), (100 + outline_width, 100 + outline_width)), fill = leaf_outline_color)
        draw.rectangle(((70 - outline_width, 50 - outline_width), (80 + outline_width, 90 + outline_width)), fill = leaf_outline_color)
        draw.ellipse(((50 - outline_width, 50 - outline_width), (90 + outline_width, 90 + outline_width)), fill = leaf_outline_color, outline = leaf_outline_color)
        draw.ellipse(((60 - outline_width, 50 - outline_width), (100 + outline_width, 90 + outline_width)), fill = leaf_outline_color, outline = leaf_outline_color)

        draw.rectangle(((50, 70), (100, 100)), fill = leaves_color)
        draw.rectangle(((70, 50), (80, 90)), fill = leaves_color)
        draw.ellipse(((50, 50), (90, 90)), fill = leaves_color, outline = leaves_color)
        draw.ellipse(((60, 50), (100, 90)), fill = leaves_color, outline = leaves_color)


    
    
        draw.rectangle(((75 - trunk_width - outline_width, 100 + outline_width + 1), (75 + trunk_width + outline_width, 130)), fill = trunk_outline_color)
        draw.rectangle(((75 - trunk_width, 100 + outline_width + 1), (75 + trunk_width, 130)), fill = trunk_color)
        crt_line = 0
        if ((increasing_lines != 0) and (sine_multiplier != 0)) :
            while (crt_line < increasing_lines) :
                draw.line([(76 + trunk_width, 131 - increasing_lines + crt_line), (76 + trunk_width + (crt_line * crt_line * sine_multiplier), 131 - increasing_lines + crt_line)], trunk_color)
                draw.line([(74 - trunk_width, 131 - increasing_lines + crt_line), (74 - trunk_width - (crt_line * crt_line * sine_multiplier), 131 - increasing_lines + crt_line)], trunk_color)
                if (outline_width != 0) :
                    draw.line([(76 + trunk_width + (crt_line * crt_line * sine_multiplier), 131 - increasing_lines + crt_line), (76 + trunk_width + (crt_line * crt_line * sine_multiplier) + outline_width, 131 - increasing_lines + crt_line)], trunk_outline_color)
                    draw.line([(74 - trunk_width - (crt_line * crt_line * sine_multiplier), 131 - increasing_lines + crt_line), (74 - trunk_width - (crt_line * crt_line * sine_multiplier) - outline_width, 131 - increasing_lines + crt_line)], trunk_outline_color)
                crt_line += 1

        draw.line([(74 - trunk_width - ((increasing_lines) * (increasing_lines) * sine_multiplier) - outline_width + 1, 131 - increasing_lines + (increasing_lines)), (75 + trunk_width + ((increasing_lines) * (increasing_lines) * sine_multiplier) + outline_width, 131 - increasing_lines + (increasing_lines))], trunk_outline_color)
        draw.line([(74 - trunk_width - ((increasing_lines+1) * (increasing_lines+1) * sine_multiplier) - outline_width + 1, 131 - increasing_lines + (increasing_lines+1)), (75 + trunk_width + ((increasing_lines+1) * (increasing_lines+1) * sine_multiplier) + outline_width, 131 - increasing_lines + (increasing_lines+1))], trunk_outline_color)
    
        crt_number = 0
        while (crt_number < treenoise) :
            pixels_x = random.randint(50, 100)
            pixels_y = random.randint(50, 100)
            if (pixmap[pixels_x, pixels_y] == leaves_color) :
                i = 0
                while (i < detail_length) :
                    if (pixmap[pixels_x, pixels_y + i] == leaves_color) :
                        pixmap[pixels_x, pixels_y + i] = detail_color
                
                    i+=1

                crt_number += 1


        crt_trd = 0
        while (crt_trd < trunknoise) :
            pixels_x = random.randint(75 - trunk_width - int((increasing_lines * increasing_lines * sine_multiplier)), 74 + trunk_width + int((increasing_lines * increasing_lines * sine_multiplier)))
            pixels_y = random.randint(101 + outline_width, 130)
            if ((pixmap[pixels_x, pixels_y] == trunk_color) or (pixmap[pixels_x, pixels_y] == trunk_outline_color)) :
                k = 0
                while (k < trunk_detail_length) :
                    if (trunknoise_direction == 'v') :
                        if (pixmap[pixels_x, pixels_y + k] == trunk_color) :
                            pixmap[pixels_x, pixels_y + k] = trunk_detail_color
                    if (trunknoise_direction == 'h') :
                        if (pixmap[pixels_x + k, pixels_y] == trunk_color) :
                            pixmap[pixels_x + k, pixels_y] = trunk_detail_color
                
                    k+=1

            crt_trd += 1

        if (does_have_flowers) :
            crt_number = 0
            while (crt_number < num_of_flowers) :
                pixels_x = random.randint(50, 100)
                pixels_y = random.randint(50, 100)
                if (pixmap[pixels_x, pixels_y] == leaves_color) :
                    flower(pixels_x, pixels_y)

                    crt_number += 1

        #draw.line((75, 0, 75, 150), (0,0,0))
        pix.save('pixel_art.png')
        print(does_have_flowers)
        pix.show()

    if (style == 2) :

        twists = 6 #number of twists the trunk makes
    
        pix = Image.new('RGB', (150, 150), color = 'white')
        pixmap = pix.load()
        draw = ImageDraw.Draw(pix)
        crt_twist = 0
        sine_multiplier = 3

        startpoint = (75, 150)
        endpoint = (75, 120)
        while (crt_twist < twists) :
            draw.line([startpoint,endpoint], (0,0,0), 3)
            startpoint = endpoint
            endpoint = tuple(map(operator.add, endpoint, (int((crt_twist * sine_multiplier)^2), -20)))
            crt_twist += 1

        pix.save('pixel_art.png')
        pix.show()

