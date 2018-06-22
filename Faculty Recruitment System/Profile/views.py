from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect
from models import Profile


# Create your views here.


def create(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'create.html', c)


def save(request):
    try:
        p = Profile.objects.filter(user=request.user)[0]
        if p:
            p.delete()
    except IndexError:
        pass
    fn = request.POST.get('firstname', '')
    mn = request.POST.get('middlename', '')
    ln = request.POST.get('lastname', '')
    d1 = request.POST.get('deg1', '')
    m1 = request.POST.get('maj1', '')
    d2 = request.POST.get('deg2', '')
    m2 = request.POST.get('maj2', '')
    d3 = request.POST.get('deg3', '')
    m3 = request.POST.get('maj3', '')
    prof = request.POST.get('profession', '')
    exp = request.POST.get('experience', '')
    org = request.POST.get('organisation', '')
    p = Profile(user=request.user, first_name=fn, middle_name=mn, last_name=ln, degree1=d1, major1=m1, degree2=d2,
                major2=m2, degree3=d3, major3=m3, previous_profession=prof, previous_experience=exp, colg_cmpny_name=org)
    p.save()
    return HttpResponseRedirect('/welcome/dashboard')


def display(request):
    try:
        p = Profile.objects.filter(user=request.user)[0]
        profile = {
            'user': p.user,
            'fn': p.first_name,
            'ln': p.last_name,
            'mn': p.middle_name,
            'd1': p.degree1,
            'm1': p.major1,
            'd2': p.degree2,
            'm2': p.major2,
            'd3': p.degree3,
            'm3': p.major3,
            'prof': p.previous_profession,
            'exp': p.previous_experience,
            'org': p.colg_cmpny_name
        }
        return render(request, 'display.html', profile)
    except IndexError:
        return HttpResponseRedirect('/profile/create')


def edit(request):
    p = Profile.objects.filter(user=request.user)[0]
    profile = {
        'user': p.user,
        'fn': p.first_name,
        'ln': p.last_name,
        'mn': p.middle_name,
        'd1': p.degree1,
        'm1': p.major1,
        'd2': p.degree2,
        'm2': p.major2,
        'd3': p.degree3,
        'm3': p.major3,
        'prof': p.previous_profession,
        'exp': p.previous_experience,
        'org': p.colg_cmpny_name
    }
    return render(request, 'create.html', profile)
