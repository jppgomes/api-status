from django.shortcuts import render
from django.conf import settings
import requests
from github import Github, GithubException

from .models import Api
from django.http import HttpResponse
 
def api_tipos(request):
    
    # all_apis = Api.objects.all()
    
    url1 = 'https://api.ubiplaces.com.br/is/helper/tipos'
    url2 = 'https://api.ubiplaces.com.br/is/helper/locais'
    url3 = 'https://ubiplaces.com.br/anuncios.json'
    url4 = 'https://ubiplaces.com.br/posts.json'

    response1 = requests.get(url1)
    response2 = requests.get(url2)
    response3 = requests.get(url3)
    response4 = requests.get(url4)

    # preview1 = [200, 'https://api.ubiplaces.com.br/is/helper/tipos']
    # preview2 = [404, 'https://api.ubiplaces.com.br/is/helper/locais']
    # preview3 = [301, 'https://ubiplaces.com.br/anuncios.json']
    # preview4 = [300, 'https://ubiplaces.com.br/posts.json']



    responses = []

    response1={'status': response1.status_code, 'url': url1 }
    response2={'status': response2.status_code, 'url': url2 }
    response3={'status': response3.status_code, 'url': url3 }
    response4={'status': response4.status_code, 'url': url4 }


    responses.append(response1)
    responses.append(response2)
    responses.append(response3)
    responses.append(response4)

    # responses.append('Status: ' + str(response1.status_code) + ' Url: ' + url1)
    # responses.append('Status: ' + str(response2.status_code) + ' Url: ' + url2)
    # responses.append('Status: ' + str(response3.status_code) + ' Url: ' + url3)
    # responses.append('Status: ' + str(response4.status_code) + ' Url: ' + url4)


    return render(request, 'core/status.html', {'all_items': responses})

    # a = 'API TIPOS - STATUS: 200 OK'
    # b = 'API TIPOS - STATUS: 404 NOT FOUND'

    # c = 'API LOCAIS - STATUS: 200 OK'
    # d = 'API LOCAIS - STATUS: 404 NOTFOUND'
    



    # if response1.status_code == 200:
    #     all_apis
    #     return render(request, 'core/status.html', {'item_1': a})
    # elif response1.status_code == 404:
    #     return render(request, 'core/status.html', {'item_1': b})
    
    # elif response2.status_code == 200:
    #     return render(request, 'core/status.html', {'item_2': c})
    # elif response2.status_code == 404:
    #     return render(request, 'core/status.html', {'item_2': d})

    # if response.status_code != 200:
    #     




def home(request):
    return render(request, 'core/home.html')
