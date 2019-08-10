# doing the webapp

from flask import Flask, render_template, request, escape 
from vsearch import search4letters

app = Flask(__name__)

@app.route('/viewlog')
def view_the_log() ->str:
    with open('vsearch.log') as log:
        contents = log.read()
        return escape(contents) 

def log_request(req: 'flask_request', res: str) -> None: 
    with open('vsearch.log','a') as log:
        print(req.form, file = log, end ='|') # saving more useful info to the file: the form data. each of the ' end ='|' replace the default 'newline' with the vertical bar as the end-of-line value
        print(req.remote_addr, file = log, end ='|') # saving the ip address
        print(req.user_agent, file = log, end ='|')  # the browser
        print(res, file = log) # the results

@app.route('/search4', methods=['POST'])  
def do_search() ->'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results'
    results = str(search4letters(phrase,letters)) 
    log_request(request, results) 
    return render_template('results.html', the_title = title, the_phrase = phrase,
                                         the_letters = letters,the_results = results) 


@app.route('/')
@app.route('/entry')
def entry_page() ->'html':
    return render_template('entry.html',the_title = 'Welcome to search4letters on the Web!')

if __name__ == '__main__': 
    app.run(debug=True)