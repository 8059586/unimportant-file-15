import csv

with open("height-weight.csv",newline="")as a:
    reader = csv.reader(a)
    data = list(reader)

data.pop(0)
newdata = []
for i in range(0,len(data)):
    num = data[i][1]
    newdata.append(float(num))
newdata.sort()
n = len(newdata)

if n % 2 == 0:
    m1 = float(newdata[n//2])
    m2 = float(newdata[n//2-1])
    median = (m1+m2)/2
else:
    median = newdata[n//2]

print(median)