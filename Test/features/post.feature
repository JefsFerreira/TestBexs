Feature: Enviar produtos
@test
Scenario: Validar se a api recebeu todos os campos conforme o json enviado

     Given : O usuario na api de produto no metodo post
      When : enviar os campos para ser cadastrados na api
             | title | price | description | image | category |
             | iphone 12 64GB | 5000.5 | Iphone 12 64GB cor preto | https: //i.pravatar.cc | celulares |
      Then : validar se todos os campo foram cadastrados