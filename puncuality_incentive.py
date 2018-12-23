# 200 is incentive for day if employee is punctual
# input
# salary = 500
# days = 3
# output
# 2100
#explanation:for first day =500,second day =700,third day = 900
a = int(input())
b = int(input())
total = 0
while b>0:
    total+=a
    a+=200
    b-=1
print(total)
