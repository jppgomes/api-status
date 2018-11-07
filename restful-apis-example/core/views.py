from django.shortcuts import render
from django.conf import settings
import requests
from .forms import DictionaryForm
from .models import Api
from django.http import HttpResponse
import time

def api_tipos(request):
    
    
    #API url's
    url_tipos = 'https://api.ubiplaces.com.br/is/helper/tipos'
    url_locais = 'https://api.ubiplaces.com.br/is/helper/locais'
    url_aluguel = 'https://api.ubiplaces.com.br/is/imoveis?tipo=aluguel&pagina=1&exibir=12'
    url_venda = 'https://api.ubiplaces.com.br/is/imoveis?tipo=venda&pagina=1&exibir=12'
    url_acao_usuario = 'https://api.ubiplaces.com.br/us/acaousuario'

    response_tipos = requests.get(url_tipos)
    response_locais = requests.get(url_locais)
    response_aluguel = requests.get(url_aluguel)
    response_venda = requests.get(url_venda)
    response_acao_usuario = requests.get(url_acao_usuario)

    responses = []

    name_status1 = ''
    name_status2 = ''
    name_status3 = ''
    name_status4 = ''
    name_status5 = ''


    #response 1
    if response_tipos.status_code == 200:
        name_status1 = 'Sucesso'

    if response_tipos.status_code == 400:
        name_status1 = 'Requisição inválida'

    if response_tipos.status_code == 404:
        name_status1 = 'Não encontrado'        
    
    if response_tipos.status_code == 401:
        name_status1 = 'Não autorizado'

    if response_tipos.status_code == 403:
        name_status1 = 'Proibido'
    
    if response_tipos.status_code == 405:
        name_status1 = 'Método não permitido'

    #response 2
    if response_locais.status_code == 200:
        name_status2 = 'Sucesso'

    if response_locais.status_code == 400:
        name_status2 = 'Requisição inválida'

    if response_locais.status_code == 404:
        name_status2 = 'Não encontrado'        
    
    if response_locais.status_code == 401:
        name_status2 = 'Não autorizado'

    if response_locais.status_code == 403:
        name_status2 = 'Proibido'

    if response_locais.status_code == 405:
        name_status2 = 'Método não permitido'

    #response 3
    if response_aluguel.status_code == 200:
        name_status3 = 'Sucesso'

    if response_aluguel.status_code == 400:
        name_status3 = 'Requisição inválida'

    if response_aluguel.status_code == 404:
        name_status3 = 'Não encontrado'        
    
    if response_aluguel.status_code == 401:
        name_status3 = 'Não autorizado'

    if response_aluguel.status_code == 403:
        name_status3 = 'Proibido'

    if response_aluguel.status_code == 405:
        name_status3 = 'Método não permitido'

    #response 4
    if response_venda.status_code == 200:
        name_status4 = 'Sucesso'

    if response_venda.status_code == 400:
        name_status4 = 'Requisição inválida'

    if response_venda.status_code == 404:
        name_status4 = 'Não encontrado'        
    
    if response_venda.status_code == 401:
        name_status4 = 'Não autorizado'

    if response_venda.status_code == 403:
        name_status4 = 'Proibido'

    if response_venda.status_code == 405:
        name_status4 = 'Método não permitido'

    #response 5    
    if response_acao_usuario.status_code == 200:
        name_status5 = 'Sucesso'

    if response_acao_usuario.status_code == 400:
        name_status5 = 'Requisição inválida'

    if response_acao_usuario.status_code == 404:
        name_status5 = 'Não encontrado'        
    
    if response_acao_usuario.status_code == 401:
        name_status5 = 'Não autorizado'

    if response_acao_usuario.status_code == 403:
        name_status5 = 'Proibido'
    
    if response_acao_usuario.status_code == 405:
        name_status5 = 'Método não permitido'


    response_tipos={'status': response_tipos.status_code, 'url': url_tipos,'name_status': name_status1, 'time': requests.get('https://api.ubiplaces.com.br/is/helper/tipos').elapsed.total_seconds() }
    response_locais={'status': response_locais.status_code, 'url': url_locais,  'name_status': name_status2, 'time': requests.get('https://api.ubiplaces.com.br/is/helper/tipos').elapsed.total_seconds() }
    response_aluguel={'status': response_aluguel.status_code, 'url': url_aluguel,  'name_status': name_status3, 'time': requests.get('https://api.ubiplaces.com.br/is/helper/tipos').elapsed.total_seconds() }
    response_venda={'status': response_venda.status_code, 'url': url_venda,  'name_status': name_status4, 'time': requests.get('https://api.ubiplaces.com.br/is/helper/tipos').elapsed.total_seconds()  }
    response_acao_usuario={'status': response_acao_usuario.status_code, 'url': url_acao_usuario,  'name_status': name_status5, 'time': requests.get('https://api.ubiplaces.com.br/is/helper/tipos').elapsed.total_seconds()  }


    responses.append(response_tipos)
    responses.append(response_locais)
    responses.append(response_aluguel)
    responses.append(response_venda)
    responses.append(response_acao_usuario)


    return render(request, 'core/status.html', {'all_items': responses})


def home(request):

    return render(request, 'core/home.html')

