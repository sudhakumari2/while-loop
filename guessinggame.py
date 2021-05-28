tries = 1
answer = 6
while tries<=5:
    print("what is the number that play on sudha")
    num = int(input("enter any number"))
    tries = tries+1
    if num==6:
        print("that is right")
        break
    else:
        print("try again your answer is wrong")

# tries = 1
# answer = 5
# while tries<=5:
#     print("what is the number that play on sudha")
#     num = int(input("enter any number"))
#     tries = tries+1
#     if num>answer:
#         print("num bada hai answer se")
#     elif num<answer:
#         print("num chota hai answer se")
#     elif num==answer:
#         print("that is right or barabar hai")
#         break
#     else:
#         print("try again your answer is wrong")