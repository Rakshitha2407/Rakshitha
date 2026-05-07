input_number = int(input("Enter a number:"))
print(f"number you input is {input_number}")
sum_of_digit = 0
while input_number != 0:
    remainder = input_number % 10
    input_number = input_number//10
    sum_of_digit += remainder
    if sum_of_digit > 9 and input_number == 0:
        input_number = sum_of_digit
        sum_of_digit = 0

print('Your lucky digit is',sum_of_digit)
