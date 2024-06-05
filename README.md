# LP3 331

## Repositório para organizar os códigos da diciplina de Linguagem de Programação 3
-----------------------

## Instruções Lab de Informática

### Ao chegar no laboratório:

- Configurar o usuário local do git

``` bash
    git config --global user.name "Seu nome"
    git config --global user.email "seuemail@email.com"
```

- Fazer o clone do seu repositório no GitHub


``` bash
    git clone https://github.com/seu-usuario/lp3-331.git
```

- Abrir o repositório no VSCode


``` bash
    code lp3-331
```

## Criar um token para realizar os pushs

### Settings  > Developer Settings

<br>
<img width=600px src="https://raw.githubusercontent.com/wiki/kai-tub/external-repo-sync-action/gifs/create_token_short.gif" alt="Token Gif">
<br>
<br>


## Antes de sair do Laboratóro

- Remover as condigurações de usuário

``` bash
    git config --global --unset user.name
    git config --global --unset user.email
```

- Deletar o token no GitHub

- Deslogar do GitHub

### Instalar Flask

- Instalação

``` bash
    curl -sSL https://install.python-poetry.org | python3 -
```

- Adicionar ao Path


``` bash
    export PATH="/home/estudante1/.local/bin:$PATH"
```

- Criar projeto Flask


``` bash
    poetry new meu_projeto
```

- Comandos do projeto flask


``` bash
    poetry shell
```
Ctrl + Shift + P

Select Interpreter

Selecionar o ambiente virtual

- Adicionar Flask ao projeto

```bash
    poetry add Flask
```
```bash
    flask --app meu_projeto/app.py run
    poetry run flask --app meu_projeto/app.py run
```