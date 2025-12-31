x=frozenset({"apple","banana","cherry"})
print(x)
print(type(x))

fs=frozenset({1,2,3,})
cp=fs.copy()
print(cp)

a=frozenset({1,2,3,4})
b=frozenset({3,4,5})
print(a.difference(b))
print(a-b)

print(a.intersection(b))
print(a & b)

x=frozenset({1,2})
y=frozenset({3,4})
z=frozenset({2,3})
print(x.isdisjoint(y))
print(x.isdisjoint(z))

a1=frozenset({1,2})
b1=frozenset({1,2,3})
print(a1.issubset(b1))
print(a1<=b1)
print(a1<b1)

print(a1.union(b1))
print(a1 | b1)
