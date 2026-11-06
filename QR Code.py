import qrcode

link = input("Enter the link you want to generate a QR code for: ")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(link)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("My QR Code.png")

img.show()  

print("QR code generated successfully!")