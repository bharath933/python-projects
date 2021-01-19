import pyqrcode
from pyqrcode import QRCode

qr_link = " https://bharatkaparapu4.wixsite.com/bharatkumarkaparapu"

url = pyqrcode.create(qr_link)

qr = url.svg("qr_code.svg",scale=10)

print("qr code is saved to location")