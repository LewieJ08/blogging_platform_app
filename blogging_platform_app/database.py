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

def create_post(title,content,category,tags):
    with open("queries/create_post.sql","r") as file:
        query = file.read()

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query,(title,content,category,tags))
            conn.commit()