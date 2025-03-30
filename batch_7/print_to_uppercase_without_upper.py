# Function to print the original string and its uppercase version without using the built-in upper() method.
def print_to_uppercase_without_upper_function(text):
    # Initialize an empty string to store the result
    result = ''
    # Iterate through each character in the input string
    for char in text:
        # Check if the character is a lowercase letter (a-z)
        if 'a' <= char <= 'z':
            # If it is, convert it to uppercase (A-Z) and add it to the result
            result += chr(ord(char) - 32)
        else:
            # If it's not a lowercase letter, add it to the result as is
            result += char
    # Print the original and converted strings
    print(f"Original String: '{text}'")
    print(f"Uppercase String: '{result}'")
# Get user input and convert to uppercase