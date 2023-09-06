from django.db import models


# 데이터베이스 Quiz 테이블에 schema 설정
class Quiz(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    answer = models.IntegerField()