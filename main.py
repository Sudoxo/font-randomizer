import sys
from PIL import Image
import pytesseract

spacing = 50
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

im1 = Image.open('example5.png')
w,h = im1.size
letters = pytesseract.image_to_boxes(im1).split("\n")
available_letters = []
for i in range(len(letters)):
    letters[i] = letters[i].split(" ")
    if letters[i][0] not in available_letters:
        available_letters.append(letters[i][0])

#print(avaiable_letters)
#print(pytesseract.image_to_string(im1))
#print(letters)

user_text = input("Enter your text: ")

images = []
spaces,widths,heights = 0,0,0

for c in user_text:
    if c == " ":
        spaces +=1
        images.append(" ")
        continue
    if(c not in available_letters):
        print("Letter '" + c + "' not found")
        continue
    for letter in letters:
        if(letter[0] == c):
            char_img = im1.crop((int(letter[1]),h-int(letter[4]),int(letter[3]),h-int(letter[2])))
            images.append(char_img)
            widths+=char_img.size[0]
            heights=max(char_img.size[1],heights)
            break

total_width = widths+spacing*len(images)+spaces*spacing*2
max_height = heights

new_im = Image.new('RGB', (total_width, max_height), "white")

x_offset = 0
for im in images:
    if im == " ":
        x_offset += spacing*2
    else:
        new_im.paste(im, (x_offset,0))
        x_offset += (im.size[0]+spacing) 

new_im.save('test1.jpg')   


