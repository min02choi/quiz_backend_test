# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializer import QuizSerializer
import random

# HelloAPI로 파악하기, get 메소드 방식
@api_view(['GET'])
def helloAPI(request):
    return Response("hello world!")

# 만들 API: 주어진 개수만큼 랜덤한 퀴즈를 반환하는 API
# 랜덤으로 선택할 것이므로 random 모듈 사용. totalQuizs 질문들을 불러와 개수는 id개만큼 뽑음
@api_view(['GET'])
def randomQuiz(request, id):
    totalQuizs = Quiz.objects.all()
    randomQuizs = random.sample(list(totalQuizs), id)
    serializer = QuizSerializer(randomQuizs, many=True)     # many=True시 다수의 데이터에 대해서도 직렬화 진행
    return Response(serializer.data)