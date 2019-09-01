import pytesseract
from PIL import Image,ImageEnhance,ImageFilter
import cv2
img = Image.open('6.png')
#text = pytesseract.image_to_string(img,lang='chi_sim')
pytesseract.pytesseract.tesseract_cmd = 'C://Program Files (x86)/Tesseract-OCR/tesseract.exe'
text = pytesseract.image_to_string(img,lang='chi_sim')
print(text)


#TESSDATA_PREFIX
#C:\Program Files (x86)\Tesseract-OCR\tessdata