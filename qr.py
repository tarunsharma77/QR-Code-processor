import qrcode
from PIL import Image


logo_url = 'pic.png'  # image name

logo = Image.open(logo_url)
basewidth = 100

# adjust given image size
wpercent = (basewidth / float(logo.size[0]))
hsize = int((float(logo.size[1]) * float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)

# adjust the size of the qr code image
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

#url of a website
url = 'http://todo-tanyasharma.herokuapp.com/'
qr.add_data(url)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="green", back_color="white")

# set position of given image on the qr code image
pos = ((qr_img.size[0] - logo.size[0]) // 2,
       (qr_img.size[1] - logo.size[1]) // 2)
qr_img.paste(logo, pos)

#generate a png file which has the output as a qrcode
qr_img.save('new.png')
print("Qr generated")