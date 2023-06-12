from django.shortcuts import render
from .models import Bmi
from .models import Calories

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
        bmi_value = int(weight / ((height / 100) ** 2))
        bmi_obj = Bmi.objects.create(weight=weight, height=height, bmi=bmi_value)
        bmi_obj.save()


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


def calculate_calories(request):
    if request.method == 'POST':
        age = int(request.POST['age'])
        weight = float(request.POST['weight'])
        height = float(request.POST['height'])
        status = request.POST['status']
        gender = request.POST['gender']

        if gender == 'male':
            if status == 'no':
                calories_value = int(10 * weight + 6.25 * height - 5 * age + 5)
                description = "No physical activity: You have a sedentary lifestyle with no regular exercise."
            elif status == 'little':
                calories_value = int(10 * weight + 6.25 * height - 5 * age + 200)
                description = "Little physical activity: You engage in light exercises 1-3 times a week."
            elif status == 'average':
                calories_value = int(10 * weight + 6.25 * height - 5 * age + 400)
                description = "Average physical activity: You engage in moderate exercises 3-5 times a week."
            elif status == 'high':
                calories_value = int(10 * weight + 6.25 * height - 5 * age + 600)
                description = "High physical activity: You engage in intense exercises daily."
            else:
                calories_value = 1500
                description = "Unknown activity level"

        elif gender == 'female':
            if status == 'no':
                calories_value = int(10 * weight + 6.25 * height - 5 * age - 161)
                description = "No physical activity: You have a sedentary lifestyle with no regular exercise."
            elif status == 'little':
                calories_value = int(10 * weight + 6.25 * height - 5 * age + 39)
                description = "Little physical activity: You engage in light exercises 1-3 times a week."
            elif status == 'average':
                calories_value = int(10 * weight + 6.25 * height - 5 * age + 239)
                description = "Average physical activity: You engage in moderate exercises 3-5 times a week."
            elif status == 'high':
                calories_value = int(10 * weight + 6.25 * height - 5 * age + 439)
                description = "High physical activity: You engage in intense exercises daily."
            else:
                calories_value = 1500
                description = "Unknown activity level"

        else:
            calories_value = 1500
            description = "Unknown gender"

        return render(request, 'blog/result_calories.html', {'calories': calories_value, 'description': description})

    return render(request, 'blog/index.html')
