filename = input("Enter file name: ")

file = open(filename, "r")
text = file.read()

print("Lines:", text.count("\n") + 1)
print("Words:", len(text.split()))
print("Characters:", len(text))

file.close()
