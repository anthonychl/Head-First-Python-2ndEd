# this is the version of the webapp that makes users wait

from flask import Flask, render_template, request, escape, session
from flask import copy_current_request_context
'''
copy_current_request_context
A helper function that decorates a function to retain the current request context.
The moment the function is decorated a copy of the request context is created
and then pushed when the function is called.

ensures that the HTTP request that is active when a function is called remains active
even when the function is subsequently executed in a thread. However the function being
decorated has to be defined within the function that calls it.
The decorated function must be nested inside its caller(as an inner function)
'''

from vsearch import search4letters
from DBcm import UseDatabase, ConnectionError, CredentialsError, SQLError
from checker import check_logged_in

from time import sleep


app = Flask(__name__)

app.secret_key = 'YouWillNeverGuessMySecretKey'

app.config['dbconfig'] = { 'host':'127.0.0.1', 'user':'vsearch',
                            'password':'vsearchpasswd', 'database': 'vsearchlogDB', }

@app.route('/')
@app.route('/entry')
def entry_page() ->'html':
    return render_template('entry.html',the_title = 'Welcome to search4letters on the Web!')

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in'

@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in') 
    return 'You are logged out'

@app.route('/search4', methods=['POST'])  
def do_search() ->'html':
    @copy_current_request_context # copying the request data to the inner function below for its use
    def log_request(req: 'flask_request', res: str) -> None:
        sleep(15) #this makes log_request really slow... this is for the example purpose only
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """ insert into log (phrase, letters, ip, browser_string, results)
                    values(%s, %s, %s, %s, %s) """
            cursor.execute(_SQL, (req.form['phrase'],
                                req.form['letters'],
                                req.remote_addr,
                                req.user_agent.browser, res,))

    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results'
    results = str(search4letters(phrase,letters))
    try:
        log_request(request, results) 
    except Exception as err:
        print('***** Loggin failed with this error ', str(err))
    return render_template('results.html', the_title = title, the_phrase = phrase,
                                         the_letters = letters,the_results = results) 

@app.route('/viewlog')
@check_logged_in # <=== our decorator to restrict access to this page
def view_the_log() ->'html':
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """ select phrase, letters, ip, browser_string, results from log """
            cursor.execute(_SQL)
            contents = cursor.fetchall()
        titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
        return render_template('viewlog.html', the_title='View Log', the_row_titles= titles,the_data= contents)
    except ConnectionError as err:
        print('Is your database switched on? ', str(err))
    except CredentialsError as err:
        print('User-ID/Password issues. Error: ', str(err))
    except SQLError as err:
        print('Is your query correct?. Error: ', str(err))
    except Exception as err:
        print('Something went wrong: ', str(err))
    return 'Error'


if __name__ == '__main__': 
    app.run(debug=True)