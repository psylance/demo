# Displays name of last person added in the database

from flask import Flask
import MySQLdb

app = Flask(__name__)
db=MySQLdb.connect('139.180.137.65', 'user', 'pass', 'k3s')


@app.route('/')
def index():
    cur=db.cursor()
    cur.execute("""SELECT name FROM persons ORDER BY ID DESC LIMIT 1""")
    result = cur.fetchall()
    
    return 'The last person added in the database was ' + result[0][0]

        
