# Function to print whether a string starts with a specified prefix without using the startswith() methoddef print_string_starts_with_no_startswith(text, prefix):
def print_string_starts_with_no_startswith(text, prefix):
    # Ensure the prefix length is not greater than the text length
    if len(prefix) > len(text):
        print(f"'{text}' does not start with '{prefix}'")
        return
    # Manually check each character of the prefix with the corresponding character of the text
    for i in range(len(prefix)):
        if text[i] != prefix[i]:
            print(f"'{text}' does not start with '{prefix}'")
            return
    # If all characters match, print the success message
    print(f"'{text}' starts with '{prefix}'")
# Prompt the user to enter a string
user_input = input("Enter a string: ")
# Prompt the user to enter the prefix to check
prefix_input = input("Enter the prefix to check: ")
# Call the function to check if the input string starts with the specified prefix