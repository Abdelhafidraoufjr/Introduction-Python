names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

name = input("Entrez votre nom : ")

if name in names:
    print(names.index(name))
else:
    print("Nom non trouvé dans la liste.")
