import numpy as np

r = int(input("Enter rows: "))
c = int(input("Enter columns: "))

a = np.array([[int(input()) for j in range(c)] for i in range(r)])
b = np.array([[int(input()) for j in range(c)] for i in range(r)])

print("Addition:\n", a + b)
print("Multiplication:\n", np.dot(a, b))
