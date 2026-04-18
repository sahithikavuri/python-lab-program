import random

nums = [random.randint(1, 100) for _ in range(20)]

print("List:", nums)
print("Any element:", nums[0])

nums.sort()
print("2nd smallest:", nums[1])
print("2nd largest:", nums[-2])

print("Smallest:", nums[0])
print("Largest:", nums[-1])

print("Even numbers:")
for i in nums:
    if i % 2 == 0:
        print(i, end=" ")
