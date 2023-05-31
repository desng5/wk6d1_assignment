from app import app
from flask import render_template

#instance of the Flask class assigned to variable 'app'


@app.route('/') #get request '/' it will return statement thats within that function.
def home():
       return render_template('index.html')

@app.route('/favs')
def favs():
    dogs = ["Basenji", "Schnauzer", "Pitbulls", "WireFox Terriers", "Bull Terriers"]
    return render_template('favs.html', dogs=dogs)