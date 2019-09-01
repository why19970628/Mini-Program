import pytesseract
from PIL import Image,ImageEnhance,ImageFilter
import cv2
img = Image.open('0.jpg')
text = pytesseract.image_to_string(img,lang='chi_sim')
print(text)
# 将图片变成灰色
img_gray = img.convert('L')
img_gray.save('./tmp/ode_gray.png')
 # 转成黑白图片
img_black_white = img_gray.point(lambda x: 0 if x > 200 else 255)
pic1='./tmp/code_black_white.png'
img_black_white.save(pic1)

#要去掉黑点，就是一个二值化降噪的过程。可以用PIL（Python Image Library）试试
im = Image.open(pic1)
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('./tmp/jiangzao.png')
#im.show()
pytesseract.pytesseract.tesseract_cmd = 'C://Program Files (x86)/Tesseract-OCR/tesseract.exe'
#text = pytesseract.image_to_string(Image.open('./tmp/jiangzao.png'),lang='chi_sim')##,lang='eng 数字
text = pytesseract.image_to_string(im,lang='chi_sim')
print(text)
#image = Image.open('1.jpg')
#code = pytesseract.image_to_string(image)
#print(code)
