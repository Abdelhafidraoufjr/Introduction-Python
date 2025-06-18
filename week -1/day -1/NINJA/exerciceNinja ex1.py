#true
operation = 3 <= 3 < 9
print(operation)

#true
operation_2 = 3 == 3 == 3
print(operation_2)

#false
operation_3 = bool(0)
print(operation_3)

#false
operation_4 = bool(5 == "5")
print(operation_4)

#true
operation_5 = bool(4 == 4) == bool("4" == "4")
print(operation_5)

#false
operation_6 = bool(bool(None))
print(operation_6)

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

#x is True
print("x is", x)
#y is false
print("y is", y)

#a: 5 bcs true = 1
print("a:", a)
#b: 10 bcs false = 0
print("b:", b)