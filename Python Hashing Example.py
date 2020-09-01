import hashlib
import time
print("This script helps to outline how hashing algorithms work")
print("You can learn more and do many things with hashlib. For better documentation visit")
print("https://docs.python.org/3/library/hashlib.html")
time.sleep(2)
print("Please enter value you want to hash (sha512 by default)")
on = input("")

result = on.encode()

print(hashlib.sha512(result).hexdigest())
