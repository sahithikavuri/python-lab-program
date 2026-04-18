nums = list(map(int, input("Enter numbers: ").split()))

evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
