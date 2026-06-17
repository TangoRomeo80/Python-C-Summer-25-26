# Immutable datatypes:
## Numeric: int, float, complex
## Sequence: str, tuple, range
# Mutable datatypes:
## Sequence: list
## Set: set
## Collections: dict

# a = 10
# print(id(a))
# a = a + 2
# print(id(a))

# a = [1, 2, 3]
# print(id(a))
# a.append(4)
# print(id(a))

# a = [1, 2, 3]
# b = a
# print(id(a))
# print(id(b))
# a.append(4)
# print(a)
# print(b)

# a = [1, 2, 3]
# b = a.copy()
# print(id(a))
# print(id(b))
# a.append(4)
# print(a)
# print(b)

# a = (1, 2, [3, 4])
# print(a[2])
# a[2].append(5)
# print(a)