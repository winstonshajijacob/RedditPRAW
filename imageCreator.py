from PIL import Image,ImageDraw,ImageFont
import textwrap
from pathlib import Path
from extract_from_reddit import read_table
from si_prefix import si_format
import os
import cred

def ques_img(data,sub_id):
    #dynamically create path
    # print(data)
    # print(sub_id)
    path1 ='Resources/output/'+sub_id
    if not os.path.exists(path1):
        os.makedirs(path1)
    ext="0.jpg"
    start_path = Path(path1)
    final_path = start_path / ext 

    img = Image.open('Resources/bg1.jpg')
    d1 = ImageDraw.Draw(img)

    #placeholders
    poster_name = "winston"
    timeago = "1 hour ago"

    #setting y pos and text width
    y_text = 300
    text_width = 38.9

    #Set fonts and sizes and fill color
    heading = ImageFont.truetype('Resources/verdanab.ttf', 30)
    sub_text = ImageFont.truetype('Resources/Verdana.ttf', 18)
    content = ImageFont.truetype('Resources/verdanab.ttf', 46)
    fcolor = (0, 0, 0)

    #Title
    d1.text((120,250), "Posted by /u/"+data[3]+" "+data[4], font=sub_text, fill = fcolor)

    #question
    #creates tesxt wrapping
    lines = textwrap.wrap(data[2], width=text_width)

    for line in lines:
        width, height = content.getsize(line)
        #(1080 - width) / 2
        d1.text((25, y_text), line, font=content, fill= fcolor)
        y_text += height

    #After title
    d1.text((25,y_text+20), si_format(int(data[8]),precision=2)+" Comments", font=sub_text, fill = fcolor)
    d1.text((900,y_text +20), data[6]+" % upvoted", font=sub_text, fill = fcolor)
    
    img.save(final_path)


def comment_img(data,sub_id):
    
    path1 ='Resources/output/'+sub_id
    if not os.path.exists(path1):
        os.makedirs(path1)
    start_path = Path(path1)
    
    poster_name = "winston"
    timeago = "1 hour ago"
    points="30k"
    
    #Set fonts and sizes and fill color
    heading = ImageFont.truetype('Resources/verdanab.ttf', 30)
    sub_text = ImageFont.truetype('Resources/Verdana.ttf', 18)
    content = ImageFont.truetype('Resources/verdanab.ttf', 44)
    fcolor = (0, 0, 0)
    index = 0
    for comment in data:
        #setting y distance
        y_text = 120
        text_width = 38.9
        img = Image.open('Resources/bg2.jpg')
        d1 = ImageDraw.Draw(img)
        index+=1
        ext=str(index)+".jpg"
        final_path = start_path / ext 
        #Poster 
        d1.text((30,100), "/u/"+comment[3]+" "+si_format(int(comment[5]),precision=2)+" points "  +timeago, font=sub_text, fill = fcolor)

        #question
        lines = textwrap.wrap(comment[2], width=text_width)

        for line in lines:
            width, height = content.getsize(line)
            #(1080 - width) / 2
            d1.text((25, y_text), line, font=content, fill= fcolor)
            y_text += height


        img.save(final_path)



