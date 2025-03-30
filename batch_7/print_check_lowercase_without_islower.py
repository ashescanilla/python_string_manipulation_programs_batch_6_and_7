# Function to print whether a string contains any lowercase letters without using the islower() method
def print_check_lowercase_without_islower(text):
    # Assume the string is lowercase initially
    is_lowercase = True
    # Iterate through each character in the string
    for char in text:
        # Check if the character is an uppercase letter (A-Z)
        if 'A' <= char <= 'Z':
            # If it is, then the string is not all lowercase
            is_lowercase = False
            # Break out of the loop
            break
    # Display the result
    if is_lowercase:
        print("The string is in lowercase.")
    else:
        print("The string is not in lowercase.")
# Get user input and check if it is lowercase