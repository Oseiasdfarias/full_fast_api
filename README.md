<p align=center> 
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/> 
<img src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white"/> 
<img src="https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white"/> 
<img src="https://img.shields.io/badge/pytest-3670A0?style=for-the-badge&logo=pytest&logoColor=ffdd54"/> 
<img src="https://img.shields.io/badge/pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white"/>
<img src="https://img.shields.io/badge/sqlalchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white"/>
<img src="https://img.shields.io/badge/ruff-D7FF64?style=for-the-badge&logo=ruff&logoColor=261230"/>
<img src="https://img.shields.io/badge/taipy-FF371A?style=for-the-badge&logo=taipy&logoColor=white"/>
<img src="https://img.shields.io/badge/httpie-73DC8C?style=for-the-badge&logo=httpie&logoColor=black"/>
</p>

<p align="center">
  <img height="140px" src="./utils/fast_api_logo.png">
</p>


<h3>Sumário</h3>


<p id="roadmap"> 
  <ul>
    <li> <a href="#id1">  Visão Geral</a> </li>
    <li> <a href="#id2"> Configuração do Ambiente</a> </li>
    <li> <a href="#id3"> Instalando as dependências do Projeto</a> </li>
    <li> <a href="#id4"> Rodando Códigos</a> </li>
  </ul>
</p>

# Fast API


<h3 id="id1">Visão Geral</h3>

API desenvolvida no curso ministrado pelo canal [Live de Python](https://www.youtube.com/@Dunossauro) ...



---


<h3>Requisitos do projeto</h3>


<ul>
    <li> <a href="#techs">Python 11+</a></li>
    <li> <a href="#id1">  Poetry ou pip</a> </li>
    <li> <a href="#id2"> FastAPI</a> </li>
  </ul>



<h2 id="id2">Configuração do Ambiente</h2>

Recomendo que use o [pyenv](https://github.com/pyenv/pyenv) para instalar a versão `3.12.3` do Python.

caso não tenha o `pyenv`  instalado em sua máquina, você pode instala-lo usando o [pipx](https://github.com/pypa/pipx), após instalar o `pipx` basta rodar o seguinte comando.

```bash
❯ pipx install pyenv
```

Agora com o `pyenv` instalado, basta roda o seguinte comando para instalar a versão `3.12.3` do Python.

```bash
❯ pyenv install 3.12.3
```

para definir a versão do python em seu projeto, você deve acessar pelo terminal o caminho do seu projeto e roda o comando abaixo em seu terminal.


```bash
❯ pyenv local 3.12.3 
```

pronto, agora você tem o `Python 3.12.3` definido para  seu projeto.


<h3 id="id3">Instalando as dependências do Projeto</h3>

Para instalar as dependências usando o `poetry` basta executar o seguinte comando em seu terminal dentro da pasta raiz do projeto:

```bash
❯ poetry install
```

Caso queira instalar usando o `pip`, use o comando abaixo:

```bash
❯ pip install -r requirements.txt
```

> [!WARNING]
> Certifique-se que seu ambiente esteja ativado.


---


<h2 id="id4">Rodando Códigos</h2>

Para executar os códigos, utilizaremos o `taskipy`, uma biblioteca em `Python` que facilita a criação de comandos para a execução de diversas ações.


<h3 id="id5">Rodando os Testes</h3>

Para rodar os testes basta executar o seguinte comando com o ambiente virtual ativado:


```bash
❯ task test
```


Saída:

```bash
All checks passed!
==================================================== test session starts =====================================================
platform linux -- Python 3.12.3, pytest-8.2.2, pluggy-1.5.0 -- /home/osfarias/workspace/workspace_python/fast_api/.venv/bin/python
cachedir: .pytest_cache
rootdir: /home/osfarias/workspace/workspace_python/fast_api
configfile: pyproject.toml
plugins: anyio-4.4.0, cov-5.0.0
collected 5 items

tests/test_app.py::test_read_root_deve_retornar_ok_e_ola_mundo PASSED                                                  [ 20%]
tests/test_app.py::test_create_user PASSED                                                                             [ 40%]
tests/test_app.py::test_read_users PASSED                                                                              [ 60%]
tests/test_app.py::test_update_user PASSED                                                                             [ 80%]
tests/test_app.py::test_delete_user PASSED                                                                             [100%]
```


<h3 id="id6">Rodando a API</h3>

 
```bash
❯ task run
```


Saída:

<p align="center">
  <img wigth="90%" src="./utils/run_api.png">
</p>


Acesando a documentação da API

A página `localhost/docs` do FastAPI é uma interface gerada automaticamente pela biblioteca que fornece uma documentação interativa para sua API. Baseada no Swagger UI, esta página permite que desenvolvedores visualizem e testem todas as rotas e endpoints da API diretamente no navegador. Cada endpoint é detalhado com informações sobre métodos HTTP suportados, parâmetros de entrada, respostas possíveis e modelos de dados. A funcionalidade interativa permite enviar requisições e visualizar as respostas, facilitando a verificação e o debugging da API durante o desenvolvimento. Essa documentação dinâmica é uma ferramenta poderosa para garantir que a API esteja funcionando conforme o esperado e para melhorar a produtividade dos desenvolvedores.



<p align="center">
  <img wigth="90%" src="./utils/docs_api.png">
</p>
