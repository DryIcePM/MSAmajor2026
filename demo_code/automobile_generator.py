from Automobile import Automobile

def main():
    #create instances of automobiles
    auto1 = Automobile("Honda", "Accord", "23456", 2.4, "Alice", 2024, "Blue")
    auto2 = Automobile("Ferrari", "F-50", "12345", 4.8, "Bob", 2022, "Black")

    auto1.__make = "Pontiac"
    auto1.year = 2014
    auto1.make = "Pontiac"
    #change some property values
    auto1.set_color("Grey")
    auto2.set_owner("Charlie")

    #create a list of automobiles 
    auto_list: list[Automobile] = []
    auto_list.append(auto1)
    auto_list.append(auto2)

    #print all automobile data
    for auto in auto_list:
        auto.print_data()

    print(f"Auto1 is {auto1.get_age()} years old")
    print(f"Auto1 make: {auto1.__make}")
main()