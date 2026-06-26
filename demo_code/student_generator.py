from Student import Student
from datetime import datetime

"""
Function to write an error message to a log file
input: string error message
output: none
"""
def write_to_error_log(message:str) -> None:
    the_date = datetime.now()
    #open the log file in append mode:error_log.txt
    with open("error_log.txt", "a") as log_file:
        log_file.write(f"{the_date}: {message}\n")
        #write an error message to the file in the format
        #6/26/2026: Error in data file on line 5
    return

"""
Function to return a list of student objects
input: none
output: list of student objects
"""
def load_students() -> list[Student]:

    #open the csv file
    data_file = open("students.csv", "r")
    print(data_file)
    students = []

    #use a loop to read the file contents line by line
    for line_of_data in data_file:
            
            #split the lines at their commas
            student_and_student_info = line_of_data.split(",")
            try:
    #get the student and their info from the list
                kid = Student(student_and_student_info[0],student_and_student_info[1],student_and_student_info[2],float(student_and_student_info[3]),float(student_and_student_info[4]),student_and_student_info[5])    
            except:
                continue
        #create an entry in the dictionary for the student and their info
            students += [kid]

    #close the file
    data_file.close()
    return students

"""
Function to convert student objets into student dictionaries
Input: list of student objects
output: list of student dictionaries
"""
def student_to_dictionary(list_of_students: list[Student]) -> list[dict]:
    #create an empty list to store the dictionaries
    student_dictionary_list = []

    #loop through the list and write each students data to a dictionary
    for student in list_of_students:
        #create an empty dictionary
        #make entries into the dictionary using the student properties
        #firstname, lastname, major, gpa, class, id
        student_dictionary = {}
        student_dictionary['first_name'] = student.get_firstname()
        student_dictionary['last_name'] = student.get_lastname()
        student_dictionary['major'] = student.get_major()
        student_dictionary['gpa'] = student.get_gpa()
        student_dictionary['class'] = student.get_class_level()
        student_dictionary['ID'] = student.get_id()

        #append the dictionary to the list of dictionaries
        student_dictionary_list.append(student_dictionary)
    #return the list of dictionaries
    return student_dictionary_list
"""
Function to get student dictionaries
input:none
output:a list of student dictionaries
"""
def get_student_dictionaries():
    #get a list of students
    student_list = load_students()

    #get a list of student dictionaries
    student_dictionaries = student_to_dictionary(student_list)

    return student_dictionaries
