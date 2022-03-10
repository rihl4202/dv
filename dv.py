import csv
import math
file = open("team_1.csv")
f = csv.reader(file)
data = list(f)
data = data[0]
sum = 0
for i in data:
    sum = sum+float(i)
mean = sum/len(data)
print(mean)
squares = []
for i in data:
    a = float(i)-mean
    a = a**2
    squares.append(a)
sum = 0
for i in squares:
    sum = sum+float(i)
result = sum/(len(data)-1)
sd = math.sqrt(result)
print(sd)