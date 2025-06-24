def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

print(longest_word("Margaret's toy is a pretty doll."))
print(longest_word("A thing of beauty is a joy forever."))
print(longest_word("Forgetfulness is by all means powerless!"))