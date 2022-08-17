Introdução
------------
Está é uma simples aplicação de teste baseada em [Python](https://www.python.org) para empresa BEXS BANCO/PAY.

Pré requisitos
------------
- Python 3.10

- PIP

- Virtualenv (vamos instalar com o PIP)

- Behave (vamos instalar com o PIP)

- Ipdb (vamos instalar com o PIP)

Instalação
------------
Vamos partir do pré-suposto que você ja tenha instalado o Python 3 e o PIP no seu computador.

Com o Python e o PIP instalado, execute o comando abaixo no seu terminal caso não tenha o virtualenv.

>$ pip install virtualenv 

Após instalar o virtualenv, iremos criar nosso ambiente virtual, onde iremos instalar todas as dependências do nosso 
projeto, precisamos criar um ambiente virtual.

Execute o comando abaixo na pasta raiz do seu projeto para criar o ambiente virtual, lembrando que o “env” pode ser 
substituído por qualquer nome que você escolha.

>$ virtualenv env 
 
Para ativar o ambiente, execute o comando abaixo.

Caso utilize o Windows.

>$ env\Scripts\activate 

Caso utilize o Linux/MacOS.

>$ source ./env/bin/activate 
 
Agora finalizado essa etapa vamos instalar o behave, execute o comando abaixo.

>$ pip install behave 

Também iremos utilizar o ipdb como debugger da nossa aplicação.

>$ pip install ipdb

Pronto finalizamos nossa config inicial. 

Estrutura do projeto
------------
Nosso projeto foi organizado da seguinte maneira: 

[Bexs\features\steps]()

- Bexs - Sendo a pasta principal, contendo o arquivo [behave.ini]() para a configuração de alguns parâmetros. 

- features - Subpasta da bexs, contendo o arquivo de [environment.py]() para carregar pré condições antes da execução do 
- nosso cenário.
- features - Subpasta da bexs, contendo os arquivos [feature]() responsável por conter o cenário a ser testado. 

- steps - Subpasta da Bexs, contendo os [scripts.py]() responsável por executar o código.

Execução da aplicação
----------
Para a execução desse projeto foi fornecido a [API]() [https://fakestoreapi.com/products/]() aceitando os métodos de 
POST e GET.

Podemos colocar o nosso teste em ação, esse comando abaixo ele vai executar todos os nossos cenários presentes dentro 
da features.

>(env) $ behave 

Também podemos segmentar por tags o que é permetido pela biblioteca do behave então podemos executar o comando abaixo, 
selecionando somente os cenários que possuir a tag descrita no BDD.

>$ behave --tags=@test