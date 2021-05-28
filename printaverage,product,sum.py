count = 1
sum = 0
product = 1
while True:
    num = int(input("enter any number ="))
    user = input('enter q for quit=')
    if user=='q':
        break
    count = count+1
    sum = sum+num
    product = product*num
print("average is" , sum//count)
print("product is" , product*num)