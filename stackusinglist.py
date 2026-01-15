stack=[]
n=int(input("Enter number of elements: "))
for i in range(n):
    stack.append(input("enter element: "))
print("Stack:",stack)
stack.pop()
print("After pop:",stack)