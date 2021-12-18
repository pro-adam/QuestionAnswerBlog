from django.core import paginator
from django.shortcuts import render
from django.core.paginator import Paginator
from . models import Question,Answer,Comment


def home(request):
    if 'q' in request.method == 'GET':
        q = request.GET.get('q')
        questions = Question.objects.filter(title__icontains=q).order_by('-id')
    else:
        questions = Question.objects.all().order_by('-id')
    print(questions)
    paginator = Paginator(questions,2)
    page_num = request.GET.get('page',1)
    questions = paginator.page(page_num)
    context = {
        'questions':questions,
    }
    return render(request,'main/home.html',context)


def detail(request,id):
    question = Question.objects.get(pk=id)
    answer = Answer.objects.get(question=question)
    comments = Comment.objects.filter(answer=answer)
    tags = question.tags.split(',')
    context = {
        'question':question,
        'answer':answer,
        'comments':comments,
        'tags':tags
    }
    return render(request,'main/detail.html',context)
