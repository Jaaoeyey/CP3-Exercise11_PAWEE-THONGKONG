number = int(input())
space = number
for x in range(number):
    print(" "*(space-x),"*"*(x*2+1))