# Function to remove trailing spaces from a string without using the rstrip() method
def print_remove_trailing_spaces_without_rstrip(text):
    # Initialize index to the last character of the string
    index = len(text) - 1
    # Iterate backward through the string to find the last non-space character
    while index >= 0 and text[index] == ' ':
        index -= 1
    # Slice the string up to the last non-space character
    result = text[:index+1]
    # Display the results
    print(f"Input String: '{text}'")
    print(f"String Without Trailing Spaces: '{result}'")
# Get user input and remove trailing spaces
user_input = input("Enter a string with trailing spaces: ")
print_remove_trailing_spaces_without_rstrip(user_input)