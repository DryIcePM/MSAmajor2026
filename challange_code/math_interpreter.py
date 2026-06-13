#while loop
while True:
    #Input
    #prompt user
    expression = input("Enter an expression (X Y Z): ")
    #Process
    #validate the expression format 
    #use the split method to split the expression to at the space
    expression_split = expression.split(" ")
    #if the length of the resulting list is not 3 then invalid format
    if(len(expression_split) != 3):
        print(f"Invalid format")
        continue
    #validate that x and z are integers
    #convert to int
    try:
        x = int(expression_split[0])
        z = int(expression_split[2])
    except: 
        print(f"Invalid format")
        continue
    #if conversion causes an exception, then incorrect format

    #validate that y is an acceptable operator (+, -, *, /)
    #use an if statement to determine if y == the symbols
    #invalid format if not

    #validate that when y = /, z != 0
    #use if statement: if y == / and z == 0, invalid format

    #do the math


    #Output
    #print the answer
    #ask to do it again