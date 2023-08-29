import qrcode

# Data to encode
data = ('https://www.w3schools.com/')
  
# Creating an instance of QRCode class
qr = qrcode.QRCode(version = 1,           
                   box_size = 15,          
                   border = 2)
 
# Adding data to the instance 'qr'
qr.add_data(data)   

# if fit value true then give the output
qr.make(fit = True)   
img = qr.make_image(fill_color = 'white',
                    back_color = 'black')
 
img.save('MyQRCode2.png')
