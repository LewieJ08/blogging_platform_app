from dotenv import load_dotenv
import psycopg2
import os 

load_dotenv()

host = os.getenv("HOST")
dbname = os.getenv("DBNAME")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
port = os.getenv("PORT")

def get_connection():
    return psycopg2.connect(host=host, dbname=dbname, user=user, password=password, port=port)

def init_database():
    with open("schema.sql", "r") as file:
        schema = file.read()

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(schema)
            conn.commit()

def get_all_posts():
    with open("queries/get_all_posts.sql") as file:
        query = file.read()
    
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query) 
            return cur.fetchall()
        
def get_post_by_id(post_id):
    with open("queries/get_post_by_id.sql") as file:
        query = file.read()
    
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query,(post_id,)) 
            return cur.fetchall()


def create_post(title,content,category,tags):
    with open("queries/create_post.sql","r") as file:
        query = file.read()

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query,(title,content,category,tags))
            conn.commit()

def update_post(title,content,category,tags,post_id):
    with open("queries/update_post.sql","r") as file:
        query = file.read()

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query,(title,content,category,tags,post_id))
            conn.commit()

def delete_post(post_id):
    with open("queries/delete_post.sql") as file:
        query = file.read()

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query,(post_id,)) 
            conn.commit()

    