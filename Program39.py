#Constructor
class Student:
    roll=""
    cgpa=""
    
    def __init__(self,roll,cgpa): 
        self.roll=roll
        self.cgpa=cgpa
    
    def display(self):
        print(f"Roll: {self.roll}, CGPA: {self.cgpa}")
 
    
rahim=Student(101,3.75)
rahim.display()  
 