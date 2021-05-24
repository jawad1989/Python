from PIL import Image, ImageFilter

image = Image.open('D:\Code\Python\scripting\image-playground\images\mountain.jpg')
print(image.size)

new_image = image.resize((400,400))
new_image.save("D:\Code\Python\scripting\image-playground\images\mountain-resize.jpeg")

image.thumbnail((400,400))
image.save("D:\Code\Python\scripting\image-playground\images\mountain-thumb.jpeg")
print(image.size)