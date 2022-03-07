a = []
n = int(input("Enter number of items in the list: "))
for i in range(0,n):
    y = int(input())
    a.append(y)
square = list(map(lambda x: x**2, a))
cube = list(map(lambda x: x**3, a))
print(square)
print(cube)
