#exception handling
try:
    list=[20,0,30]
    result=list[0]/list[3]
    print(result)
    print("Done")

except (ValueError,ZeroDivisionError):
    print("You have entered incorrect input")

finally:
    print("Successful")
    