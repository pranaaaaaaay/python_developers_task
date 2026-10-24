# 40. Demonstrate common list methods

numbers = [30, 10, 20, 10]
print("Original list:", numbers)

numbers.append(40)
print("append(40):", numbers)

numbers.insert(1, 15)
print("insert(1, 15):", numbers)

numbers.remove(10)
print("remove(10):", numbers)

removed = numbers.pop()
print("pop():", numbers, "| removed:", removed)

copied = numbers.copy()
print("copy():", copied)

print("count(10):", numbers.count(10))
print("index(20):", numbers.index(20))

numbers.extend([50, 60])
print("extend([50, 60]):", numbers)

numbers.sort()
print("sort():", numbers)

numbers.reverse()
print("reverse():", numbers)

numbers.clear()
print("clear():", numbers)
