from django.urls import path
from . import views
app_name ='botschaft'
urlpatterns = [
    path('<str:from_person>/',views.message_win,name='message_win'),
    path('<str:from_person>/msg/',views.send_msg,name='send_msg'),
    ]