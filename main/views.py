from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment,Like, Dislike,User
from django.utils import timezone

from django.views.decorators.http import require_POST
from django.http import HttpResponse
import json
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# mainpage view 함수
def showmain(request):
    posts = Post.objects.all()  # Blog 의 객체 모두를 가져옴
    return render(request, 'main/mainpage.html', {'posts': posts})




def showjypage(request):
    return render(request, "main/jypage.html")

@login_required
def detail(request, id):
    post = get_object_or_404(Post, pk = id)
    all_comments = post.comments.all().order_by('-created_at')
    return render(request, 'main/detail.html', {'post':post, 'comments':all_comments})

def posts(request):
    posts = Post.objects.all()
    return render(request, 'main/posts.html', {'posts': posts})

def new(request):
    return render(request, 'main/new.html')

@login_required
def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.user
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    new_post.image = request.FILES.get('image')
    new_post.save()
    return redirect('main:detail', new_post.id)

@login_required
def edit(request, id):
    edit_post = Post.objects.get(id=id)
    if request.user != edit_post.writer:
        messages.warning(request, "게시글 수정 권한이 없습니다.")
        return redirect("main:detail", id)
    
    return render(request, 'main/edit.html', {'post': edit_post})

@login_required
def update(request, id):
    update_post = Post.objects.get(id=id)
    update_post.title = request.POST['title']
    update_post.writer = request.user
    update_post.pub_date = timezone.now()
    update_post.body = request.POST['body']
    update_post.image = request.FILES.get('image')
    update_post.save()
    return redirect("main:detail", update_post.id)


@login_required
def delete(request, id):
    delete_post = Post.objects.get(id = id)
    
    if request.user != delete_post.writer:
        messages.warning(request, "게시글 삭제 권한이 없습니다.")
        return redirect("main:detail", id)
    delete_post.delete()
    return redirect('main:posts')

@login_required
def create_comment(request, post_id):
    new_comment = Comment()
    new_comment.writer = request.user
    new_comment.content = request.POST['content']
    new_comment.post = get_object_or_404(Post, pk=post_id)
    new_comment.save()
    return redirect('main:detail', post_id)


@login_required
def edit_comment(request, post_id, comment_id):
    # edit_post = Post.objects.get(id=id)
    post = Post.objects.get(id = post_id)
    edit_comment = Comment.objects.get(id = comment_id)
    
    if request.user != edit_comment.writer:
        messages.warning(request, "댓글 수정 권한이 없습니다.")
        return redirect("main:detail", post_id)
    
    return render(request, 'main/edit_comment.html', {'post':post, 'comment':edit_comment})


@login_required
def update_comment(request, post_id, comment_id):
    update_comment=get_object_or_404(Comment,pk=comment_id)
    if request.method == "POST":
        update_comment.content =request.POST['content']
        update_comment.save()
        return redirect('main:detail', update_comment.post.id)
    return render(request,'main:detail',{'comment':update_comment})


@login_required
def delete_comment(request, comment_id):
    delete_comment = Comment.objects.get(id=comment_id)
    
    if request.user != delete_comment.writer:
        messages.warning(request, "댓글 삭제 권한이 없습니다.")
        return redirect("main:detail", delete_comment.post.id)
    
    delete_comment.delete()
    return redirect('main:detail', delete_comment.post.id)

@require_POST
@login_required
def like_toggle(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    post_like, post_like_created = Like.objects.get_or_create(user=request.user, post=post)

    if not post_like_created:
        post_like.delete()
        result = "like_cancel"
    else:
        result = "like"
    context = {
        "like_count" : post.like_count,
        "result" : result
    }
    return HttpResponse(json.dumps(context), content_type = "application/json")

@require_POST
@login_required
def dislike_toggle(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    post_dislike, post_dislike_created = Dislike.objects.get_or_create(user=request.user, post=post)

    if not post_dislike_created:
        post_dislike.delete()
        result = "dislike_cancel"
    else:
        result = "dislike"
    context = {
        "dislike_count" : post.dislike_count,
        "result" : result
    }
    return HttpResponse(json.dumps(context), content_type = "application/json")

@login_required
def my_like(request, user_id):
    user = User.objects.get(id = user_id)
    like_list = Like.objects.filter(user = user)
    context = {
        'like_list' : like_list,
    }
    return render(request, 'main/my_like.html', context)