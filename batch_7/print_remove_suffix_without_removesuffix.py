# Function to print the original string and its version without the specified suffix, without using removesuffix()
def print_remove_suffix_without_removesuffix(text, suffix):
    # Check if the text ends with the specified suffix
    if text[-len(suffix):] == suffix and len(suffix) <= len(text):
        # Remove the suffix by slicing
        result = text[:-len(suffix)]
    else:
        result = text
    # Display the results
    print(f"Original String: '{text}'")
    print(f"String Without Suffix: '{result}'")
# Get user input and suffix to remove