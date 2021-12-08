import os
import base64
from PIL import Image

filePath = input('Please enter the file path of the desired image: ')
Size = input('Enter the width of your desired size: ')
imageSize = int(Size)
fileType = input('What is the type of file: ')
front = "data:image/{};base64,".format(fileType)

savePath = input('Enter the file path where you would like it saved as well as the name of the image EX(C:/Users/Christopher/Desktop/Saved-Image.jpg): ')

path = filePath
newPath = path.replace(os.sep, '/')

image = Image.open(newPath)
image.thumbnail((imageSize, imageSize))
image.save(savePath)

save_file_path = savePath
newSavePath = save_file_path.replace(os.sep, '/')

with open(newSavePath, "rb") as img_file:
    my_string = base64.b64encode(img_file.read())

print(front + str(my_string.decode('utf-8')))

input('Press ENTER to exit')
