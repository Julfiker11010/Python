#Lambda Function
x=(lambda a,b : a*a+2*a*b+b*b)(2,3)
print(x)

def myfunc(n):
    return lambda a : a*n

y= myfunc(2)
z= myfunc(3)

print(y(11))
print(z(11))