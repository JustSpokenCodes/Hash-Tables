import time
import hashlib
import bcrypt 

def myFakeHash(word):
    hash = len(word)
    return hash 

myFakeHash('Joshua') # --> 6
myFakeHash('Jessia') # --> 6

#scamble the key and comeup with very different values
def djb2(key):
    # start from a large prime number
    hash_value = 5381

    # randomly scrambling it by using bit-shifting
    for char in key:
        hash_value = hash_value + (hash_value << 5) + char 

    return hash_value

key = b"mypassword"

n = 10000

start_time = time.time()
for i in range(n):
    djb2(key)
end_time = time.time()
print("djb2 run time: ", end_time - start_time)

start_time = time.time()
for i in range(n):
    hashlib.sha256(key)
end_time = time.time()
print("sha256 run time: ", end_time - start_time)

start_time = time.time()
salt = bcrypt.gensalt()
for i in range(n):
    bcrypt.hashpw(key,salt)
end_time = time.time()

print("hashpw run time: ", end_time - start_time) # omg this takes so long!!