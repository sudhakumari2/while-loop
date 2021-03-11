# i=1
# p_n=0
# n_n=0
# odd=0
# even=0
# zero=0
# while i<=20:
#     num=int(input("enter the number"))
#     if num>0:
#         p_n=p_n+1
#         if num%2==0:
#             even=even+1
#         else:
#             odd=odd+1
#     elif num<0:
#         n_n=n_n+1
#         if num%2==0:
#             even=even+1
#         else:
#             odd=odd+1
#     else:
#         zero+=1
#     i+=1
# print(p_n,n_n,even,odd,zero)


i=1
p_n=0
n_n=0
odd=0
even=0
zero=0
for num in range (20):
    num=int(input("enter the number"))
    if num>0:
        p_n=p_n+1
        if num%2==0:
            even=even+1
        else:
            odd=odd+1
    elif num<0:
        n_n=n_n+1
        if num%2==0:
            even=even+1
        else:
            odd=odd+1
    else:
        zero+=1
    i+=1
print(p_n,n_n,even,odd,zero)