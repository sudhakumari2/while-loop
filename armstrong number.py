# check armstrong nuber only therr digit hai ya nhi
# num = int(input("enter any number"))
# sum=0
# i = num
# while i>0:
#     digit = i%10
#     sum=sum+digit**3
#     i=i//10
# if sum==num:
#     print("armstrong number hai")
# else:
#     print("armstrong number nhi hai")

# check armstrong number any digit
num=int(input("enter any number"))
i=num
sum=0
count=len(str(num))
while i>0:
    rem=i%10
    sum=sum+rem**count
    i=i//10
if sum==num:
    print("armstrong number h")
else:
    print("armstrong number  nhi h")