# Get user input
text = input("Enter a string: ")
# Initialize an empty result string
swapped_text = ""
# Iterate through each character in the string
for char in text:
    # Determine if the character is an uppercase letter using ASCII values
    if 'A' <= char <= 'Z':
        # Change to lowercase by applying a 32-value ASCII adjustment
        swapped_text += chr(ord(char) + 32)
    elif 'a' <= char <= 'z':
        # Change to uppercase by reducing 32 from its ASCII value
        swapped_text += chr(ord(char) - 32)
    else:
        # Keep non-alphabetic characters unchanged
        swapped_text += char
# Print the result