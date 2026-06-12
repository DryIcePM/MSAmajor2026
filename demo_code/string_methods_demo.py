def main():
    my_name = "parker"

    # capitalize a string
    print(f"\nMy name capitalized: {my_name.capitalize()}")

    # make a string uppercase
    print(f"\nMy name uppercase: {my_name.upper()}\n")

    # make a string lowercase
    last_name = "MARSHALL"
    print(f"My full name lowercase: {my_name.lower()} {last_name.lower()}\n")

    # compare two strings
    my_name_title_case = "Parker"
    if my_name.lower() == my_name_title_case.lower():
        print("The strings are equal.\n")
    else:
        print("The strings are not equal.\n")
    print("\nUsing the startswith method\n----------------------------------")
    #determine if a string starts with a set of characters 
    print(f"\n{my_name} starts with a P or p: {my_name.startswith("P") or my_name.startswith("p")}\n")
    

    if(not my_name.startswith("Park") and (not my_name.startswith("park"))):
        print(f"You spelled {my_name} incorrectly.")
    else:
        print(f"You spelled {my_name} correctly.")

    if((not my_name.lower().startswith("park"))):
        print(f"You spelled {my_name} incorrectly.")
    else:
        print(f"You spelled {my_name} correctly.")

    print("\nUsing the endswith method\n----------------------------------")
    print(f"{my_name} ends with 'er': {my_name.endswith('er')}")

    print("\nUsing the find method\n----------------------------------")
    # find the k in parker
    search_letter = "ker"
    index_of_substring = my_name.find(search_letter)
    if index_of_substring != -1:
        print(f"the '{search_letter}' is at index {index_of_substring} in {my_name}")
    else:
        print(f"there is no '{search_letter}' in {my_name}")


    print("\nLooping through a string\n---------------------------")
    for letter in my_name:
        print(letter)
    print(f"{my_name} has {len(my_name)} letters.")
    #print the letters in a string along with the index positions
    for letter_index in range(len(my_name)):
        print(f"Letter {letter_index + 1}: {my_name[letter_index]}")

    print("\nSearch a string\n-----------------")
    sentence = "I have a dog. My dog is cute. Do you want a dog?"
    #write code that counts the number of dogs in the sentence
    #expected output: 3
    search_word = "dog"
    start_index = 0
    number_of_dogs = 0
    while True:
        #Start at the beginning of the string 
        #search for the occurence of the word dog starting at indx 0
        dog_index = sentence.find(search_word, start_index)
        #if we find dog, add one to  some variable we use to keep track of the the number of dogs we find
        #continue searching the string from the next index after the dog we just found
        #update the starting index by one
        if dog_index == -1:
            break
        else:
            #number_of_dogs = number_of_dogs + 1
            number_of_dogs += 1
            start_index = dog_index + 1
    print(f"There are {number_of_dogs} {search_word}(s) in the sentence.")
    


main()