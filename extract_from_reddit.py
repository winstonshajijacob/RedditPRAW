import psycopg2
import cred


connection = psycopg2.connect(user=cred.sql_user,
                                      password=cred.sql_password,
                                      host=cred.sql_host,
                                      port=cred.sql_port)
cursor = connection.cursor()
#post and comment processing here

def insertTable(posts,comments):
    
    args_str = ','.join(cursor.mogrify("(%s,%s,%s,%s,%s,%s,%s)", x).decode("utf-8") for x in posts)
    query1 = """INSERT INTO reddit_posts (submission_id,title,author,num_comments,created_timeago,score,upvote_ratio) 
                VALUES """+args_str+ """ON CONFLICT (submission_id) DO UPDATE
                SET num_comments = excluded.num_comments,
                score = excluded.score,
                upvote_ratio = excluded.upvote_ratio"""
    
    args_str1 = ','.join(cursor.mogrify("(%s,%s,%s,%s,%s,%s)", x).decode("utf-8") for x in comments)
    query2 = """INSERT INTO subreddit_comments (submission_id,body,author,timeago,score,comment_id) 
                VALUES """+args_str1+ """ON CONFLICT (comment_id) DO UPDATE
                SET score = excluded.score"""
    
        
    try:
        
        cursor.execute(query1)
        cursor.execute(query2)
        connection.commit()
        
    except (Exception, psycopg2.DatabaseError) as error :
        if(connection):
            print("Error while creating", error)
    
    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def read_table():
    
    query3 = """SELECT * FROM reddit_posts WHERE is_posted ='false' AND upvote_ratio::int > 60 ORDER BY score::int DESC LIMIT 1;"""
    try:
        
        cursor.execute(query3)
        data = cursor.fetchall()
        
        
    except (Exception, psycopg2.DatabaseError) as error :
        if(connection):
            print("Error while fetching", error)
    
    # finally:
    #     #closing database connection.
    #     if(connection):
    #         cursor.close()
    #         connection.close()
    #         print("PostgreSQL connection is closed")
    
    return data

def read_comments(sub_id):
    
    query4 = """SELECT * FROM subreddit_comments WHERE submission_id = """+sub_id+""" ORDER BY score::int DESC LIMIT 8;"""
    try:
        cursor.execute(query4)
        data1 = cursor.fetchall()
        
        
    except (Exception, psycopg2.DatabaseError) as error :
        if(connection):
            print("Error while fetching", error)
    
    # finally:
    #     #closing database connection.
    #     if(connection):
    #         cursor.close()
    #         connection.close()
    #         print("PostgreSQL connection is closed")
    
    return data1

def update_posted(col):
    query4 = """UPDATE reddit_posts set is_posted = true where submission_id = """+col+""";"""
    try:
        
        cursor.execute(query4)
        connection.commit()
        
        
    except (Exception, psycopg2.DatabaseError) as error :
        if(connection):
            print("Error while fetching", error)
    
    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


