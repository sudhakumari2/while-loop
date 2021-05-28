# num = int(input("enter any number"))
# sum = 0
# i = 1
# while i<num:
#     if num%i==0:
#       sum = sum+i
#     i = i+1
# print(sum)
# if num==sum:
#     print("perfect number hai")
# else:
#     print("perfect number nahi hai")


i=1
while i<=100:
	j=1
	s=0
	while j<i:
		if i%j==0:
			s=s+j
		j+=1
	if s==i:
		print('perfect no h',i)
	else:
		print('perfect no nhi hai ',i)
	i+=1