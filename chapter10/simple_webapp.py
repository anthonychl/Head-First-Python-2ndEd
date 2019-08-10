from flask import Flask, session

from checker import check_logged_in #import our module and decorator function

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

@app.route('/')
def hello() -> str:
    return 'Hello from the simple webapp'

@app.route('/page1')
@check_logged_in  #using our decorator to check for login status
def page1() -> str:
    return 'This is page 1'

@app.route('/page2')
@check_logged_in  #using our decorator to check for login status
def page2() -> str:
    return 'This is page 2'

@app.route('/page3')
@check_logged_in #using our decorator to check for login status
def page3() -> str:
    return 'This is page 3'

if __name__ == '__main__':
    app.run(debug=True)
