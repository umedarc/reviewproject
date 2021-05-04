from django.core.mail import send_mail
from django.http import HttpResponse

def emailfunc(request):
  send_mail(
    'Password Reset Mail',
    'Please access below URL, and reset your password.',
    'caihongline@gmail.com',
    ['yumedamail@yahoo.co.jp'],
    fail_silently=False,
  )
  return HttpResponse('')