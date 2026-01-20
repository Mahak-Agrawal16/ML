import statistics

n = int(input("Enter number of elements: "))
data = []

for i in range(n):
    data.append(int(input("Enter element: ")))

print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Standard Deviation:", statistics.stdev(data))
