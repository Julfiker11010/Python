#xxargs
def student(**details):
    print("ID is",details["id"],"and the name is "+details["name"])

student(id=101,name="Julfiker")

def student(**details):
    print(details)
    print(details["id"])

student(id=101,name="Julfiker")