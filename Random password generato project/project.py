#random password genertor
import random
print("welcome to random password generator")
randomchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&"
numofpwd = int(input("enter the number of password to be generated:"))
pwdlen = int(input("plase eneter the lenght of the password needed:"))

print("here are ur random password:")
for i in range(numofpwd):
    pwd = ""
    for char in range(pwdlen):
        pwd = pwd + random.choice(randomchars)
    print(pwd)

