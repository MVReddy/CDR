from django.http import HttpResponse
from polls.models import Question
from django.shortcuts import get_object_or_404


def index(request):

    q = get_object_or_404(Question, id=1)


    try:
        q = Question.objects.get(id=2)
    except Question.DoesNotExist:
        q = Question()
        q.question_text = ""
        q.save()

    return HttpResponse("Hello, world. New Resposne ")
