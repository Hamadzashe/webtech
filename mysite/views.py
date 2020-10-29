from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.
def home(request):
     if request.method == "POST":
          client= request.POST['client']
          message_number = request.POST['message-number']
          message_email = request.POST['message-email']
          message = request.POST['message']

          #send an email
          send_mail(
               client, # subject
               message, # message
               message_email, # from email
               ['webtechnologygo@gmail.com'], # to email
          )

          return render(request, 'mysite/home.html', {'client': client})
     else:
          return render(request, 'mysite/home.html')   