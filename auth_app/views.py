from django.shortcuts import render
from django.shortcuts import render
from auth_app.models import User, UserToken
from django.utils import timezone

def user_detail(request, uuid):
  user_obj= User.objects.get(uuid=uuid)
  context = {
      "user": user_obj,
  }
  return render(request, "user_detail.html", context)

def allusers_detail(request):
  user_objs= User.objects.all()
  context = {
      "users": user_objs,
  }
  return render(request, "users_detail.html", context)

