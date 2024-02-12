import socket
import time
from datetime import datetime
import hashlib

def now():
    day = datetime.now().day
    month = datetime.now().month
    year = datetime.now().year
    today = [day, month, year]
    return today

def encrypt(a,b,c):
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
    for i in [a,b,c]:
        for digit in str(i):
            if digit.isdigit():
                encryptedString += special_characters[int(digit)]
            else:
                encryptedString += digit
    for j in reversed(encryptedString):
        reversedString += j
    return (reversedString)

def generatePassword(passwordRecipe):
    a = passwordRecipe[0]
    b = passwordRecipe[1]
    c = passwordRecipe[2]
    unhashedString = encrypt(a,b,c)
    hashedString = hashlib.sha256(unhashedString.encode()).hexdigest()
    return hashedString

try: #create server                                                                                                     #vulnerability, no hash author verification. Fix by putting this code in main
    SERVER_ADDRESS = ('localhost', 12345)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(SERVER_ADDRESS)
    server_socket.listen(5)
    print('Server listening on', SERVER_ADDRESS)
    
    while True:
        client_socket, client_address = server_socket.accept()
        print('Connection from', client_address)
        data = client_socket.recv(1024)
        if data.decode() == 'generatePassword': #if this message recieved
            passwordRecipe = now()
            encryptedPassword = generatePassword(passwordRecipe)
            print(encryptedPassword, "sent successfully")
            client_socket.sendall(encryptedPassword.encode())
            client_socket.close()  # Close the connection after sending the password
except Exception as e:
    print("An error occurred:", e)
finally:
    server_socket.close()
