from django.contrib import admin

from .models import Calories
from .models import Bmi

# Register your models here.


# admin.site.register(Bmi)
# admin.site.register(Calories)

@admin.register(Bmi)
class BmiAdmin(admin.ModelAdmin):
    list_display = ['id', 'status']
    list_filter = ['status']


@admin.register(Calories)
class CaloriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'status']