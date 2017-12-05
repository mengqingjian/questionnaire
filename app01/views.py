from django.shortcuts import render,HttpResponse

# Create your views here.
from app01 import models
def login(request):
    if request.is_ajax():
        username=request.POST.get("username")
        print("+++++",username)
        password=request.POST.get("password")
        login_response={"is_login":False,"error_msg":None}
        user=models.UserInfo.objects.filter(username=username,password=password)
        if user:
            login_response["is_login"]=True
        else:
            login_response["error_msg"]="username and password error"
        import json
        return HttpResponse(json.dumps(login_response))
    return render(request,"login.html")
def index(request):
    Questionnaire_list = models.Questionnaire.objects.all()
    return render(request, "index.html", {"Questionnaire_list": Questionnaire_list})
def questionnaire(request):
    question_obj=models.Question.objects.all()
    return render(request,"questionnaire.html",{"question_obj":question_obj})
