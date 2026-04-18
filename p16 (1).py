def first_diff(s1, s2):
    for i in range(min(len(s1), len(s2))):
        if s1[i] != s2[i]:
            return i
    return -1

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

pos = first_diff(s1, s2)

if pos == -1:
    print("Strings are same")
else:
    print("First difference at index:", pos)
