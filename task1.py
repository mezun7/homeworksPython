#Shukhrat Azimuratov
#11-2105
#Task1
f = raw_input("Enter digit: ")
f = int(f)

for i in range(1, 10):
    s = str(f) + "x" + str(i)
    print s, '=', str(f * i)

