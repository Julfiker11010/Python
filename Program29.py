#List comprehension
num=[1,2,3,4,5]
result=list(map(lambda x:x*x,num))
print(result)

newlist=[x*x for x in num]
print(newlist)

r=[x for x in num if x%2==0]
print(r)

