word = input("Enter a word: ")
vowels = "aeiouAEIOU"

found = False
for ch in word:
    if ch in vowels:
        found = True
        break

if found:
    print("Contains vowel")
else:
    print("No vowels")
