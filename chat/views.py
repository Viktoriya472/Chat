from django.shortcuts import render
from django.http import HttpResponseForbidden
from main.models import Users
from django.views.generic import ListView


class Chat(ListView):
    model = Users
    template_name = "chat.html"
    context_object_name = "users"


# def chat(request):
#     users = User.objects.all().values_list("username")
#     return render(request, "chat.html", {"users": users})


def room(request, user_id):
    try:
        user = request.user.id
    except:
        return HttpResponseForbidden()
    return render(request, "room.html", {"user": user})
