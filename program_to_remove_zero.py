# **REVERSE A NUMBER**
## Number N is passsed as input.program must print reverse number of N
## input1: 2541
## output1:1425
## input2:6500
## output2:56

num = int(input())
while num%10 == 0 and num!=0:
    num = int(num/10)
numstr = str(num)
print(numstr[::-1])
