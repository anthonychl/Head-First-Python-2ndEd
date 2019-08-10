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

if __name__ == '__main__': 
    app.run(debug=True)
"""
    this last 'if' statement makes sure that 'app.run()' is never executed when the webapp's
    code is imported (as a module)

    if we deploy the webapp to the cloud for example in PythonAnywhere, it imports the webapp's code
    and executes it's own 'app.run()' statement so to speak, so if it encounters the 'app.run()'
    statement in our code it wont work
    So instead of having two versions of the code, one for the cloud without the 'app.run()' statement
    and one with it for development in our local machine/server,
    we use the 'dunder name dunder main' as this --> if __name__ == '__main__':
    is affectionately called.
    
    __name__ is equal to '__main__' if it's executed directly by Python
    __name__ is equal to 'the name of the module imported' if it's imported to some other code 
                          in this case the module name would be 'vsearch4web'
"""