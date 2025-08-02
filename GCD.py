import math

n = int(input("Enter small number"))
o = int(input("Enter big number"))

while (o) :
    ns = o
    o = o % n 
    n = ns

print(f"GCD is {n}")

# alternate 

print("GCD is" , math.gcd(n ,o ))