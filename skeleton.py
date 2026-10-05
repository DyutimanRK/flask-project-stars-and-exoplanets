from flask import Flask

app = Flask(__name__) #an instance of the flask class has been created, this will act as a web server gateway interface application (WSGI)

@app.route('/') #this is the homepage. The following function gets executed
def welcome():
    return 'Welcome boss!!'

@app.route('/new')
def new():
    return 'Welcome to the new page, boss!!'


if __name__=='__main__':
    app.run(debug=True) #debug=True automatically restarts the server if any change is made to the code and saved