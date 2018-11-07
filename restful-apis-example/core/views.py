from django.shortcuts import render
from django.conf import settings
import requests
from github import Github, GithubException
from .forms import DictionaryForm
from .models import Api
from django.http import HttpResponse
import time

def api_tipos(request):
    
    # all_apis = Api.objects.all()
    
    url1 = 'https://api.ubiplaces.com.br/is/helper/tipos'
    url2 = 'https://api.ubiplaces.com.br/is/helper/locais'
    url3 = 'https://api.ubiplaces.com.br/is/imoveis?tipo=aluguel&pagina=1&exibir=12'
    url4 = 'https://api.ubiplaces.com.br/is/imoveis?tipo=venda&pagina=1&exibir=12'
    url5 = 'https://api.ubiplaces.com.br/us/acaousuario'

    response1 = requests.get(url1)
    response2 = requests.get(url2)
    response3 = requests.get(url3)
    response4 = requests.get(url4)
    response5 = requests.get(url5)

    responses = []

    name_status1 = ''
    name_status2 = ''
    name_status3 = ''
    name_status4 = ''
    name_status5 = ''

    #response 1

    if response1.status_code == 200:
        name_status1 = 'Sucesso'

    if response1.status_code == 400:
        name_status1 = 'Requisição inválida'

    if response1.status_code == 404:
        name_status1 = 'Não encontrado'        
    
    if response1.status_code == 401:
        name_status1 = 'Não autorizado'

    if response1.status_code == 403:
        name_status1 = 'Proibido'
    
    if response1.status_code == 405:
        name_status1 = 'Método não permitido'

    #response 2
    if response2.status_code == 200:
        name_status2 = 'Sucesso'

    if response2.status_code == 400:
        name_status2 = 'Requisição inválida'

    if response2.status_code == 404:
        name_status2 = 'Não encontrado'        
    
    if response2.status_code == 401:
        name_status2 = 'Não autorizado'

    if response2.status_code == 403:
        name_status2 = 'Proibido'

    if response2.status_code == 405:
        name_status2 = 'Método não permitido'

    #response 3
    if response3.status_code == 200:
        name_status3 = 'Sucesso'

    if response3.status_code == 400:
        name_status3 = 'Requisição inválida'

    if response3.status_code == 404:
        name_status3 = 'Não encontrado'        
    
    if response3.status_code == 401:
        name_status3 = 'Não autorizado'

    if response3.status_code == 403:
        name_status3 = 'Proibido'

    if response3.status_code == 405:
        name_status3 = 'Método não permitido'

    #response 4
    if response4.status_code == 200:
        name_status4 = 'Sucesso'

    if response4.status_code == 400:
        name_status4 = 'Requisição inválida'

    if response4.status_code == 404:
        name_status4 = 'Não encontrado'        
    
    if response4.status_code == 401:
        name_status4 = 'Não autorizado'

    if response4.status_code == 403:
        name_status4 = 'Proibido'

    if response4.status_code == 405:
        name_status4 = 'Método não permitido'

    #response 5    
    if response5.status_code == 200:
        name_status5 = 'Sucesso'

    if response5.status_code == 400:
        name_status5 = 'Requisição inválida'

    if response5.status_code == 404:
        name_status5 = 'Não encontrado'        
    
    if response5.status_code == 401:
        name_status5 = 'Não autorizado'

    if response5.status_code == 403:
        name_status5 = 'Proibido'
    
    if response5.status_code == 405:
        name_status5 = 'Método não permitido'


    response1={'status': response1.status_code, 'url': url1,  'name_status': name_status1, 'time': requests.get('https://api.ubiplaces.com.br/is/helper/tipos').elapsed.total_seconds() }
    response2={'status': response2.status_code, 'url': url2,  'name_status': name_status2, 'time': requests.get('https://api.ubiplaces.com.br/is/helper/tipos').elapsed.total_seconds() }
    response3={'status': response3.status_code, 'url': url3,  'name_status': name_status3, 'time': requests.get('https://api.ubiplaces.com.br/is/helper/tipos').elapsed.total_seconds() }
    response4={'status': response4.status_code, 'url': url4,  'name_status': name_status4, 'time': requests.get('https://api.ubiplaces.com.br/is/helper/tipos').elapsed.total_seconds()  }
    response5={'status': response5.status_code, 'url': url5,  'name_status': name_status5, 'time': requests.get('https://api.ubiplaces.com.br/is/helper/tipos').elapsed.total_seconds()  }


    responses.append(response1)
    responses.append(response2)
    responses.append(response3)
    responses.append(response4)
    responses.append(response5)


    return render(request, 'core/status.html', {'all_items': responses})


def github(request):

    return render(request, 'core/home.html')

