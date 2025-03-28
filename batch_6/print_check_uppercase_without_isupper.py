# Get user input
text = input("Enter a string: ")
# Initialize a flag variable
all_uppercase = True
# Iterate through each character in the string
for char in text:
    # Check if the character is a letter and not uppercase using ASCII values
    if 'a' <= char <= 'z':
        all_uppercase = False
        break
# Print the result