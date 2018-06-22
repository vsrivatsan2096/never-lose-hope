from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from models import Job, Candidates
# Create your views here.


def dashboard(request):
    return render(request, 'dash.html', {})


def civil(request):
    j = Job.objects.filter(branch="CIV")
    return render(request, 'civil.html', {'jobs': j})


def cse(request):
    j = Job.objects.filter(branch="CSE")
    return render(request, 'cse.html', {'jobs': j})


def eee(request):
    j = Job.objects.filter(branch="EEE")
    print(j)
    return render(request, 'eee.html', {'jobs': j})


def ece(request):
    j = Job.objects.filter(branch="ECE")
    return render(request, 'ece.html', {'jobs': j})


def mech(request):
    j = Job.objects.filter(branch="MEC")
    return render(request, 'mech.html', {'jobs': j})


def office(request):
    j = Job.objects.filter(branch="OFF")
    return render(request, 'office.html', {'jobs': j})


def status(request):
    try:
        c = Candidates.objects.filter(user_id=int(request.user.id))
        j = Job.objects.filter(id=c[0].job_id)
        data = {
            'title': j[0].title,
            'status': c[0].status
        }
        return render(request, 'status.html',  data)
    except:
        return render_to_response('status.html')


def support(request):
    return render_to_response('support.html')


def apply(request):
    user_id = int(request.user.id)
    job_id = int(request.GET.get("job_id", ""))
    if len(Candidates.objects.filter(user_id=request.user.id)) == 0:
        c = Candidates(user_id=user_id, job_id=job_id)
        c.save()
        return HttpResponseRedirect("/welcome/dashboard")
    else:
        return HttpResponseRedirect("/welcome/dashboard")
