import math

n = int(input("Enter small number"))
o = int(input("Enter big number"))

def hcf(n,o):
    while (o) :
        ns = o
        o = o % n 
        n = ns
    return n

print(f"GCD is {n}")

print("Lcm is " , n / hcf(n,o) * o)

# alternate 

print("LCM is" , math.lcm(n ,o ))