import hashlib
import time
print("This script helps to outline how hashing algorithm works")
print("You can learn and do many things with hashlib for better documentation visit")
print("https://docs.python.org/3/library/hashlib.html")
time.sleep(2)
print("Please enter value you want to encrypt (sha512)")
on = input("")

result = on.encode()

print(hashlib.sha512(result).hexdigest())