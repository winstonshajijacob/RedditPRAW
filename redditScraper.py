import praw,timeago,datetime,pandas as pd
from praw.models import MoreComments
reddit = praw.Reddit('askBot')

subreddit = reddit.subreddit('askreddit')
# print(reddit.user.me())
posts = []
sub_comments = []
hot = subreddit.hot(limit=10)
for submission in hot: 
        
    if not submission.stickied:
        submission.comment_sort = 'top'
        # Limit to, at most, 10 top level comments
        submission.comment_limit = 25
        submission.comments.replace_more(limit=0)
        comments = submission.comments
        print(len(comments)) 
        posts.append([submission.id,submission.title,submission.author,submission.num_comments,submission.created_utc,submission.score,submission.upvote_ratio])
        for comment in comments:
        #         if isinstance(comment, MoreComments):
        #                 continue
                sub_comments.append([submission.id,comment.body,comment.author,comment.created_utc,comment.score])

                
posts = pd.DataFrame(posts,columns=['id','title','author','num_comments','created_utc','score','upvote_ratio'])
sub_comments = pd.DataFrame(sub_comments,columns=['id','body','author','created_utc','score'])
# print("The submission id is {}.title:{},author:{},number of comments:{},created time:{},score:{},upvote ratio:{}, url : {},sticky?:{}".format(submission.id,submission.title,submission.author,submission.num_comments,submission.created_utc,submission.score,submission.upvote_ratio,submission.url,submission.stickied))

posts.to_csv("posts.csv")
sub_comments.to_csv("all_comments.csv")


pdate = datetime.datetime.fromtimestamp(submission.created_utc) 
date = datetime.datetime.now()
print (timeago.format(pdate,date))



# print(posts)
