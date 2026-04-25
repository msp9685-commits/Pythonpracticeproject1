import qrcode

intro = "https://www.geeksforgeeks.org/python/generate-qr-code-using-qrcode-in-python/"
img = qrcode.make(intro)
img.save("Firstqrcode.png")