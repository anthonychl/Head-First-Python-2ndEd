# doing the webapp

from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)

@app.route('/search4', methods=['POST'])  
def do_search() ->'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results'
    results = str(search4letters(phrase,letters)) 
    return render_template('results.html', the_title = title, the_phrase = phrase,
                                         the_letters = letters,the_results = results) 


@app.route('/') # a function can have multiple URL's so we add it here, and eliminate the function using redirect
@app.route('/entry')
def entry_page() ->'html':
    return render_template('entry.html',the_title = 'Welcome to search4letters on the Web!')

app.run()