# 1
numbers = [1, 2, 3, 4, 5]
cubes = list(map(lambda x: x**3, numbers))
print(cubes)

# 2
words = ["hello", "world", "python"]
first_chars = list(map(lambda w: w[0], words))
print(first_chars)

# 3
numbers = [1, 2, 3, 4, 5, 6]
parity = list(map(lambda x: "Juft" if x % 2 == 0 else "Toq", numbers))
print(parity)

# 4
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
products = list(map(lambda x, y: x * y, list1, list2))
print(products)

# 5
texts = ["hello123", "world456", "py#thon"]
letters_only = list(map(lambda t: ''.join(filter(str.isalpha, t)), texts))
print(letters_only)

# 6
numbers = [1, 2, 3, 4, 5]
degree = int(input("Daraja kiriting: "))
powered = list(map(lambda x: x**degree, numbers))
print(powered)
