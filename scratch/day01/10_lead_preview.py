details = input("Enter your details (name, budget, interest): ")
name, budget, interest = details.split(",")
budget = int(budget)
name = name.strip().title()
interest = interest.strip().lower()

if budget >= 3000 and interest == "high":
    print ("-----------------------------")
    print("LEAD CARD")
    print ("-----------------------------")

    print(f"Name: {name}")
    print(f"Budget: {budget:,}")
    print(f"Interest: HOT")


    print ("-----------------------------")
else:
    print ("-----------------------------")
    print("LEAD CARD")
    print ("-----------------------------")

    print(f"Name: {name}")
    print(f"Budget: {budget:,}")
    print(f"Interest: COLD")


    print ("-----------------------------")


