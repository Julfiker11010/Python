#map and filter function
def square(x):
    return x*x

num=[1,2,3,4,5]

a=list(map(square,num))
print(a)

b=list(filter(lambda x:x%2==0,num))
print(b)
