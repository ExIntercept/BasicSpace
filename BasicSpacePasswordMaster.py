import time
from datetime import datetime
import hashlib

def now():
    day = datetime.now().day
    month = datetime.now().month
    year = datetime.now().year
    today = [day, month, year]
    return today

def encrypt(a, b, c):
    special_characters = {
        0: '@',
        1: '#',
        2: '$',
        3: '%',
        4: '&',
        5: '*',
        6: '+',
        7: '=',
        8: '?',
        9: '!'
    }
    encryptedString = ""
    reversedString = ""
    for i in [a, b, c]:
        for digit in str(i):
            if digit.isdigit():
                encryptedString += special_characters[int(digit)]
            else:
                encryptedString += digit
    for j in reversed(encryptedString):
        reversedString += j
    return reversedString

       
def generatePassword(passwordRecipe):
    a = passwordRecipe[0]
    b = passwordRecipe[1]
    c = passwordRecipe[2]
    unhashedString = encrypt(a, b, c)
    hashedString = hashlib.sha256(unhashedString.encode()).hexdigest()
    return hashedString

passwordRecipe = now()
print(passwordRecipe)
print("Password: ", generatePassword(passwordRecipe))

input("Press Enter to exit...")#needed if converted to exe
