pwd=input("Enter password: ")
score=0
if len(pwd)>=8: score+=1
if any(c.isdigit() for c in pwd): score+=1
if any(c.isupper() for c in pwd): score+=1
if any(c in "!@#$" for c in pwd): score+=1
print(f"Strength: {score}/4")
if score==4: print("STRONG")
else: print("WEAK - add numbers, CAPS, symbols")
