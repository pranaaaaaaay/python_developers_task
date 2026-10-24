# 34. Find common elements between two lists

first_list = [1, 2, 3, 4, 5]
second_list = [3, 4, 5, 6, 7]
common = []

for number in first_list:
    if number in second_list and number not in common:
        common.append(number)

print("Common elements:", common)
