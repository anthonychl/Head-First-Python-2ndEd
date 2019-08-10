# adding functionality with the vsearch module

from flask import Flask
from vsearch import search4letters


app = Flask(__name__)

@app.route('/')
def hello() ->str:
    return 'Hello world from Flask'

@app.route('/search4')  # adding a new URL associated with the function below
def do_search() ->str:
    return str(search4letters('life, the universe and everything','eiru,!')) #convert the set to string with str() as the web browser expects text not Python sets

app.run()