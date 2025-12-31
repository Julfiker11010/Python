import re
pattern=r"a+b" # + means 1 or more

if re.match(pattern,"abaaacolour"):
    print("Matched")
    
else:
    print("Not matched")
    