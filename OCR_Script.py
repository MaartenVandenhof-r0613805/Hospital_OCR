from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import requests
import pytesseract as pt


# load image from the IAM database (actually this model is meant to be used on printed text)
img = 'F:\\Projects\\Hospital_OCR\\images\\14752-15876807.jpg'
img = "F:\\Projects\\Hospital_OCR\\images\\polsbandje-e1567792095992-1024x1024.jpg"
img = "F:\\Projects\\Hospital_OCR\\images\\polsbandjeweb.jpg"
img = "F:\\Projects\\Hospital_OCR\\images\\true_img.jpg"
# image = Image.open(img).convert("RGB")

# processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-printed')
# model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-printed')
# pixel_values = processor(images=image, return_tensors="pt").pixel_values

# generated_ids = model.generate(pixel_values)
# generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
# print(generated_text)


# TESSERACT TEST
pt.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

content = pt.image_to_string(img)

print(content.lower().strip())