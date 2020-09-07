# Import QRCode from pyqrcode 
import pyqrcode
import os
from pyqrcode import QRCode

user = input('Enter your text>>  ')
user = str(user)



# String which represent the QR code 
s = user

# Generate QR code 
url = pyqrcode.create(s) 

# Create and save the png file naming "myqr.png" 
url.svg("myqr.svg", scale = 9) 


print()
print()
print()
print("Your qrcode text is >>>>")
print(user)
print()
print()
print()
print()
