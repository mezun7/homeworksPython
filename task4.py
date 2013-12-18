#Shukhrat Azimuratov
#11-2105
#Task4
__author__ = 'shuhrat'

input = file("in.txt", "r")
output = file("out.txt", "w")
#s = ""
#s = s.lower()
#print s
for i in input:
    s = ""
    a = i.split(" ")
    for j in a:
        for z in j:
            if(z.isupper()):
                z = z.lower()
            elif(z.islower()):
                z = z.upper()
            s += z
        s += " "




    s = s.strip()
    s += "\n"
    output.write(s)
output.close()
#print s
