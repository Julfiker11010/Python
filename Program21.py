#Tuples

students=(
    ("Md Julfiker Hossain", 20,4.00),
    "Abir Rahman Sakin",
    "Sudeepta Mandal"
)

print(students)
print(students[0])
print(students[1:])
print(students[1:2])
print(students[2:])
print(students[-3:-2])

print("\n")

#Unpack Tuples
fruits=("Apple","Banana","Cherry")
(Green,Yellow,Red)=fruits
print(Green)
print(Yellow)
print(Red)

print("\n")

fruits1=("Apple","Mango","Papaya","Pineapple","Cherry")
(Green,*Tropic,Red)=fruits1

print(Green)
print(Tropic)
print(Red)
