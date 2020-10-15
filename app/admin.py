from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm

"""
Есть две модели в БД: автомобиль (марка, модель), обзорная статья 
(автомобиль, заголовок статьи, текст обзора). Нужно сделать админку:

1 С выводом в таблицу списка объектов.
2 Добавить поиск по названиям и заголовкам и фильтры по основным полям.
3 Для модели автомобиля добавить кастомное поля, в котором выводить количество 
статей про данный автомобиль.
+ 4 Русифицировать отображение название моделей в админке (car -> машина).
+ 5 Поменять порядок вывода объектов в списке (например от элемента с большим id 
к элементу с меньшим). Тогда новые записи будут наверху.
"""


class CarAdmin(admin.ModelAdmin):

    list_display = ('brand', 'model', 'review_count')
    list_filter = ('brand', 'model')
    search_fields = ('brand', 'model')

    def review_count(self, obj):
        return obj.review_count()


class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm

    list_display = ('car', 'title')
    search_fields = ('car__model', 'title')




admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
