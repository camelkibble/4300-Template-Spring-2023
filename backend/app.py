import json
import os
from flask import Flask, render_template, request
from flask_cors import CORS
from helpers.MySQLDatabaseHandler import MySQLDatabaseHandler
from random import randint


# ROOT_PATH for linking with all your files. 
# Feel free to use a config.py or settings.py with a global export variable
os.environ['ROOT_PATH'] = os.path.abspath(os.path.join("..",os.curdir))

# These are the DB credentials for your OWN MySQL
# Don't worry about the deployment credentials, those are fixed
# You can use a different DB name if you want to
MYSQL_USER = "root"
MYSQL_USER_PASSWORD = ""
MYSQL_PORT = 3306
MYSQL_DATABASE = "CityFood"

mysql_engine = MySQLDatabaseHandler(MYSQL_USER,MYSQL_USER_PASSWORD,MYSQL_PORT,MYSQL_DATABASE)

# Path to init.sql file. This file can be replaced with your own file for testing on localhost, but do NOT move the init.sql file
mysql_engine.load_file_into_db()

app = Flask(__name__)
CORS(app)

# Sample search, the LIKE operator in this case is hard-coded, 
# but if you decide to use SQLAlchemy ORM framework, 
# there's a much better and cleaner way to do this
def sql_search(episode):
    query_sql = f"""SELECT * FROM episodes WHERE LOWER( title ) LIKE '%%{episode.lower()}%%' limit 10"""
    keys = ["id","title","descr"]
    data = mysql_engine.query_selector(query_sql)
    return json.dumps([dict(zip(keys,i)) for i in data])

@app.route("/")
def home():
    return render_template('base.html',title="sample html")

@app.route("/episodes")
def episodes_search():
    text = request.args.get("title")
    return sql_search(text)

@app.route('/main')
def main():
    return render_template('main.html')

def give_random_restaurant(restaurants):
    keys = ["business_id","name","address","city","state","postal_code","latitude","longitude","stars", "review_count", "is_open", "attributes" , "categories" , "hours" ]
    # a random restaurant is selected from the list of restaurants
    random_num = randint(0,len(restaurants)-1)
    return [dict(zip(keys,[str(j) for j in i])) for i in restaurants][random_num]
    # return [dict(zip(keys,[str(j) for j in i])) for i in restaurants][0]

@app.route('/random')
def random():
    restaurants = list(mysql_engine.query_selector("SELECT * FROM restaurant"))
    random_restaurant = give_random_restaurant(restaurants)
    print(random_restaurant)
    # random_restaurant_name = random_restaurant["name"]
    return json.dumps({"restaurant": random_restaurant })

# app.run(debug=True)