import numpy as np

n = int(input("Enter size of array: "))
a = np.array([int(input()) for _ in range(n)])
b = np.array([int(input()) for _ in range(n)])

print("Addition:", a + b)
print("Multiplication:", a * b)
