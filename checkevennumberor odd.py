# i = 1
# while i<=100:
#     if i%2==0:
#         print(-i)
#     else:
#         print(i)
#     i = i+1

c=0
i=1
count=0
while i<=10:
    num=int(input("enter a number "))
    if num%2==0:
        c=c+1
    else:
        count=count+1
    i=i+1
print(c)
print(count)