from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name= "home"),
    path('login/',views.login_view,name='Login_view'),
    path('login/submission/',views.login_view_submission,name='login_view_submission'),
    path('create/',views.create_user,name= "create_user"),
    path('create/submission/',views.create_user_submission,name= "create_user_submission"),
    path('login/<str:profile>/<int:friend_id>/', views.add_friend, name='add_Friend'),
    path('login/post/<str:profile>', views.post_view, name='post_view')
]
