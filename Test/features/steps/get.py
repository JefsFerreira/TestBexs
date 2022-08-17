from behave import *
from httpx import get
from httpx import post
import json

@given(u': O usuario logado na api de produto no metodo get')
def test_deve_retornar_200(context):
    context.request = get(context.url)
    assert context.request.status_code == 200, 'Diferente de 200'


@when(u': verificar a quantidade de produtos na api')
def test_realizar_um_get(context):
   data = json.loads(context.request.content)
   print(data[19]['id'])

@then(u': a quantidade de produto não pode ser maior que 20 e deve conter o produto sandisk no valor de 109')
def test_verificar_a_quantidade(context):
    data = json.loads(context.request.content)
    qtdelista = len(data)
    assert qtdelista == 20
    for entry in data:
        print(entry['id'])
        print(entry['title'])
    assert (data[9]['title'] == 'SanDisk SSD PLUS 1TB Internal SSD - SATA III 6 Gb/s')
    assert (data[9]['price'] == 109)


