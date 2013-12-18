#Shukhrat Azimuratov
#11-2105
#Task1

eps = 0.000000001
f = raw_input("Enter your x: ")

prev = 1
curr = prev + f*f/2
f = False
i = 3

while(abs(curr - prev) < eps):

