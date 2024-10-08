# Write a program that takes in an integer input and prints the following pattern based on the integer.
#     1
#   2 2
# 3 3 3

pyramid_size = int(input("Enter the size of the pyramid: "))

# The number of characters the largest digit will take up
max_number_size = len(str(pyramid_size))

for i in range(1, pyramid_size + 1):
    number_of_spaces = pyramid_size - i

    # The number of characters this current digit takes up
    current_number_size = len(str(i))

    for j in range(number_of_spaces):
        # Add left spaced padding for the number depending on how many characters this digit takes up
        print(" " * (max_number_size + 1), end="")

    for j in range(i):
        # Prints the number with left padding that will fill up to the largest digit
        print((" " * (max_number_size - current_number_size + 1)) + str(i), end="")

    print()