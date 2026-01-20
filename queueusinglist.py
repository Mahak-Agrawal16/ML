queue = []
n = int(input("Enter number of elements: "))

for i in range(n):
    queue.append(input("Enter element: "))

print("Queue:", queue)
queue.pop(0)
print("After dequeue:", queue)
