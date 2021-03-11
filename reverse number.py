# print sum of 1 to 100
i = 1
sum = 0
while i<=100:
    print(i)
    i = i+1
    sum = sum+i
print(sum)
# print ten user input sum
s = 0
i = 1
while i<=10:
    num = int(input("enter any number"))
    i = i+1
    s = s+num
print(s)

# print negative even number and positive odd
i = 1
while i<=100:
    if i%2==0:
        print(-i)
    else:
        print(i)
    i = i+1

# print 3 se divisible numer nav and divisible by 5 to gurukul and divisible by both to print navgurukul
i = 1
while i<=100:
    if i%3==0 and i%7==0:
        print("navgurukul")
    elif i%3==0:
        print("nav")
    elif i%7==0:
        print("gurukul")
    else:
        print(i)
    i = i+1
    
# print reverse number
number = int(input("enter any number"))
rev = 0
while number>0:
    rev = (rev*10)+number%10
    number = number//10
print("the reverse number of enter number is",rev)