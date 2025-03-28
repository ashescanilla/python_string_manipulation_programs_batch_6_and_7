# Get user input
text = input("Enter a string: ")
total_length = int(input("Enter the desired total length: "))
# Check if the string needs centering
if len(text) < total_length:
    # Calculate spaces on both sides
    total_spaces = total_length - len(text)
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces
    # Add spaces to center the text
    centered_text = ' ' * left_spaces + text + ' ' * right_spaces
else:
    # If no centering is needed, keep the string as is
    centered_text = text
# Print the result
print("Centered string:", repr(centered_text))