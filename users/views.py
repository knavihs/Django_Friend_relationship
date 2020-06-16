from django.shortcuts import render,HttpResponseRedirect,get_object_or_404
from .forms import create_user_form,login_form,Post_form
from .models import People,Relationship,Posts
from passlib.hash import pbkdf2_sha256
from tkinter.messagebox import *
from django.http import Http404

# Create your views here.

def home(request):
    return render(request,'users/home.html')

def create_user(request):
    form = create_user_form()

    context ={
        'form':form,
    }
    return render(request,"users/create_user.html",context)



def create_user_submission(request):
    try:
        log_form = login_form()
        if request.method == 'POST':
            form = create_user_form(request.POST)
            if form.is_valid():
                name = request.POST["name"]
                username=request.POST["username"]
                password= request.POST["password"]
                enc_password = pbkdf2_sha256.encrypt(password,rounds=12000,salt_size=32)

                user = People(Name=name,Username=username,Password=enc_password)
                user.save()


        return render(request,"users/login_form.html",{'form':log_form})

    except Exception as e:
            showerror(ERROR,"Username Already exists, comeup with your own")
            return render(request, "users/create_user.html", {'form': form})


def login_view(request):
    form = login_form()
    return render(request,"users/login_form.html",{'form':form})


def login_view_submission(request):

    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                user = get_object_or_404(People, Username=username)
                notfriend = People.objects.filter().exclude(Username=username)
                friend_list = Relationship.objects.filter(from_person=user)
                post_form = Post_form()
                posty = Posts.objects.all()
    
                if verify_password(user.Password,password):
                    print(f'{username} is logged in now')
                    return render(request,'users/inside_profile.html',{'user':user,'notfriend':notfriend,'friend_list':friend_list,'post_form': post_form,'post':posty})
                else:
                    raise Http404("Incorret Password")
    return login_form()


def add_friend(request,profile,friend_id):
    #print(f'{friend} has been added as friend')
    user= People.objects.get(Name=profile)
    dost = People.objects.get(id=friend_id)
    user.add_relationship(dost)
    notfriend = People.objects.filter().exclude(Name=profile)
    friend_list = Relationship.objects.filter(from_person=user)
    post_form = Post_form()
    posty = Posts.objects.all()
    return render(request,'users/inside_profile.html',{'user':user,'notfriend':notfriend,'friend_list':friend_list,'post_form':post_form,'post':posty})


def post_view(request,profile):
    user = People.objects.get(Name=profile)
    notfriend = People.objects.filter().exclude(Name=profile)
    friend_list = Relationship.objects.filter(from_person=user)
    posty = Posts.objects.all()
    if request.method == 'POST':
        post_form = Post_form(request.POST)
        if post_form.is_valid():
            post_content = request.POST['post_content']
            post_of = user
            post = Posts(post_of=post_of,content=post_content)
            post.save()
            return render(request,'users/inside_profile.html',{'user':user,'notfriend':notfriend,'friend_list':friend_list,'post_form':post_form,'post':posty})


def verify_password(password,raw_password):
        return pbkdf2_sha256.verify(raw_password,password)
