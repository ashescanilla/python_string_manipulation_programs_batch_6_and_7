# Prompt the user to enter a string
text = input("Enter a string: ")
# Split the input string into a list of words using spaces as delimiters
words = text.split()
# Create an empty list to store the words after applying title case
title_case_words = []
# Iterate through each word to apply title case
for word in words:
    if word:
        # Check if the first character is a lowercase letter and convert it to uppercase using ASCII
        if 'a' <= word[0] <= 'z':
            first_char = chr(ord(word[0]) - 32)
        else:
            # Keep the first character unchanged if it's not a lowercase letter
            first_char = word[0]
        # Convert the remaining characters to lowercase using ASCII if they are uppercase
        remaining_chars = ""
        for char in word[1:]:
            if 'A' <= char <= 'Z':
                remaining_chars += chr(ord(char) + 32)
            else:
                # Keep the character unchanged if it's not uppercase
                remaining_chars += char
        # Combine the capitalized first letter with the rest of the word
        title_case_word = first_char + remaining_chars
        title_case_words.append(title_case_word)
# Join the processed words with spaces to form the final title-cased string
# Display the result