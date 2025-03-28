# Ask the user to input a number from 0-1000
num_input = input("Enter a number (0-1000): ")
# Get the length of the inputed number
input_length = len(num_input)
# Subtract it from 6
no_of_zeros = 6 - input_length
# Multiply "0" and the difference of the 6 and length
zeros = "0" * no_of_zeros
# Add the zeros before the inputted number
new_number = zeros + num_input
# Print the modified number
print(new_number)