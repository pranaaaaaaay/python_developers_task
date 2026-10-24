# 19. Remove duplicates from a list of 10 numbers

numbers = [1, 2, 3, 2, 4, 5, 1, 6, 5, 7]
unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print("List without duplicates:", unique_numbers)
