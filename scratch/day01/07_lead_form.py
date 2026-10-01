details = input("Enter your details (Name, Budget, Source): ")
name, budget, source = details.split(",")
name = name.strip().title()
budget = int(budget)
source = source.strip().lower()

print ("-----------------------------")
print("LEAD CARD")
print ("-----------------------------")

print(f"Name: {name}")
print(f"Budget: {budget:,}")
print(f"Source: {source}")
print(f"Budget pero month: {budget / 12:,.2f}")


print ("-----------------------------")
