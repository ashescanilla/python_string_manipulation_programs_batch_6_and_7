# Function to right-justify a string without using rjust()
def print_right_justify_without_rjust(text, width):
    # Calculate how many spaces are needed to right-justify the text
    spaces_needed = max(0, width - len(text))
    # Create a string with the required spaces and concatenate it with the text
    result = ' ' * spaces_needed + text 
    # Display the result
# Prompt the user to enter a string
# Prompt the user to enter the desired width for right-justification
# Call the function to right-justify the input string without using the rjust() method