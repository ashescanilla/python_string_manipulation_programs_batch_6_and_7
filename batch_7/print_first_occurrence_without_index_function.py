# Function to find the first occurrence of a character without using index()
def print_first_occurrence_without_index_function(text, char_to_find):
    # Iterate through each character in the string using its index
    for i in range(len(text)):
        # Check if the current character matches the specified character
        if text[i] == char_to_find:
            print(f"The first occurrence of '{char_to_find}' is at index {i}.")
            return
    # If the character is not found, display a message
    print(f"'{char_to_find}' is not found in the string.")
# Prompt the user to enter a string
user_input = input("Enter a string: ")
# Prompt the user to enter the character to find within the string
char_input = input("Enter the character to find: ")
# Ensure only one character is provided for searching
if len(char_input) == 1:
    print_first_occurrence_without_index_function(user_input, char_input)
else:
    print("Please enter a single character to find.")