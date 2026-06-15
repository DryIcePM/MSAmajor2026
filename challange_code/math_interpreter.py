while True:
    expression = input("Enter an expression (X Y Z): ")
    expression_split = expression.split(" ")
    if(len(expression_split) != 3):
        print(f"Invalid Format")
        continue
    try:
        x = int(expression_split[0])
        z = int(expression_split[2])
    except: 
        print(f"Invalid Format")
        continue
    y = expression_split[1]
    if(y != "+" and y != "-" and y != "/" and y != "*"):
        print("Invalid Format")
        continue
    if(y == "/" and z == 0):
        print("Divide by Zero Error")
        continue
    if(y == "+"):
        final_answer = (x + z)
    if(y == "-"):
        final_answer = (x - z)
    if(y == "*"):
        final_answer = (x * z)
    if(y == "/"):
        final_answer = (x / z)
    print(f"Answer = {final_answer}")
    answer = input("Would You Like To Enter Another Expression? (Y or N) ")
    if(answer == "Y"):
       continue
    else:
        break
