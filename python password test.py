import random
import time
element = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
panjang_password = int(input("Passwordnya mau berapa karakter?"))

password = ""
for i in range(panjang_password):
    password += random.choice(element)
    
    print(password)
time.sleep(2)
    print("password anda ada di line terakhir ya!")
