# Get user input
text = input("Enter a string: ")
# Initialize an empty result string
lowercase_text = ""
# Iterate through each character in the string
for char in text:
    # Determine if the character is an uppercase letter (A-Z)
    if 'A' <= char <= 'Z':
        # Convert the character to lowercase using ASCII value adjustment
        lowercase_text += chr(ord(char) + 32)
    else:
        # Keep the character unchanged if it's not uppercase
        lowercase_text += char
# Print the converted lowercase string