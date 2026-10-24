# 18. Take input to create a list and display it

numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(number) for number in numbers]

print("Your list:", numbers)
