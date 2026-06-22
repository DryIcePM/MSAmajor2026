import flask
from flask import request, jsonify
import student_generator_v2 as sg

#create a flask app object 
app = flask.Flask(__name__)

#tell the server to reload each time the code changes
#create a route for the home page of the application 
#create endpoint for the functions we will make
#run the application