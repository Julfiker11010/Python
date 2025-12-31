#OOP
class Student:
    roll=""
    cgpa=""
    
rahim=Student()
print(isinstance(rahim,Student))

rahim.roll=101
rahim.cgpa=3.7

print(f"Roll: {rahim.roll}, CGPA: {rahim.cgpa}")
