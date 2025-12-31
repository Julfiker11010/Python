num=[10,20,30,40,50]
print(num)

for x in num:
    print(x)

fruits=["apple","banana","orange"]
for x in fruits:
    if x=="banana":
        break
    print(x)

for x in fruits:
    if x=="banana":
        continue
    print(x)
    