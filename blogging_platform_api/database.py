from dotenv import load_dotenv
import psycopg2
import os 

load_dotenv()

host = os.getenv("HOST")
dbname = os.getenv("DBNAME")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
port = os.getenv("PORT")

conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password, port=port)

