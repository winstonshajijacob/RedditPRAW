from imageCreator import *
from extract_from_reddit import *
from instagrapi import Client
from pathlib import Path
import random

def rm_tree(pth):
    pth = Path(pth)
    for child in pth.glob('*'):
        if child.is_file():
            child.unlink()
        else:
            rm_tree(child)
    pth.rmdir()

#python create directory
# print(post)


post = read_table()
post_id = """'"""+post[0][1]+"""'"""
comments = read_comments(post_id)
ques_img(post[0],post[0][1])
comment_img(comments,post[0][1])


#post to instagram and update as posted
p_list =[]
base_path = 'Resources/output/'+post[0][1]
fpath = Path(base_path)
for i in range (9):
    p = str(i)+".jpg"
    p1= fpath / p
    p_list.append(p1)
p_list.append(Path('Resources/output/9.jpg'))

hashtag_list =['#askme', '#questionandanswer', '#questionablejudgement', '#redditgetsdrawn', '#redditphotoproject', '#QuestionLook', '#questionamentos', '#Redditum', '#questionmark', '#redditchred', '#askamillionaire', '#redditloseit', '#redditgram', '#QuestionEverythingDontBeStupid', '#questionedisguardi', '#QuestionOfTheDay', '#asking', '#questionsanswered', '#questionable', '#questionsthatneedanswers', '#reddit', '#askingforafriend', '#redditstreetwear', '#reddittphotography', '#askailesi', '#ask2020', '#askforhelp', '#AskAboutMe', '#redditanalog', '#redditmua', '#reddititap', '#questionsoflife', '#reddit360', '#REDDITO', '#QuestionEverthing', '#ask', '#questioning', '#asketchaday', '#redditbodybuilding', '#redditartistnetwork', '#redditig', '#questionnaire', '#asklaftananlamaz', '#redditmag', '#QuestioneDiStile', '#askmehow', '#redditcats', '#askim', '#REDDITOSISTEMATICOERICORRENTE', '#RedditchEyelashExtensions', '#questionablecontent', '#redditmeme', '#askfm', '#questionoflooks', '#redditbb', '#AskForDiamond', '#redditxxfitness', '#askdamz', '#questionauthority', '#questionanswer', '#redditartist', '#askquestions', '#askanyonewhoknows', '#questionaire', '#askmequestions', '#questioneverything', '#QuestionsChallenge', '#AskSquatU', '#askingalexandria', '#asker', '#askyourself', '#askgaryvee', '#questionoftheweek', '#questions', '#askmeanything', '#redditphotography', '#redditmemes', '#question', '#askmore', '#questione', '#redditch', '#questionablycool', '#redditors', '#askeryareni', '#questiontime', '#askbelievereceive', '#questionsandanswers', '#redditt', '#askyfullofstars', '#redditbwf', '#asklisa']
htag_samp = random.sample(hashtag_list,15)
caption = "Put your answers in the comments below. Follow @ask_the_internet for more questions like these daily \n. \n. \n. \n "
for ht in htag_samp:
    caption+=ht +" "

cl = Client()
cl.login(cred.insta_username, cred.insta_password)
cl.album_upload(p_list , caption)

update_posted(post_id)

rm_tree(fpath)