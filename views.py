from django.shortcuts import render

def homepage(request):
    return render(request, 'roadshow/homepage.html')

def pilot(request):
    return render(request, 'roadshow/pilot.html')

def costs(request):
    return render(request, 'roadshow/costs.html')

def benefits(request):
    return render(request, 'roadshow/benefits.html')

def target(request):
    return render(request, 'roadshow/target.html')

def entry(request):
    return render(request, 'roadshow/entry.html')

def television(request):
    return render(request, 'roadshow/television.html')

def pdf(request):
    return render(request, 'roadshow/pdf.html')

def contact(request):
    return render(request, 'roadshow/contact.html')

def preproduction(request):
    return render(request, 'roadshow/preproduction.html')

def production(request):
    return render(request, 'roadshow/production.html')

def postproduction(request):
    return render(request, 'roadshow/postproduction.html')

def whatisit(request):
    return render(request, 'roadshow/whatisit.html')

def howdoijoin(request):
    return render(request, 'roadshow/howdoijoin.html')

def whataretherules(request):
    return render(request, 'roadshow/whataretherules.html')

def whocanjoin(request):
    return render(request, 'roadshow/whocanjoin.html')

def whowinswhat(request):
    return render(request, 'roadshow/whowinswhat.html')

def schedule(request):
    return render(request, 'roadshow/schedule.html')
