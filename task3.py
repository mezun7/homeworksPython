#Shukhrat Azimuratov
#11-2105
#Task3

f = raw_input()
f = int(f)
z = 1
k = f - 1
for i in range(f):
    s = ""
    j = 0;
    while j < 2 * f - 1:
        if(k == j):
            for l in range(z):
                s += '0'
                j += 1
            z += 2
            k -= 1
        else :
            s += '*'
            j += 1
    print s
z -= 4
k += 2
for i in range(f - 1):
    s = ""
    j = 0
    while j < 2 * f - 1:
        if(k == j):
            for l in range(z):
                s += '0'
                j += 1
            z -= 2
            k += 1
        else :
            s += '*'
            j += 1
    print s
