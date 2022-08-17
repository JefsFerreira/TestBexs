  Feature: Pesquisar produtos
    @test
  Scenario: Validar o retorno de todos os produtos cadastrados na API

      Given : O usuario logado na api de produto no metodo get
       When : verificar a quantidade de produtos na api
       Then : a quantidade de produto não pode ser maior que 20 e deve conter o produto sandisk no valor de 109


