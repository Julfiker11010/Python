import re
pattern=r"ice(-)?cream" # ? means 0 or 1

if re.match(pattern,"icecream"):
    print("Matched")
    
else:
    print("Not matched") 
    