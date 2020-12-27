import praw,timeago,datetime
from praw.models import MoreComments
from extract_from_reddit import insertTable



#ini
reddit = praw.Reddit('askBot')

subreddit = reddit.subreddit('askreddit')
# print(reddit.user.me())

#Convert timestamp to timeago
def t_ago(time):
    pdate = datetime.datetime.fromtimestamp(time) 
    date = datetime.datetime.now()
    return (timeago.format(pdate,date))

    
posts = []
p_comments = []
hot = subreddit.hot(limit=25)
for submission in hot: 
        
    if not submission.stickied:
        submission.comment_sort = 'top'
        # Limit to, at most, 25 top level comments,we use 25 because MoreComment Instances are counted too
        submission.comment_limit = 25
        submission.comments.replace_more(limit=0)
        comments = submission.comments
        # print(len(comments)) 
        posts.append((str(submission.id),submission.title,submission.author.name,str(submission.num_comments),t_ago(submission.created_utc),str(submission.score),str(int(submission.upvote_ratio * 100))))
        for comment in comments:
            if len(comment.body) > 600:
                continue
            if comment.author is None: 
                c_name = "deleted"
                continue
            c_name = str(comment.author.name)
            p_comments.append((submission.id,comment.body,c_name,t_ago(comment.created_utc),str(comment.score),comment.id))
insertTable(posts,p_comments)


