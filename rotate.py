from PIL import Image


imageFileName = 'minamiPic.jpeg'
Image = Image.open(imageFileName)

# box tuple (x_start, y_start, x_end, y_end)
# These counts start from left-top
# In this case, the size is (360 * 576)
croppedIm = Image.crop((360, 288, 720, 864))
# croppedIm.save('cropped.png')

croppedIm.rotate(6).save('rotated6.png')
croppedIm.rotate(6, expand=True).save('rotate6_expanded.png')

