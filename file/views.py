from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import FileModel
from .models import Form
from utils.upload_functions import convert_string_type, get_total_value


def uploader(request):
    message = "Envie o arquivo CNAB:"
    total = 0
    if request.method == "POST":
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            for row in request.FILES["docfile"]:

                year = str(row)[3:7]
                month = str(row)[7:9]
                day = str(row)[9:11]

                hour = str(row)[44:46]
                minute = str(row)[46:48]
                second = str(row)[48:50]

                cnab_file = {
                    "tipo": convert_string_type(str(row)[2]),
                    "data": f"{day}/{month}/{year}",
                    "valor": int(str(row)[12:21])/100,
                    "CPF": str(row)[21:32],
                    "cartao": str(row)[32:44],
                    "hora": f"{hour}:{minute}:{second}", 
                    "dono": str(row, "utf-8")[48:62],
                    "nome_loja": str(row, "utf-8")[62:80]
                }

                new_file = FileModel(**cnab_file)
                new_file.save()



            return redirect("uploader")
        else:
            message = "The form is not valid. Fix the following error:"
    else:
        form = Form()

    files = FileModel.objects.all()
 
    total = get_total_value(files)



    context = {"files": files, "form": form, "message": message, "total": total}
    return render(request, "index.html", context=context)
