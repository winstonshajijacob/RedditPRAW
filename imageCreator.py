from PIL import Image,ImageDraw,ImageFont
import textwrap
from pathlib import Path


def ques_img(path,i):
    #dynamically create path
    i=str(i)+".jpg"
    start_path = Path('Resources/output')
    final_path = start_path / path / i 

    img = Image.open('Resources/bg1.jpg')
    d1 = ImageDraw.Draw(img)

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
    d1.text((120,250), "Posted by /u/"+poster_name+" "+timeago, font=sub_text, fill = fcolor)

    #question
    text = "You’re 78 years old, you’ve reached the end of your life and you die. Next thing you know, you’re wide awake sitting in a circle with a bunch of other people and they ask how your trip was. Would you try that drug again, why or why not?"
    text1 = "This is a question in ask reddit"
    # d1.text((120,600),text , font=content, fill = fcolor)
    lines = textwrap.wrap(text, width=text_width)

    for line in lines:
        width, height = content.getsize(line)
        #(1080 - width) / 2
        d1.text((25, y_text), line, font=content, fill= fcolor)
        y_text += height

    #After title
    d1.text((25,y_text+20), "30k Comments", font=sub_text, fill = fcolor)
    d1.text((900,y_text +20), "100% upvoted", font=sub_text, fill = fcolor)

    img.save(final_path)


def comment_img(path,i):
    i=str(i)+".jpg"
    start_path = Path('Resources/output')
    final_path = start_path / path / i 

    img = Image.open('Resources/bg2.jpg')
    d1 = ImageDraw.Draw(img)

    poster_name = "winston"
    timeago = "1 hour ago"
    points="30k"
    #setting y distance
    y_text = 120
    text_width = 38.9
    #Set fonts and sizes and fill color
    heading = ImageFont.truetype('Resources/verdanab.ttf', 30)
    sub_text = ImageFont.truetype('Resources/Verdana.ttf', 18)
    content = ImageFont.truetype('Resources/verdanab.ttf', 44)
    fcolor = (0, 0, 0)

    #Poster
    d1.text((30,100), "/u/"+poster_name+" "+points+" points "  +timeago, font=sub_text, fill = fcolor)

    #question
    text = "This is an answer and im checking the formatting" + i
    text1 = "This was years ago now, but I used to work with a guy who had been an engineer for Match.com.  He said 99% of the profiles were inactive, and that 80% of the active profiles were men.  He didn't provide numbers but also said the was a huge disparity between the average number of messages sent to women versus those sent to men.  According to him, all told the site was mostly men reaching out to dead profiles and never getting responses.As I said however, this was years ago, so it's entirely possible that they've cleaned the site up since then. checking maximum size 1234567890 checking maximum size 1234567890"
    # d1.text((120,600),text , font=content, fill = fcolor)
    print(len(text1))
    lines = textwrap.wrap(text, width=text_width)

    for line in lines:
        width, height = content.getsize(line)
        #(1080 - width) / 2
        d1.text((25, y_text), line, font=content, fill= fcolor)
        y_text += height


    img.save(final_path)


ques_img("k12shw",0)
for i in range(1,9):
    comment_img("k12shw",i)
