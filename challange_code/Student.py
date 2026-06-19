class Student():
    def __init__(self, firstname, lastname, major, hours, gpa, id):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__major = major
        self.__credit_hours = hours
        self.__gpa = gpa
        self.__id = id

    def get_id(self):
        return self.__id
    
    def get_firstname(self):
        return self.__firstname
    
    def set_firstname(self, new_name:float):
        self.__firstname = new_name
    
    def get_lastname(self):
        return self.__lastname
    
    def set_lastname(self, new_lastname:float):
        self.__lastname = new_lastname

    def get_major(self):
        return self.__major
    
    def set_major(self, new_major:float):
        self.__major = new_major

    def get_gpa(self):
        return self.__gpa
    
    def set_gpa(self, new_gpa:float):
        self.__gpa = new_gpa

    def get_credit_hours(self):
        return self.__credit_hours
    
    def set_credit_hours(self, new_hours:float):
        self.__credit_hours = new_hours

    def print_data(self):
        print(f"{self.__firstname} {self.__lastname} {self.__major}")
        print(f"Hours: {self.__credit_hours} GPA: {self.__gpa}")
        print(f"ID: {self.__id}")
    
    def get_class_level(self):
        if self.__credit_hours >= 0 and self.__credit_hours <= 30:
            return "Freshman"
        if self.__credit_hours > 30 and self.__credit_hours <= 60:
            return "Sophomore"
        if self.__credit_hours > 60 and self.__credit_hours <= 90:
            return "Junior"
        if self.__credit_hours > 90:
            return "Senior"
        
    def update_credit_hours(self, additional_hours):
        self.__credit_hours = additional_hours + self.__credit_hours
