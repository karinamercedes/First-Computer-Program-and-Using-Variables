# Request user's name using input()
# Store the information as "name"
# Request user's age using input()
# Store the information as "age"
# Request user's house number using input()
# Store the information as "house_number"
# Request user's street name using input()
# Store the information as "street_name"
# Print a single sentence containing all the details

name = input("Enter your full name: ")
age = input("Enter your age: ")
house_number = input("Enter your house number: ")
street_name = input("Enter your street name: ")
print("This is " + str.title(name) + ". He is " + str(age) + " years old and lives at house number " + str(house_number) + " on " + str.title(street_name) , end=".")