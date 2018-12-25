#interlace odd/even
a = int(input())
b = int(input())
from_ctr = a
to_ctr = b
oddprint = 1
if a%2 == 0 and b%2 == 0:
    oddprint = 0
while from_ctr<=b or to_ctr>=a:
    if oddprint:
        while from_ctr%2 != 1:
            from_ctr+=1
        if from_ctr<=b:
            print(from_ctr,end=" ")
        oddprint=0
    if not oddprint:
        while to_ctr%2 != 0:
            to_ctr-=1
        if to_ctr>=a:
            print(to_ctr,end=" ")
        oddprint=1
    from_ctr+=1
    to_ctr-=1
