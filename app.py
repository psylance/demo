# Displays name of last person added in the database

from flask import Flask
import MySQLdb

app = Flask(__name__)
db=MySQLdb.connect('45.77.34.140', 'user', 'pass', 'k3s')


@app.route('/')
def index():
    cur=db.cursor()
    cur.execute("""SELECT name FROM persons ORDER BY ID DESC LIMIT 1""")
    result = cur.fetchall()
    
    return 'The last person added in the database was ' + result[0][0]

        
