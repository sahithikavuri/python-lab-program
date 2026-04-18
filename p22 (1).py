with open("emails.txt", "r") as f:
    lines = f.readlines()

result = "".join(lines)
print(result)
