text = input("Enter a sentence: ")

words = text.split()
joined = "-".join(words)

data = {
    "words": words,
    "joined": joined
}

print(data)
