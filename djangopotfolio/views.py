import json
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError

from django.views.decorators.csrf import csrf_exempt
from .forms import ContactForm

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            try:
                send_mail(
                    f'Portfolio Form Submission from {name},{phone_number},{email}',
                    message,
                    email,
                    ['elvisodhiambo255@gmail.com'],
                    fail_silently=False,
                )

                return render(request, 'thank_you.html', {'name': name})
            except BadHeaderError:
                return render(request, 'failure.html', {'message': 'Invalid header found.'})
            except Exception as e:
                # Log the error message or handle it accordingly
                return render(request, 'failure.html', {'message': str(e)})
        else:
            return render(request, 'failure.html', {'message': form.errors})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def work(request):
    return render(request, 'work.html')

def otherproject(request):
    return render(request, 'otherprojects.html')
def thank_you(request):
    return render(request, 'thank_you.html')
def failure(request):
    return render(request, 'failure.html')
