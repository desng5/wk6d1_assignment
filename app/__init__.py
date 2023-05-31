from flask import Flask

#instance of the Flask class assigned to variable 'app'
app = Flask(__name__)

from app import routes