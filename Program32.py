#Reading a File
file=open("Student.txt","r+")
#print(file.writable())
text=file.read()
print(text)

size=len(text)
print(size)

print(text1)
file.close()