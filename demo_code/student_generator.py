from Student import Student

def main(file_name):

    #open the csv file
    data_file = open(file_name, "r")
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
student = main("students.csv")

for kid in student:
     kid.print_data()

