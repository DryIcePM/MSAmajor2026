# Print Hello World
print("Hello World")

# Create a Variable to Store my Name
first_name = "Parker"

# Cretae a Variable for my last name
last_name = "Marshall"

# write a python statement to display "my fullname is firstname lastname"
print("My full name is", first_name, last_name, sep="")

#print using the f string (string interpolation)
print(f"My full name is {first_name} {last_name}.")

#create a variable to store age and weight
age = 16
weight = 172.8
half_age = age / 2

#print a sentence with name, age, and weight
print(f"My name is {first_name} {last_name}.\nI am {age} years old and I weigh {weight}lbs.")

#get and print the data type for age, weight, and half age
print("\nChecking Data Types\n----------------")
print(type(age))
print(type(weight))
print(type(half_age))

#write 3 statements using string interpolation (f string) to print descriptive sentences for the data types
#"variable age is an int"
print(f"Varible age is an int because although it is a number, it does not contain a decimal point like variable weight does.\nDue to the tenths place number in variable weight, it becomes a float.\nFinally, variable half_age is a float because when it divides it gains a decimal in the final answer.")

number_1 = "5"
number_2 = "7"
total = number_1 + number_2
print(f"Total: {total}")

