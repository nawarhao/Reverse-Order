# Palindrome Numbers + Digit Counter

# Take input from user
number = int(input("Enter a number: "))

# Count the number of digits
digit_count = len(str(abs(number)))
print("Number of digits:", digit_count)

# Reverse the number
rev = 0
temp5 = number
while temp5 > 0:
    rem = temp5 % 10
    rev = (rev * 10) + rem
    temp5 = temp5 // 10  # Use // for integer division

# Check if it's a palindrome
if number == rev:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
