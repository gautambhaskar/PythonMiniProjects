import math
#This is a simple Quadratic calculator.
print("Quadratic Root Finder")
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
ax = "ax2".translate(SUP)
print("Enter the following values as per standard form: y = " + ax + " + bx + c")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
try:
    sol1 = (-b + math.sqrt((b ** 2)-(4 * a * c)))/(2 * a)
    sol2 = (-b - math.sqrt((b ** 2)-(4 * a * c)))/(2 * a)
except:
    print("The values entered cannot be processed. This could be because there is no solution, or because of an incorrect input of values...")
try:
    sol1 = int(sol1)
except:
    pass
try:
    sol2 = int(sol2)
except:
    pass
try:
    if sol1 == sol2:
        print ("Solution is:")
        print (sol1)
    else:
        print ("Solutions are:")
        print (sol1)
        print (sol2)
except:
    pass