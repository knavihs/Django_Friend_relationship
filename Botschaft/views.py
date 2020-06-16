from django.shortcuts import render

from .models import Botschaft
from users.models import People,Relationship
from .forms import Msg_form

# Create your views here.
def message_win(request,from_person):
     from_pep = People.objects.get(Name= from_person)
     friend_list = Relationship.objects.filter(from_person=from_pep)
     msg_form = Msg_form()
     print(from_pep)
     print(friend_list)
     msg_model =Botschaft.objects.all()
     return render(request,'botschaft/msg_window.html',{'from_pep':from_pep,'msg_model':msg_model,'friend_list':friend_list,'msg_form':msg_form})


def send_msg(request,from_person):

     from_pep = People.objects.get(Name=from_person)
     friend_list = Relationship.objects.filter(from_person=from_pep)
     if request.method=='POST':
          msg_form=Msg_form(request.POST)
          if msg_form.is_valid():
               msg_content = request.POST['msg']
               to_friend = request.POST["dost"]
               to_pep = People.objects.get(Name=to_friend)
               msg_model=Botschaft(from_person=from_pep,to_person=to_pep,msg=msg_content)
               msg_model.save()
               msg_model = Botschaft.objects.all()
               return render(request,'botschaft/msg_window.html',{'from_pep':from_pep,'msg_model':msg_model,'friend_list':friend_list,'msg_form':msg_form})

