from pdf2image import convert_from_path
from PIL import Image, ImageDraw
import pytesseract
from Windows import EditPersonWindow

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class Processing():

    def __init__(self):
        self.convert(self.filename)
        date = self.ocr_core(self.filename)
        self.Name = date[9]
        self.Surname = date[7]
        self.Patronomic = date[11]
        self.Date_of_birth = date[12]
        self.Issued_by_whom = date[2] + date[3]
        self.Place_of_birth = date[14]

    def add_filename(self):
        self.filename = EditPersonWindow.EditPersonWindow.click_add_img_passport()

    def return_surname(self):
        return self.Surname

    def return_name(self):
        return self.Name

    def convert(self):
        images = convert_from_path(self.filename, poppler_path=r"poppler-22.11.0\Library\bin")
        for i in range(len(images)):
            images[i].save(self.filename.replace('.pdf', '') + '.jpg', 'JPEG')

    def ocr_core(self):
        image = Image.open(self.filename.replace('.pdf', '.jpg'))  # Открываем изображение.
        draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования.
        width = image.size[0]  # Определяем ширину.
        height = image.size[1]  # Определяем высоту.
        pix = image.load()
        for i in range(width):
            for j in range(height):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                S = a + b + c
                if (S > (((255 + 5) // 2) * 3)):
                    a, b, c = 255, 255, 255
                else:
                    a, b, c = 0, 0, 0
                draw.point((i, j), (a, b, c))
        for i in range(width):
            for j in range(height):
                a = pix[i, j][0] + 10
                b = pix[i, j][1] + 10
                c = pix[i, j][2] + 10
                if (a < 0):
                    a = 0
                if (b < 0):
                    b = 0
                if (c < 0):
                    c = 0
                if (a > 255):
                    a = 255
                if (b > 255):
                    b = 255
                if (c > 255):
                    c = 255
                draw.point((i, j), (a, b, c))
        image.save("temp.jpg", "JPEG")
        del draw
        text = pytesseract.image_to_string(('temp.jpg'), lang='rup')
        return text.split('\n')