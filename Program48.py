#Metacharacters
import re
pattern=r"^colo..r$"

if re.match(pattern,"colouar"):
    print("Matched")

else:
    print("Not matched")
    