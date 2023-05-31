from flask import Flask

#instance of the Flask class assigned to variable 'app'
app = Flask(__name__)


@app.route('/') #get request '/' it will return statement thats within that function.
def home():
       return render_template('index.html')

@app.route('/favs')
def favs():
    dogs = ["Basenji", "Schnauzer", "Pitbulls", "WireFox Terriers", "Bull Terriers"]
    return render_template('favs.html', dogs=dogs)