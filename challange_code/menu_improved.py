#Function to load data from a data file and return a dictionary
#Input: filename: string
#Output: dictionary




def load_menu_items(filename:str) -> dict:
    #open menu.txt, create a file handler to open file in read mode
    data_file = open(filename, "r")
    print(data_file)
    #create an empty dictionary
    menu_items = {}
    #use a loop to read the contents of the file line by line
    for line_of_data in data_file:
        #split the line at the comma
        item_name_and_price = line_of_data.split(",")
        print(item_name_and_price)
        #get the item and price from the list
        item_name = item_name_and_price[0]
        item_price = float(item_name_and_price[1])
        #create an entry in the dictionary for the item and price
        menu_items[item_name] = item_price
    #close the file
    data_file.close()

    #return the dictionry of menu_items
    return menu_items


def main():
    total = 0
    menu_items = load_menu_items("menu_items.txt")


    for item in menu_items:
        print(f"{item}: ${menu_items[item]:.2f}")
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

main()