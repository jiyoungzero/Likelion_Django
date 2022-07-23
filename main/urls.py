from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    # mainpage URL 연결하기 with 별명사용
    path('', showmain, name="showmain"),
    # firstpage URL 연결하기 with 별명사용

    path('jypage/', showjypage, name="showjypage"),

    path('<int:id>', detail, name="detail"),

    path('new/', new, name="new"),
    path('posts/', posts, name="posts"),

    path('create/', create, name="create"),

    path('edit/<int:id>', edit, name="edit"),

    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
    path('<str:post_id>/create_comment', create_comment, name="create_comment"),
    
    path('<str:post_id>/<str:comment_id>/edit_comment', edit_comment, name="edit_comment"),    
    path('<str:post_id>/<str:comment_id>/update_comment', update_comment, name="update_comment"),    
    path('<str:comment_id>/delete_comment', delete_comment, name="delete_comment"),
    
    # like, dislike toggle
    path('like_toggle/<int:post_id>/', like_toggle, name="like_toggle"),
    path('dislike_toggle/<int:post_id>/', dislike_toggle, name="dislike_toggle"),
    
    # 좋아요 목록
    path('my_like/<int:user_id>/', my_like, name="my_like"),
]
