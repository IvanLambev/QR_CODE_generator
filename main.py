import qrcode



def qr_code():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data('https://www.youtube.com/watch?v=ePAJPKTktsk')
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save('qrcode.png') # save the image to a file



if __name__ == '__main__':
    qr_code()

