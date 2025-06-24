words = input("Enter comma-separated words:")

sorted_words = ",".join(sorted([word.strip() for word in words.split(",")]))
print(sorted_words)