import hashlib

password = '3214858235'

result = hashlib.sha256(password.encode())
print(password.encode())