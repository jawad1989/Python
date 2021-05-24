
"""
Work with images: sharpen, blur, grayscale, rotate, open/save, show
"""
from PIL import Image, ImageFilter

image = Image.open('images/pikachu.jpg')
print(image.size)

# # smoother_image = image.filter(ImageFilter.SMOOTH)
# # sharpen_image  = image.filter(ImageFilter.SHARPEN)
# filtered_image = image.filter(ImageFilter.BLUR)
# filtered_image.save("D:\Code\Python\scripting\image-playground\images\jsblur.png","png")

# # convert to gray scale
# grayscale   = image.convert("L")
# rotation_90 = grayscale.rotate(90)
# rotation_90.save("D:\Code\Python\scripting\image-playground\images\grayscale.png","png")
# # rotation_90.show()

# # resize image
# resize_90 = grayscale.resize((300,300))
# resize_90.save("D:\Code\Python\scripting\image-playground\images\jsreized.png","png")
# # resize_90.show()

# #crop image
# (left, upper, right, lower) = (20, 20, 400, 400)
# im_crop = grayscale.crop((left, upper, right, lower))
# im_crop.save("D:\Code\Python\scripting\image-playground\images\jsreized.png","png")
# im_crop.show()


# print(image)
# print(image.format)
# print(image.size)
# print(image.mode)
# print(dir(image))
