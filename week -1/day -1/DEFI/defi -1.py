number = int(input("Entre un nombre : "))
length = int(input("Entre la longueur : "))
results = []
for i in range(1, length + 1):
    results.append(number * i)
print(results)
