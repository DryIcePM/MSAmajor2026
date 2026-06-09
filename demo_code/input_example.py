# program to convert lbs to kgs
# INPUT (gettting the data that will be processed)
# Prompt user to enter weight in lbs
user_weight = float(input("Enter weight in pounds: "))

# PROCESSING
# use a conversion factor to convert lbs to kgs (2.205lbs = 1kg)
lbs_to_kg = 2.205
user_weight_in_kg = user_weight / lbs_to_kg

# OUTPUT
# create the output to the user
print(f"You weigh {user_weight_in_kg:.2f} kgs.")