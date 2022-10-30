from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.contrib import auth, messages
from django.template.context_processors import csrf
from musicapp.models import Musiclover
from django.contrib.auth.models import User
#from .forms import SubscribersForm, MailMessageForm
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

# Create your views here.

def index(request):
   return render(request, 'musicapp/index.html')
   #return render(request, 'home/home.html', context)

def blog(request):
   #return render(request=request, template_name='musicapp/blog.html')
   return render(request, 'musicapp/blog.html')


def contact(request):
   return render(request, 'musicapp/contact.html')
def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {'fi_name': form.cleaned_data['fl_name'],
            'email': form.cleaned_data['email_address'],
            'message': form.cleaned_data['message_detail']}
            message_detail = "\n".join(body.values())
            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
                return redirect ("/musicapp")
                form = ContactForm()
                return render(request, 'musicapp/contact.html', {'form':form})


def elements(request):
   return render(request, 'musicapp/elements.html')

def event(request):
   return render(request, 'musicapp/event.html')

def login(request):
   #return render(request=request, template_name='musicapp/login.html')
   return render(request, 'musicapp/login.html')
def loginview(request):
    if request.method == 'POST':
        email = request.POST['lemail']
        password = request.POST['lpassword']
        #username = User.objects.get(email=str(email)).username

        try:
            user = authenticate(
            request,
            email=email,
            password=password
            )
            if user is not None:
                login(request, user)
                messages.success(request, 'You are now signed in')
                return redirect('musicapp:musicapp')
        except:
            return render(request, 'musicapp:signup')

        messages.error(request, "You dont have an account with us")
        return redirect('musicapp:signup')



def albumsstore(request):
   return render(request, 'musicapp/albums-store.html')
