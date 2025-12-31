#Character class
import re
pattern=r"[A-Z][a-z][0-9]"

if re.match(pattern,"Tn6dljfdrp"):
    print("Matched")
    
else:
    print("Not matched")
    