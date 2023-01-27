from django.shortcuts import render
import requests
import datetime


def Vtinterface(request):
    return render(request, 'vtinterface.html')


def callvt(request):
    current_time = datetime.datetime.now()
    time = string(current_time)

    file = request.POST.get('filescan', False)

    url = 'https://www.virustotal.com/vtapi/v2/file/scan'

    params = {'apikey': 'b8f01cc12c3d48bd487962dddb17ac585da280f2e0db6ade23d891cecb389dc5'}
    files = {'file': file}
    response = requests.post(url, files=files, params=params)

    print(response.json())
    return render(request, 'vtinterface.html')
