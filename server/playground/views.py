from django.shortcuts import render
from django.http.response import JsonResponse
from playground.models import Questions
from playground.serializers import QuestionsSerailizer
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Create your views her

@csrf_exempt
def addQuestion(request):
    question = JSONParser().parse(request)
    questions_serializer=QuestionsSerailizer(data=question)
    if questions_serializer.is_valid():
        questions_serializer.save()
        return JsonResponse(True, safe=False)
    return JsonResponse(False, safe=False) 


@csrf_exempt
def getAllQuestions(request):
    questions = Questions.objects.all()
    questions_serializer = QuestionsSerailizer(questions, many=True)
    return JsonResponse(questions_serializer.data, safe=False)


@csrf_exempt
def deleteQuestion(request):
    questionJson = JSONParser().parse(request)
    question = Questions.objects.get(QuestionId=questionJson["id"])
    question.delete()
    return JsonResponse("Delete Success", safe=False)
