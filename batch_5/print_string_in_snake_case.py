# Ask the user to enter their name
full_name = input("Enter your full name: ")
# Use the 'lower()' method to convert the string into all lower case
full_name = full_name.lower()
# Use the 'replace()' method to replace the spaces with underscores
full_name = full_name.replace(" ", "_")
# Print the modified string
print(full_name)