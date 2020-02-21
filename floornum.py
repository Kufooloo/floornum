floornum = int(input('Floor?'))
def floor(x):
    
    if x <=0:
        if x  <=-13:
            pos = 1
        else:
            pos = 0
        return x +pos
    else:
     if x >= 13:
         neg = 2
     else:
         neg = 1
    x = x - neg
    return x
print (floor(floornum))

 
