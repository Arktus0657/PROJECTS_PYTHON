import qrcode

img = qr.make("https://www.india.gov.in/")
img.save("Portal of India.png")