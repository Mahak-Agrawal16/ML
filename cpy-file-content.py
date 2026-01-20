source = input("Enter source file name: ")
target = input("Enter target file name: ")

f1 = open(source, "r")
f2 = open(target, "w")

f2.write(f1.read())

f1.close()
f2.close()
