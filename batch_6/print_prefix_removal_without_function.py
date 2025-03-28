# Get user input
text = input("Enter a string: ")
prefix = input("Enter the prefix to remove: ")
# Check if the string starts with the prefix
if text[:len(prefix)] == prefix:
    # Remove the prefix using slicing
    result = text[len(prefix):]
else:
    # Return original string if no prefix match
    result = text
# Print the result after removing the specified prefix (if found)