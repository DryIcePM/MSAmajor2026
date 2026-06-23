import flask
from flask import request, jsonify
import student_generator as sg

#create a flask app object 
app = flask.Flask(__name__)

#tell the server to reload each time the code changes
app.config["DEBUG"] = True

"""
Function to query the list of student dictionaries based on a search key, and a value
Input: search key - key in the dictionary we check the value of
    search value - the value of the key we need to match
output: list of student dictionaries that match the search criteria
"""
def search_dictionary_list(search_key, search_value):
    search_list = []
    for student in sg.get_student_dictionaries():
        if student[search_key] == search_value:
            search_list.append(student)
    return search_list


#create a route/view for the home page of the application 
@app.route('/', methods=['GET'])
def index():
    return "<h1>Student Data API</h1>"

#create endpoint for the functions we will make
#create a route to return student data
@app.route('/api/students/all', methods=['GET'])
def api_all():
    #get student dictionaries
    student_dictionaries = sg.get_student_dictionaries()
    return jsonify(student_dictionaries)

#create a route that returns students in a specific major
#create a route that returns students of a specific class
#create a route that returns a specific student by id

#run the application
app.run(debug=True)
