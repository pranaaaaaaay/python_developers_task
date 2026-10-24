# 33. Find the second largest distinct number

numbers = [10, 45, 20, 35, 45, 30]
unique_numbers = sorted(set(numbers))

if len(unique_numbers) >= 2:
    print("Second largest number:", unique_numbers[-2])
else:
    print("There is no second largest number")
