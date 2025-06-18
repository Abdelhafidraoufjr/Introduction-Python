from datetime import datetime

BirthDate = input("Enter your birth date (YYYY-MM-DD):")

year, month, day  = map(int, BirthDate.split('-'))
current_year = datetime.now().year
age = current_year - year

candles = age % 10
if candles == 0:
    candles = 10
print(candles)
def print_cake(candles):
    print(f"   _{'i' * candles}_")
    print("  |:H:a:p:p:y:|")
    print("__|___________|__")
    print("|^^^^^^^^^^^^^^^|")
    print("|:B:i:r:t:h:d:a:y:|")
    print("|                 |")
    print("~~~~~~~~~~~~~~~~~~~")

print_cake(candles)