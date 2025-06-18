word = input("Entrez une chaîne : ")

result = "" 

for char in word:
    if len(result) == 0 or char != result[-1]:
        result += char

print("Résultat sans lettres consécutives en double :", result)
