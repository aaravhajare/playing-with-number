
n = int(input("Enter a number"))

ogn = n
r = 0

# store og number
while n > 0 :
    digit = n %10
    r = r * 10 + digit
    n //= 10

#checking 

if r == ogn :
    print(f"{n} is a palindrome")
else : 
    print(f"{n} is not a palindrome")