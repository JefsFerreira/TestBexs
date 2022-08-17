import ipdb
from behave import *
from httpx import post
import requests
import json

@given(u': O usuario na api de produto no metodo post')
def test_se_a_api_esta_funcionando(context):
    context.request = post(context.url)
    assert context.request.status_code == 200, 'diferente de 200'

@when(u': enviar os campos para ser cadastrados na api')
def test_cadastrar_os_produtos(context):
     feature_tabela =context.table[0]
     dados = {}
     dados['title'] = feature_tabela['title']
     dados['price'] = feature_tabela['price']
     dados['description'] = feature_tabela['description']
     dados['image'] = feature_tabela['image']
     dados['category'] = feature_tabela['category']
     context.request =post(context.url, data=dados)


@then(u': validar se todos os campo foram cadastrados')
def test_validar_se_os_campos_foram_cadastrados(context):
    tipo = context.request.json()
    assert (tipo['id']) == 21
    assert (tipo['title']) == 'iphone 12 64GB'
    assert (tipo['price']) == '5000.5'
    assert (tipo['description']) == 'Iphone 12 64GB cor preto'
    assert (tipo['image']) == 'https: //i.pravatar.cc'
    assert (tipo['category']) == 'celulares'
