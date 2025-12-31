#Sets
num1={1,2,3,4,5}
num2=set([4,5,6])

num2.add(7)
print(num2)

num2.remove(7)
print(num2)

num1.update(num2)
print(num1)

print(7 in num2)
print(4 in num2)
print(4 not in num2)
print(7 not in num2)

print(num1 | num2)
print(num1 & num2)
print(num1-num2)
print(len(num1))

thisset={"apple","banana","cherry"}
thisset.discard("banana")
print(thisset)

thisset.pop()
print(thisset)

thisset.clear()
print(thisset)

#Join a set and a tuple
x={"a","b","c"}
y=(1,2,3)
z=x.union(y)
print(z)

set1={"a","b","c"}
set2={1,2,3}

set1.update(set2)
print(set1)

set3={"apple","banana","cherry"}
set4={"google","microsoft","apple"}
result=set3.intersection(set4)
print(result)

res=set3.difference(set4)
print(res)