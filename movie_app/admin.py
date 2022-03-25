from csv import list_dialects
from django.contrib import admin
from .models import Movie
from django.db.models import QuerySet

# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'rating', 'year', 'budget', 'currency', 'raiting_status']
    list_editable = ['rating', 'year', 'budget', 'currency'] # Редаг. в админ панели
    list_per_page = 10 # Пагинация в админ панели
    # ordering = ['rating', 'name'] сортировка
    prepopulated_fields = {"slug": ("name",)}
    actions = ['set_dollars', 'set_euro', 'set_uah']

    @admin.action(description='Установить валюту в Долар')
    def set_dollars(self, request, qs: QuerySet):
        qs.update(currency=Movie.USD)

    @admin.action(description='Установить валюту в Евро')
    def set_euro(self, request, qs: QuerySet):
        qs.update(currency=Movie.EUR)
    
    @admin.action(description='Установить валюту в Гривню')
    def set_uah(self, request, qs: QuerySet):
        qs.update(currency=Movie.UAH)

    @admin.display(ordering='rating', description='Статус')
    def raiting_status(self, nov: Movie):
        if nov.rating < 50:
            return 'Зачем это смотреть!?'
        if nov.rating < 70:
            return 'Разок можно глянуть'
        if nov.rating <=80:
            return 'Зачет'
        return 'ТОП'
        


