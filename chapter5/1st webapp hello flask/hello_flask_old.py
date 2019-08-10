# the most basic of Flask webapps

from flask import Flask

app = Flask(__name__) # create an instance of a Flask object and assign it to 'app'

@app.route('/')  # URL associated with the function below
def hello() ->str:
    return 'Hello world from Flask'

app.run() # ask Flask to start its web server, the webapp starts running