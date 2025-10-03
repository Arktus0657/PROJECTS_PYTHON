import qrcode as qr

img = qr.make("https://www.india.gov.in/")
img.save("Portal of India.png")