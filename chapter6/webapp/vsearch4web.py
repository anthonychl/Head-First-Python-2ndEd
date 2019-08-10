# doing the webapp

from flask import Flask, render_template, request, escape
from vsearch import search4letters

app = Flask(__name__)

@app.route('/viewlog')
def view_the_log() ->str:
    with open('vsearch.log') as log:
        contents = log.read()
        return contents

def log_request(req: 'flask_request', res: str) -> None: # saving logs to a file. 'flask_request' is just an annotation not actual excutable code you can write anything instead 'cause python skips over it. 'None' is an annotation to indicate the function has no return value
    with open('vsearch.log','a') as log:
        print(req, res, file = log)

@app.route('/search4', methods=['POST'])  
def do_search() ->'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results'
    results = str(search4letters(phrase,letters)) 
    log_request(request, results) # a call to log_request(), saving this search in the logs file
    return render_template('results.html', the_title = title, the_phrase = phrase,
                                         the_letters = letters,the_results = results) 


@app.route('/') # a function can have multiple URL's so we add it here, and eliminate the function using redirect
@app.route('/entry')
def entry_page() ->'html':
    return render_template('entry.html',the_title = 'Welcome to search4letters on the Web!')

if __name__ == '__main__': 
    app.run(debug=True)