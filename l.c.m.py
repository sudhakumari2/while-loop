num1 = int(input("enter first number"))
num2= int(input("enter second number"))
if num1>num2:
    a=num1
else:
    a=num2
while True:
    if a%num1==0 and a%num2==0:
        print(a)
        break
    a+=1