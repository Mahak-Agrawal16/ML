n=int(input("enter number of students: "))
students={}
for i in range(n):
    name= input("Enter name: ")
    marks= int(input("Enter marks: "))
    students[name]= marks
    for name,marks in students.items():
        if marks>75:
            print(name,marks)