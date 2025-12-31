#Dictionaries
thisdict={
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964,
    "Colors": ["Red","White","Blue"]
}

dict1=dict(name="John",age=22,county="Norway")
print(dict1)

x=dict1.keys()
print(x)

dict1["Occ"]="Student"
print(x)

print(thisdict)
print(type(thisdict))
print(thisdict["Brand"])
print(len(thisdict))
print(thisdict.get("Model"))
print(thisdict.values())
print(thisdict.items())

#change
thisdict["Year"]=2018
print(thisdict)

#update
thisdict.update({"Year":2020})
print(thisdict)

thisdict.pop("Model")
print(thisdict)

del thisdict["Colors"]
print(thisdict)

dict1.clear()
print(dict1)

if "Model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

else:
    print("No, 'model' is one of the keys in the thisdict dictionary")
    