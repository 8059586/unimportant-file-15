import csv

with open("height-weight.csv",newline="")as a:
    reader = csv.reader(a)
    data = list(reader)

data.pop(0)
newdata = []
for i in range(0,len(data)):
    num = data[i][1]
    newdata.append(float(num))

sum = 0
for g in newdata:
    sum+=g
mean = sum/len(newdata)
print(mean)