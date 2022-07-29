from main.models import Post, User
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.


def mypage(request, id):
    user = get_object_or_404(User, pk=id)
    context = {
        'user':user,
        'posts':Post.objects.filter(writer=user),
        # 'followings' : user.profile.followings.all(),
        # 'followers' : user.profile.followers.all(),
    }

    return render(request, 'users/mypage.html', context)
