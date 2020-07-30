from django.contrib import admin
from .models import Notices, Result, NewsTicker

class ResultAdmin(admin.ModelAdmin):
    list_display = ('batch', 'exam_year')
    fields = ('batch', 'exam_year', 'result_file')

admin.site.register(Notices)
admin.site.register(Result, ResultAdmin)
admin.site.register(NewsTicker)