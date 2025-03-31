# Function to print whether a string starts with a specified prefix without using the startswith() methoddef print_string_starts_with_no_startswith(text, prefix):
def print_string_starts_with_no_startswith(text, prefix):
    # Ensure the prefix length is not greater than the text length
    if len(prefix) > len(text):
        print(f"'{text}' does not start with '{prefix}'")
        return
    # Manually check each character of the prefix with the corresponding character of the text
    # If all characters match, print the success message
# Prompt the user to enter a string
# Prompt the user to enter the prefix to check
# Call the function to check if the input string starts with the specified prefix