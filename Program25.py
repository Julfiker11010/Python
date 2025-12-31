#xargs
def student(*details):
    print(details)

student(101,"Julfiker")
student(102,"Julfiker",3.75)

def add(*numbers):
    sum=0
    for num in numbers:
        sum+=num
    print(sum)

add(10,20)
add(10,20,30)
add(10,20,30,40)

def my_function(*kids):
    print("The youngest child is "+kids[2])

my_function("Emil","Tobias","Linus")