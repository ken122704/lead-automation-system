number = input("Enter a number: ")
number = int(number)

if number < 100:
    print("small")
elif number >= 100 and number <= 999:
    print("medium")
else:
    print("large")