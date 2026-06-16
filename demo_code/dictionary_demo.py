def main():
    #the need for dictionaries
    scores = [55, 75, 87, 82, 91]
    students = ["Alice", "Bob", "Jerry", "Jane", "Bill"]

    #print the names of the students with their scores 
    print("Students and scores using the lists\n------------------------")
    for index in range(len(scores)):
        print(f"{students[index]}: {scores[index]}")

    #create a dictionary of names and scores
    student_scores = {
        "Alice": 55,
        "Bob": 75,
        "Jerry": 87,
        "Jane" : 82,
        "Bill": 91
    }

    # print bob and janes scores
    print("\nPrint Bob and Janes Scores\n--------------------")
    print(student_scores["Bob"])
    print(student_scores["Jane"])



    #print all the data in the student scores dictionary
    print("\nprint all students data\-------------")
    for student in student_scores:
        print(f"{student}: {student_scores[student]}")

    #Create a dictionary to store car info
    #make, model, year, value, engine size
    car_1 = {"make": "Ferrari", "model": "F-50", "year": "2024", "value": "500000", "engine size": "4.8"}
    print("\nGet all car info\n------------------")
    for key, value in car_1.items():
        print(f"{key}: {value}")

    #create a second car
    car_2 = {"make": "Honda", "model": "accord", "year": "2024", "value": "18000", "engine size": "2.4"}
    car_1["transmission"] = "manual"
    car_2["transmission"] = "automatic"
    dictionary_list = [car_1, car_2]



    #Display info for all cars
    print("\nDisplay info for all cars\n--------------")

    #loop over all the cars
    for car in dictionary_list:
        print("\nCar Info\n-------------------")

        #loop over the items in the dictionary
        for feature, value in car.items():
            print(f"{feature}: {value}")

    #create a dictionary of dictionaries
    car_dictionary = {"Ferrari": car_1, "Honda": car_2}

    #Print all car info from the dictionary
    print("\nCar info from dictionaries\n--------------")

    for make, car in car_dictionary.items():
        print(f"\n{make}")
        for feature, value in car.items():
            print(f"{feature}: {value}")

    #Getting a value from a dictonary when no key exists
    key = "Transmission"
    car_1.keys()
    try:
        print(f"{car_1["key"]}")
    except:
        print(f"ERROR: {key} key does not exist in the dictionary")

    if key not in car_1.keys():
        print(f"ERROR: {key} key does not exist in the dictionary")
    else: 
        print(f"{car_1["key"]}")






main()
