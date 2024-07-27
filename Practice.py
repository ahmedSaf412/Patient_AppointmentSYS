

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')#index or root or base directory (if yuou visit the root website you uwill se what is down\/\/\/
#((decorater)) to provie additional functionalyty to an existing function

#we have a fun -> basic function but this thing will make it special


def welcome():
    suff = "this is <strong>Bold</strong> text"
    return render_template('home.html', stuff=suff)

@app.route('/BookApp.html')
def BookApp():
    return render_template('BookApp.html')

@app.route('/home.html')
def welcome2():
    suff = "this is <strong>Bold</strong> text"
    return render_template('home.html', stuff=suff)

@app.route('/prescriptions.html')
def prescriptions():
    ListOfDict = [
        {'name': 'John', 'age': 30, 'address': 'Highway 37'},
        {'name': 'Mary', 'age': 27, 'address': 'Highway 19'}
    ]
    stuff = "this is <strong>Bold</strong> text"
    return render_template('prescriptions.html', stuff=stuff, ListOfDict=ListOfDict)


#invaliud url
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    

#intenral server err
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500
    

if __name__ == '__main__':
    app.run(debug=True)


'''
 Version conterol

    allows to back up our code 
'''