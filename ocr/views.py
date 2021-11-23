from django.shortcuts import render
from PIL import Image
import pytesseract
import pdfplumber


def index(request):
    pytesseract.pytesseract.tesseract_cmd = 'tess/tesseract.exe'
    context = {}
    if request.method == "POST":
        file = request.FILES.get('tesbefore')

        if file:
            t = file.content_type.split('/')
        else:
            return render(request, "error/notfound.html")
        if t[0] == "image":
            im = Image.open(file)
            text = pytesseract.image_to_string(
                im, lang=request.POST.get("from"))
            context.update({
                'after': text,

            })

            context.update({
                'after': text,
            })
        else:
            return render(request, "error/notfound.html")
    return render(request, "ocr/index.html", context)
