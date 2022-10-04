import csv
import os

path = "C:/Users/admin/PycharmProjects/pythonProject/programmation/"

f = open(path + "addresses.csv", 'r')
re = csv.reader(f, delimiter=';')
print(type(re))
ma = []
for row in re:
    print(row)
    ma.append(row)
for line in ma:
    for val in line:
        print(val)
    print("\n")
