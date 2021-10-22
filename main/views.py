from django.shortcuts import render, redirect
from .forms import UserForm
from .models import Users

from django.core.mail import send_mail

# Create your views here.

def index(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			return redirect('index')
	else:
		form = UserForm()
	return render(request, 'index.html', {'form' : form})

def sendmail(request):
  userlist = []
  dataset = Users.objects.all()
  for data in dataset:
    userlist.append(data.email)
  print(userlist)
  send_mail("Test Django Mail", "Hello world this is automated django mailing system", "tamalsamanta2601@gmail.com", userlist, fail_silently=False)
  return render(request, 'send.html',{})