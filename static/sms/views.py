from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from teachers.models import TeacherInfo
from students.models import StudentInfo

@login_required
def index(request):
    context = {
       'teachers': TeacherInfo.objects.count(),
       'students': StudentInfo.objects.count()
    }
    return render(request, "home.html", context)



