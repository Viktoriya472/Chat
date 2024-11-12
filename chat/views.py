from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from django.views.generic import ListView


class Chat(ListView):
    model = User
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
