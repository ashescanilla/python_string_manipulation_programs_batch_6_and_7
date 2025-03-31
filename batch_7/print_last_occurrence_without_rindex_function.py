# Program to find the first location of a character starting from the end without using rindex()
def print_last_occurrence_without_rindex_function(text, char_to_find):
    # Iterate through the string in reverse using a negative step
    for i in range(len(text) - 1, -1, -1):
        # Check if the current character matches the specified character
        if text[i] == char_to_find:
            print(f"The last occurrence of '{char_to_find}' is at index {i}.")
            # If a match is found, return the index of the character
            return
    # If the character is not found, display a message
    print(f"'{char_to_find}' is not found in the string.")
# Prompt the user to enter a string
user_input = input("Enter a string: ")
# Prompt the user to enter the character to find within the string
char_input = input("Enter the character to find: ")
# Ensure only one character is provided for searching
if len(char_input) == 1:
    print_last_occurrence_without_rindex_function(user_input, char_input)
else:
    print("Please enter a single character to find.")