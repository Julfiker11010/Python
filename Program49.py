import re
pattern=r"(ab)*" # * means 0 or more

if re.match(pattern,"colour"):
    print("Matched")
    
else:
    print("Not matched")
    