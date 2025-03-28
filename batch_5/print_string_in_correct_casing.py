# Ask the user to input their name in incorrect casing
full_name = input("Enter your name in wrong capitalization: ")
# Use the 'split()' method to convert each part to each independent string and store it in a list
name_parts = full_name.split()
# Initializing a new list for correct capitalization
new_parts = []
# Itterate through the list and use the 'capitalize()' method to convert the stings into their correct casing
for part in name_parts:
    new_parts.append(part.capitalize())
# Use the 'join()' method with an empty space to join the each string with spaces
modified_name = " ".join(map(str, new_parts))
# Print the modified string
print(modified_name)