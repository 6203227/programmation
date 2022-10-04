import os

path = "C:/Users/admin/PycharmProjects/pythonProject/programmation/"

f = open(path + "addresses.csv", 'r')
c = f.read()
print(c)