# doing the webapp

from flask import Flask, render_template, request, redirect
"""
render_template : is for managing the templates. it returns a string of HTML when invoked,
                  provided with the name of a template and any required arguments

request : is for managing the form's data sent (via POST in this case)

redirect : is for redirecting from one page to another

"""
from vsearch import search4letters

app = Flask(__name__)

@app.route('/') # redirecting to 'localhost:5000/entry' from 'localhost:5000'
def hello() ->'302': # adjust the annotation to indicate what's being returned, 302 is what Flask sends when redirect is invoked
    return redirect('/entry')

@app.route('/search4', methods=['POST']) # route() takes another argument 'methods' which specifies the method used to handle the data that has been sent, it takes 'GET" as the default value
def do_search() ->'html': # the annotation indicates this function returns HTML, not a string  
    phrase = request.form['phrase'] # assign the form's data to the variables 'phrase' and 'letters', from the html input tags of the same name in the form
    letters = request.form['letters']
    title = 'Here are your results'
    results = str(search4letters(phrase,letters)) 
    return render_template('results.html', the_title = title, the_phrase = phrase,
                                         the_letters = letters,the_results = results) 
    """
        the arguments in render_template() are first: the html template itself we want to use
        and then: all the values we want to substitute in the template with the same name
        within the doble curly brackets {{ xx_xxxx }}
    """

@app.route('/entry')
def entry_page() ->'html': # the annotation indicates this function returns HTML, not a string
    return render_template('entry.html',the_title = 'Welcome to search4letters on the Web!')


app.run(debug=True)
"""
to improve the efficiency while testing, Flask allows you to run your webapp in debbuging mode
this automatically restarts your webapp every time Flask notice the code has changed
(typically as result of you  making and saving a change)
"""