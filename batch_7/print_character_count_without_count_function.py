# Function to count character occurrences without using count()
def print_character_count_without_count_function(text, char_to_count):
    # Initialize a counter to store the number of occurrences
    count = 0
    # Iterate through each character in the string
    for char in text:
        # Compare the current character with the specified character
        if char == char_to_count:
            # If they match, increment the counter
            count += 1
    # Display the result
    print(f"Character '{char_to_count}' appears {count} times in the string.")
# Prompt the user to enter a string
user_input = input("Enter a string: ")
# Prompt the user to enter the character whose occurrences are to be counted
# Ensure only one character is provided for counting