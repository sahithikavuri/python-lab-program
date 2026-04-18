with open("temp.txt", "r") as f:
    temps = f.readlines()

for t in temps:
    c = float(t.strip())
    f_val = (c * 9/5) + 32
    print(f_val)
