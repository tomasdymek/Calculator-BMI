from django.shortcuts import render
from .models import Bmi


def starting_page(request):
    return render(request, "blog/index.html")


def posts(request):
    return render(request, "blog/all-posts.html")


def post_detail(request):
    pass


def calculate_bmi(request):
    if request.method == 'POST':
        weight = float(request.POST['weight'])
        height = float(request.POST['height'])
        bmi_value = weight / ((height/100) ** 2)  # Obliczanie BMI
        bmi_obj = Bmi.objects.create(weight=weight, height=height, bmi=bmi_value)
        bmi_obj.save()
        return render(request, 'result.html', {'bmi': bmi_obj})
    return render(request, 'index.html')