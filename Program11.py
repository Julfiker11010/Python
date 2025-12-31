#Lists
subjects=["Java","Python","C","C++","OS","Networking"]
subjects1=["ML","AI","Algorithms"]

subjects.extend(subjects1)
print(subjects)

subjects2=subjects.copy()
print(subjects2)

print(subjects)
print(len(subjects))
print(subjects[0])
print(subjects[2:])
print(subjects[-3])
print("Python" in subjects)
print("DSA" not in subjects)
print("TOC" in subjects)
print(subjects+["DSA",25])
print(subjects*3)
print(type(subjects))

print(subjects.count("OS"))

subjects.append("TOC")
print(subjects)

subjects.insert(2,"CAD")
print(subjects)

subjects.remove("CAD")
print(subjects)

subjects.sort()
print(subjects)

pos=subjects.index("Java")
print(pos)

subjects.reverse()
print(subjects)

subjects.pop()
print(subjects)

subjects.pop()
print(subjects)

subjects.clear()
print(subjects)
