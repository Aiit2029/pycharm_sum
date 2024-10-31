from django.shortcuts import render

from app241030 import models


# Create your views here.
def  index(request):

    # student_object = models.Student(
    #     name = 'alex',
    #     age = 23,
    # )
    # student_object.save()

    # 方式2
    new_object = models.Student.objects.get()
    print(new_object.name)
    print(new_object.age)




    return render(request,'index.html')