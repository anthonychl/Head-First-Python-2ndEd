from flask import Flask, session

app = Flask(__name__)

app.secret_key = 'YouWillNeverGuessMySecretKey'

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in'

@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in') # use the 'pop' method to remove the 'logged_in' key from the session dict
    return 'You are logged out'

@app.route('/status')
def check_status() -> str:
    if 'logged_in' in session: # if the 'logged_in' key exists in the session dict: do the line below
        return 'You are currently logged in'
    return 'You are NOT logged in' # if the 'logged_in' key does not exists do this


@app.route('/')
def hello() -> str:
    return 'Hello from the simple webapp'

@app.route('/page1')
def page1() -> str:
    return 'This is page 1'

@app.route('/page2')
def page2() -> str:
    return 'This is page 2'

@app.route('/page3')
def page3() -> str:
    return 'This is page 3'

if __name__ == '__main__':
    app.run(debug=True)
