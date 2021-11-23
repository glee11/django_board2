from django.shortcuts import render
from PIL import Image
import pdfplumber


def index(request):
    context = {}
    if request.method == "POST":
        file = request.FILES.get('tesbefore')
        if file:
            t = file.content_type.split('/')
        else:
            return render(request, "error/notfound.html")
        print(t[1])
        if t[0] == "application" and t[1] == "pdf":
            text = ''
            with pdfplumber.open(file) as pdf:
                for i in range(len(pdf.pages)):
                    first_page = pdf.pages[i]
                    print(first_page.extract_text())
                    if first_page.extract_text() is None:
                        text = first_page.extract_tables()
                    else:
                        text += first_page.extract_text()
                    print(i+1)

            context.update({
                'after': text,
            })

        else:
            return render(request, "error/notfound.html")
    return render(request, "pdf/index.html", context)
