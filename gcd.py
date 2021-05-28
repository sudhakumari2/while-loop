num1 = int(input("enter first number"))
num2= int(input("enter second number"))
if num1>num2:
    a=num1
else:
    a=num2
i=1
while i<=a:
    if num1%i==0 and num2%i==0:
        gcd=i
    i+=1
print("gcd of given number is",gcd)