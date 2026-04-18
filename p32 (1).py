from functools import reduce

nums = list(map(int, input("Enter numbers: ").split()))

total = reduce(lambda x, y: x + y, nums)
print("Sum:", total)
