from flask import Flask, request
from database import MySQL
from dotenv import load_dotenv
from config import *

#Initialize Flask and sets our secret key.
app = Flask(__name__)
app.secret_key = SECRET_KEY

#Turns debug on if we're in our development environment.
if ENVIRONMENT == 'dev':
    app.debug = True

app.db = MySQL(MYSQLHOST, MYSQLUSER, MYSQLPASS, MYSQLDB)

@app.context_processor
def inject_settings() -> dict:
    """
    Sets our global settings from our database
    """
    query = app.db.query('SELECT * from settings', querytype='select', fetchall=False)
    settings = {
        'settings': query,
    }
    return settings

@app.route('/')
def index():
    try:
        API_KEY = request.get_json()['API_KEY']
    except:
        return {'Status': 'Failed', 'Reason': 'No API_KEY variable.'}
    apix = app.db.query(f'SELECT owner, apikey FROM `keys` WHERE apikey="{API_KEY}"', querytype='select', fetchall=False)
    if not apix:
        return {'Status': 'Failed', 'Reason': 'Incorrect API_KEY.'}
    products = app.db.query('SELECT * from products')
    return {
        'Status': 'Success',
        'Authorization': apix,
        'Products': products
    }

if __name__=='__main__':
    app.run()