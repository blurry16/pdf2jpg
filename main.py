from pdf2image import convert_from_path
import os

PDF_FOLDER = ""  # input folder
JPG_FOLDER = ""  # output folder
POPPLER_PATH = ""  # /bin/ folder of poppler

for filename in os.listdir(PDF_FOLDER):
    name, ext = os.path.splitext(filename)
    if ext.lower() == ".pdf":
        images = convert_from_path(fr"{PDF_FOLDER}\{filename}",
                                   poppler_path=POPPLER_PATH)
        for i in range(len(images)):
            output = fr"{JPG_FOLDER}\{name}{f'({str(i + 1)})' if len(images) > 1 else ''}.jpg"
            print(f"Saving {output}")
            images[i].save(output, "JPEG")
