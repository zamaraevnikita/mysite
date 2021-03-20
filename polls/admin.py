from django.contrib import admin

from .models import Question, Choice

class ChoiceAdmin(admin.TabularInline):
    fieldsets = [
        ("Вариант ответа", {"fields" : ["text", "votes"]} ),
    ]
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Текст вопроса", {"fields" : ["text"]} ),
        ("Дата создания вопроса", {"fields" : ["pub_date"]} ),

    ]
    inlines = [ChoiceAdmin]
    list_filter = ["pub_date"]
    search_fields = ["text"]


#register (МОДУЛЬ, СВЯЗАННАЯ АДМИНКА, МОДЕЛЬ (ПАНЕЛЬ))
admin.site.register(Question, QuestionAdmin)