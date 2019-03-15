from django.shortcuts import render
from .models import Talk


def get_talks(request):
    data = Talk.objects.all()
    return render(request, '', {'data': data})


# def get_talk_id(request):
#     data = Talk.objects.filter(id=1)
#     return render(request, '', {"data": data})


def insert(request):
    data = Talk.objects.create(name='test')
    return render(request, '', {"data": data})


# def update(request):
#
#     return render(request, '', )
#
#
# def delete(request):
#
#     return render(request, '', )


# GetTalks() -returns list of talks
# GetTalk(int ID)
# Insert(Talk)
# Update(Talk,ID)
# Delete(ID)
