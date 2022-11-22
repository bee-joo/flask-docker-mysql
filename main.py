import os
from database import Database
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)
db = Database(host=os.environ['MYSQL_HOST'],
              user=os.environ['MYSQL_USER'],
              password=os.environ['MYSQL_PASSWORD'],
              db="inventory"
)

import router

if __name__ == '__main__':
    db.initdb() 
    app.run(host='0.0.0.0', port=80)