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
    student_dictionaries = sg.get_student_dictionaries()
    list_of_results = []

    for student_dict in student_dictionaries:
        if student_dict[search_key].lower() == search_value.lower():
            list_of_results.append(student_dict)
    return list_of_results

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
#api/majors/education
@app.route('/api/major/<string:major>', methods = ['GET'])
def api_students_by_major(major:str):
    major_students = search_dictionary_list("major", major)
    return jsonify(major_students)

#create a route that returns students of a specific class
# api/class/class we are looking for
@app.route('/api/class/<string:student_class>', methods=['GET'])
def api_students_by_class(student_class:str):
    #call the search function to get the students from that class
    class_students = search_dictionary_list("class", student_class)
    return jsonify(class_students)
#create a route that returns a specific student by id
@app.route('/api/student/id/<string:id>', methods = ['GET'])
def api_get_student_by_id(id:str):
    student = search_dictionary_list("id", id)
    return jsonify(student)

#create a route to return a list of unique majors
@app.route('/api/majors/all', methods=['GET'])
def get_all_majors():
    #create a empty list to store the majors
    major_list = []
    #get a list of student dictionaries
    student_dictionaries = sg.get_student_dictionaries()
    #use a for loop to iterate through the student list
    for student in student_dictionaries:
        #add the major to the major list if the major isnt already in the list
        if student['major'] not in major_list:
            major_list.append(student['major'])
    #sort the list
    major_list.sort()
    #return the list
    return major_list

#run the application
app.run(debug=True)

