#Importing necessary (pytesseract and Pillow) modules
import pytesseract
from PIL import Image
import pyttsx3
from googletrans import Translator
#Defining path of tesseract software
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#path of image file(jpg & png only)
image_file = r'C:\Users\Susandhi Pal\Desktop\Image-text-speech\input_images\Image1.jpg'
img = Image.open(image_file)
img.show()
text = pytesseract.image_to_string(image_file)
print(text)
output_file = open("output_file.txt", "w")
output_file.write(text)
p = Translator()
k = p.translate(text, dest = 'english')
engine = pyttsx3.init()
engine.say(k)
engine.runAndWait()