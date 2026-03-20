import qrcode 
img= qrcode.make("https://www.youtube.com/results?search_query=apna+college")
img.save("apna+college_web.png")