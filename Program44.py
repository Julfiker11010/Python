#RegEx
import re
pattern=r"colour"

if re.search(pattern,"Red is a colour, I love red colour"):
    print("Matched")

else:
    print("Not matched")
    
print(re.findall(pattern,"Red is a colour, I love colour"))

if re.match(pattern,"Red is a colour, I love red colour"):
    print("Matched")
    
else:
    print("Not matched")