import pyqrcode
import png
from pyqrcode import QRCode

qrstring = 'https://www.youtube.com/watch?v=mo1JL7Uyzws'

url = pyqrcode.create(qrstring)

url.png(r'C:\Users\berna\Downloads\qr.png', scale=8)
