
#!/usr/bin/python
# -*- coding: utf-8 -*-
import pyqrcode
import os
from pyqrcode import QRCode
user = input('Enter your text>>  ')
user = str(user)
s = user
url = pyqrcode.create(s)
url.svg('myqr.svg', scale=9)
print ()
print ()
print ()
print 'Your qrcode text is >>>>'
print user
print ()
print ()
print ()
print ()
