num = int(input("enter any number"))
a = num
sum = 0
while a>0:
    fac = 1
    i = 1
    rem = a%10
    while i<=rem:
        fac = fac*i
        i = i+1
    sum = sum+fac
    a = a//10
if num==sum:
    print("strong number hai",num)
else:
    print("strong number nhi hai",num)