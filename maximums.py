def max_of_two(x, y):
    if x>y:
        return x
    elif x<y:
        return y
    else:
        return y
    
def max_of_three(x, y, z):    
    if ((x>y) and (x>z)) or ((x>y) and (x==z)) or ((x>z) and (x==y)):
        return x
    elif (y>x) and (y>z) or ((y>x) and (y==z)) or ((y>z) and (y==x)):
        return y
    elif (z>x) and (z>y) or ((z>y) and (x==z)) or ((z>x) and (z==y)):
        return z
    else:
        return z 
