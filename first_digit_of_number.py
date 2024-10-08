# 1) Get an integer from the user.
user_input = int(input("Input a number: "))

# 2) Handle positive and negative cases and print the first digit of the number
first_digit = None
# Positive case
if user_input >= 0:
    first_digit = str(user_input)[0]
# Negative case, so we need to skip the -
else:
    first_digit = str(user_input)[1]

print(f"The first digit of {user_input} is {first_digit}")