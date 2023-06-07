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
        bmi_value = int(weight / ((height / 100) ** 2))  # Obliczanie BMI
        bmi_obj = Bmi.objects.create(weight=weight, height=height, bmi=bmi_value)
        bmi_obj.save()

        # Opisy wyników BMI
        if bmi_value < 18.5:
            description = "Underweight - You should eat more."
            bmi_category = 'underweight'
        elif bmi_value >= 18.5 and bmi_value < 25:
            description = "Normal weight - Keep up the good work!"
            bmi_category = 'normal'
        elif bmi_value >= 25 and bmi_value < 30:
            description = "Overweight - You should eat less."
            bmi_category = 'overweight'
        else:
            description = "Obese - You should consult a doctor."
            bmi_category = 'obese'

        return render(request, 'blog/result.html', {'bmi': bmi_obj, 'description': description, 'bmi_category': bmi_category})

    return render(request, 'blog/index.html')

