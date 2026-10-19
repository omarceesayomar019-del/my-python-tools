import random, string
chars=string.ascii_letters+string.digits+"!@#"
pwd="".join(random.choice(chars) for _ in range(12))
print("Generated:",pwd)
