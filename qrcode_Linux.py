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
new = input('Enter your file name>>>   ')
print ()
print ()
print ()
print 'Your qrcode text is >>>>'
print user
print ()
print ()
print ()
print ()
old_file = 'myqr.svg'
new_file = new + '.svg'
os.rename(old_file, new_file)
print 'Done!'
print '
