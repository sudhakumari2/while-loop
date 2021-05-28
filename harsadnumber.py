# print check harsad number or not
# num = int(input("enter any number"))
# a = num
# sum = 0
# while num>0:
#     rem = num%10
#     sum = sum+rem
#     num = num//10
# if a%sum==0:
#     print("harsad number hai",a)
# else:
#     print("harsad number nahi hai",a)

# print 1 to 100 harsad number
i= 1
sum = 0
while i<=100:
    i=i+1
    rem = i%10
    sum = sum+rem
    i = i//10
    if i%sum==0:
      print("harsad number hai",i)
    i = i+1
# else
#     print("harsad number nhi hai",i)