from django.contrib import admin
from .models import Quiz

# 이렇게 등록을 할 시 관리자 페이지에서 Quiz모델을 관리할 수 있음
admin.site.register(Quiz)
