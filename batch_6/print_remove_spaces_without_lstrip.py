# Get user input
user_input = input("Enter a string with leading spaces: ")
# Initialize an index to keep track of the current character position
index = 0
# Use a while loop to find the first non-space character
while index < len(user_input) and user_input[index] == ' ':
    index += 1   
# Extract the string from the first non-space character
# Print the result