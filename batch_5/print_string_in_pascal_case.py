# Ask the user to enter their name
full_name = input("Please enter your full name: ")
# Use the 'title()' method to capitalize the first letter of each word in the name
full_name = full_name.title()
# Use the 'replace()' method to replace the spaces to empty string
pascal_name = full_name.replace(" ", "")
# Print the formatted name