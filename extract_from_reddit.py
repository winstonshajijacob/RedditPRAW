import psycopg2
import cred


connection = psycopg2.connect(user=cred.sql_user,
                                      password=cred.sql_password,
                                      host=cred.sql_host,
                                      port=cred.sql_port)
#post and comment processing here

def insertTable(parameters):
    
    try:
        
        cursor = connection.cursor()
        #SQL UPSERT STATEMENT HERE
        upsert_post_query = """  INSERT INTO the_table (id, column_1, column_2) 
                            VALUES (1, 'A', 'X'), (2, 'B', 'Y'), (3, 'C', 'Z')
                            ON CONFLICT (id) DO UPDATE 
                            SET column_1 = excluded.column_1, 
                            column_2 = excluded.column_2; """
    
        upsert_comments_query = """  INSERT INTO the_table (id, column_1, column_2) 
                            VALUES (1, 'A', 'X'), (2, 'B', 'Y'), (3, 'C', 'Z')
                            ON CONFLICT (id) DO UPDATE 
                            SET column_1 = excluded.column_1, 
                            column_2 = excluded.column_2; """
        
    
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
    print("read and update")
