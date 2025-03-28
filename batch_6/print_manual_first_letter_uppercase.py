# Get user input
text = input("Enter a string: ")
# Check if the string is not empty
if text:
    # Convert the first character to uppercase using ASCII adjustment if it's a lowercase letter
    if 'a' <= text[0] <= 'z':
        first_char = chr(ord(text[0]) - 32)
    else:
        first_char = text[0]
    # Convert the remaining characters to lowercase using a loop
            # Convert to lowercase using ASCII adjustment
    # Combine the first character and the rest of the string
# Print the result