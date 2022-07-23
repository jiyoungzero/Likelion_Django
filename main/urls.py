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
]
