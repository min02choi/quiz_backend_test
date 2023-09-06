from rest_framework import serializers
from .models import Quiz


# Quiz 모델 데이터가 주어지면 title, body, answer을 담고 있는 JSON 타입의 데이터로 변환해주는 시리얼라이저
class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('title', 'body', 'answer')    # fields 변수의 값은 Model에 있는 변수의 이름이어야 함