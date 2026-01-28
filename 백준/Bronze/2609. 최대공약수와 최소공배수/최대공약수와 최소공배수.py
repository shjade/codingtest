a, b = map(int, input().split())
x, y = a, b

while y != 0:
    x, y = y, x % y

g = x
l = a * b // g

print(g)
print(l)