# Function to left-pad a string with zeros to achieve a specified width without using the built-in zfill() method
def print_zero_fill_without_zfill(text, width):
    # Calculate how many zeros are needed to fill the text to the specified width
    zeros_needed = max(0, width - len(text))
    # Create a string with the required zeros and concatenate it with the text
    result = '0' * zeros_needed + text  
    # Display the result
    print(f"Original String: '{text}'")
    print(f"Zero-Filled String: '{result}'")
# Prompt the user to enter a numeric string
user_input = input("Enter a number: ")
# Prompt the user to enter the desired width for zero-filling
# Call the function to zero-fill the input string to the specified width without using the zfill() method