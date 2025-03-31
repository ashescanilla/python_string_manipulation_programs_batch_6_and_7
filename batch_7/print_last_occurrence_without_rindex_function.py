# Program to find the first location of a character starting from the end without using rindex()
def print_last_occurrence_without_rindex_function(text, char_to_find):
    # Iterate through the string in reverse using a negative step
    for i in range(len(text) - 1, -1, -1):
        # Check if the current character matches the specified character
    # If the character is not found, display a message
# Prompt the user to enter a string
# Prompt the user to enter the character to find within the string
# Ensure only one character is provided for searching