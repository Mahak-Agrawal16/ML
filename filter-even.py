n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

even = list(filter(lambda x: x % 2 == 0, lst))
print(even)
