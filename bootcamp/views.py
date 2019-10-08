from django.shortcuts import render,redirect
from .models import Etudiant,Encadreur,Specialite,Lieu
from django.contrib.auth.models import User
# Create your views here.


def home(request):
    data={
        'specialite':Specialite.objects.filter(status=True),
        'lieux':Lieu.objects.filter(status=True)
    }
    return render(request,'bootcamp.html',data)

def save_info(request):
    data = {}
    if request.method == 'POST':
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
    return redirect('bootcamp')