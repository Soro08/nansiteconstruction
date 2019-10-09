from django.shortcuts import render,redirect
from .models import Etudiant,Encadreur,Specialite,Lieu
from django.contrib.auth.models import User
# Create your views here.


def home(request):
    
    is_error = False
    is_success = False
    if request.method == 'POST':
        try:
            lieu=Lieu.objects.get(pk=request.POST.get('lieu'))
            specialite = Specialite.objects.get(pk=request.POST.get('specialite'))
            print('======================================\r\n',request.POST,lieu,specialite,'\r\n==============================')
            username = request.POST.get('first_name')+' '+request.POST.get('last_name')
            if request.POST.get('first_name') is not None and request.POST.get('last_name') is not None and request.POST.get('contact') is not None:

                user = User(username =username, first_name = request.POST.get('first_name'), last_name = request.POST.get('last_name'), email = request.POST.get('email'))
                user.save()
                user.etudiant.contact=request.POST.get('contact')
                user.etudiant.lieu = lieu
                user.etudiant.specialite =  specialite
                user.save()
                is_success = True
            else:
                is_error = True
        except:
            is_error = True

        
    data={
        'specialite':Specialite.objects.filter(status=True),
        'lieux':Lieu.objects.filter(status=True),
        'is_succes':is_success,
        'is_error': is_error,
    }
    return render(request,'bootcamp.html',data)

def save_info(request):
    data = {}
    is_error = False
    is_success = False
    if request.method == 'POST':
        try:

            lieu=Lieu.objects.get(pk=request.POST.get('lieu'))
            specialite = Specialite.objects.get(pk=request.POST.get('specialite'))
            print('======================================\r\n',request.POST,lieu,specialite,'\r\n==============================')
            username = request.POST.get('first_name')+' '+request.POST.get('last_name')
            user = User(username =username, first_name = request.POST.get('first_name'), last_name = request.POST.get('last_name'), email = request.POST.get('email'))
            user.save()
            user.etudiant.contact=request.POST.get('contact')
            user.etudiant.lieu = lieu
            user.etudiant.specialite =  specialite
            user.save()
            is_success = True
        except:
            print('error')
            is_error = True
    return redirect('bootcamp')