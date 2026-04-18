l1 = list(map(int, input("Enter first sorted list: ").split()))
l2 = list(map(int, input("Enter second sorted list: ").split()))

merged = sorted(l1 + l2)
print("Merged list:", merged)
