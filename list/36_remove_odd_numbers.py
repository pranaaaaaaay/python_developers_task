# 36. Remove all odd numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print("After removing odd numbers:", even_numbers)
