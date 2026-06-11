#Input values can only be accepted if they are the numbers 1, 5, 10, or 25
#Prompt user to enter a coin by detailing the words Vending Machine, separating the text with dashes and then prompting for user input 
print(f"Vending Machine\n------------------------")
amount_due = 50





#make a function so the program validates the input based on the accepted values
#create a while-loop to continue to prompt the user without subtracting from the total if the input is not valid
while(true):
    try:
        coin_inserted = int(input("Insert Coin"))
        if coin_inserted != 5 or coin_inserted != 1 or coin_inserted != 10 or coin_inserted != 25:
        
            break






#make a function that subtracts values from the total cost of 50
#continue until the total amount dued reaches zero




#make a function to grant extra change if the final input puts the total dued below zero.












main()