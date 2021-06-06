from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['ques_txt']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('ques_txt', 'pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['ques_txt']

admin.site.register(Question, QuestionAdmin)