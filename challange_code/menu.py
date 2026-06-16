#print text that reads Item:
#move down a line between the prompt and the beginning text
#Prompt the user to enter a word
def main():


    #define the total of 0 at the beginning
    total = 0
    #define the possible inputs
    #plug in their money values
    menu_items = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    for item in menu_items:
        print(f"{item}: ${menu_items[item]:.2f}")

    #If the input is not supported, ignore and request input again (including uncapitalized words)
    #When a supported value is entered, take its price and add it to the total
    #keep using the same total and don't undo previous inputs
    while(True):
        try:
            selection = input("Item:\n")
            if selection in menu_items.keys():
                total += menu_items[selection]
                print(f"Total: ${total:.2f}")
            if selection.lower() == "end":
                break
        except:
            continue




    #continue until user enters END in any way



main()





























