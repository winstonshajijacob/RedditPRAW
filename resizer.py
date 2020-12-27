#Script for immediate img manipulation and tinkering
# #Import required Image library
from PIL import Image,ImageDraw,ImageFont
import textwrap
# from PIL import Image

# #Create an Image Object from an Image
# im = Image.open("Resources/logo.png")

# #Display actual image
# # im.show()

# #Make the new image half the width and half the height of the original image
# resized_im = im.resize((round(im.size[0]*0.30), round(im.size[1]*0.30)))

# #Display the resized imaged
# # resized_im.show()

# #Save the cropped image
# resized_im.save('Resources/logo30.png')
fcolor = (0, 0, 0)
img = Image.open('Resources/bg2.jpg')
logo = Image.open('Resources/logo30.png')
# arrow = Image.open('Resources/resized85.png')
d1 = ImageDraw.Draw(img)
heading = ImageFont.truetype('Resources/verdanab.ttf', 32) #44
sub_text = ImageFont.truetype('Resources/Verdana.ttf', 18)
# #Top Left text
# d1.text((90,20), "Swipe", font=heading, fill = fcolor)
# img.paste(arrow,(0,0),arrow)

#  #Post Title
img.paste(logo,(30,200),logo)
d1.text((120,200), "r/AskReddit", font=heading, fill = fcolor)

# #Bottom Text
# text = "Follow @ask_the_internet for more content like this "
# text_width = 60
# lines = textwrap.wrap(text, width=text_width)
# y_text = 1040


# for line in lines:
#         width, height = heading.getsize(line)
#         #(1080 - width) / 2
#         d1.text((100, y_text), line, font=heading, fill= fcolor)
#         y_text += height

# d1.text((300,y_text+3), "@mypagenamehere", font=heading, fill = fcolor)
# img.paste(logo,(431,y_text+100),logo)

img.save("bg1.jpg")