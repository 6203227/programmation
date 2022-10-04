import os

path = "C:/Users/admin/Desktop/"

f = open(path + "text.txt", 'w')
for i in range(10):
    f.write(''' \n test\ntest1\ntest2
test3
test4
''')
    f.write(str(i))
f.close()
