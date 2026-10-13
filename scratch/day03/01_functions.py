def add(a,b):
    return a + b

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

def min_max(numbers):
    return min(numbers), max(numbers)


returns = add(3, 5)
returns2 = greet("KC")
returns3 = min_max([1, 2, 3, 4, 5])

print(returns)
print(returns2)
print(returns3)