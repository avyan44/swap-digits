def swap_digits(number, digit1, digit2):
    # Convert number to string
    num_str = str(number)
    # Swap digit1 and digit2
    swapped = ''
    for ch in num_str:
        if ch == digit1:
            swapped += digit2
        elif ch == digit2:
            swapped += digit1
        else:
            swapped += ch
    return int(swapped)

# Example usage
number = input("Enter a number: ")
d1 = input("Enter the first digit to swap: ")
d2 = input("Enter the second digit to swap: ")

# Check input validity
if not (number.isdigit() and d1.isdigit() and d2.isdigit()):
    print("Please enter only digits.")
elif len(d1) != 1 or len(d2) != 1:
    print("Please enter single-digit numbers.")
else:
    result = swap_digits(number, d1, d2)
    print(f"Result after swapping: {result}")

