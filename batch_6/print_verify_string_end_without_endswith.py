# Get user input
text = input("Enter a string: ")
suffix = input("Enter the suffix to check: ")
# Check if the end of the string matches the suffix using slicing
if text[len(text) - len(suffix):] == suffix:
    print("The string matches the given suffix.")
else:
    print("The string does not match the given suffix.")