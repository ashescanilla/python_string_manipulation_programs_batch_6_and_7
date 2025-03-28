# Get user input
text = input("Enter a string: ")
total_length = int(input("Enter the desired total length: "))
# Check if the string needs padding
if len(text) < total_length:
    # Calculate how many spaces are needed
    spaces_needed = total_length - len(text)
    # Add spaces at the end using concatenation
    padded_text = text + ' ' * spaces_needed
else:
    # If no padding is needed, keep the string as is
    padded_text = text
# Print the result