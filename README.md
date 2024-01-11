# Alayacare Python Skill Test - CRUD TODO

Este projeto é uma implementação do desafio da Alayacare, que consiste em criar um CRUD TODO em Python.

#### Homepage:
![Homepage](/web/img/homepage.png?raw=true "Homepage")

#### Login page:
![Login page](/web/img/login-page.png?raw=true "Login page")

#### Todos:
![Todos](/web/img/todos.png?raw=true "Todos")

## Introdução

O desafio proposto pela Alayacare envolve a criação de um aplicativo de gerenciamento de tarefas (TODO) em Python. Neste projeto, você encontrará uma implementação completa desse CRUD TODO, seguindo as diretrizes fornecidas pela empresa.

## Instruções e Tarefas

O desafio inclui várias tarefas para melhorar o código do aplicativo. Aqui estão algumas delas:

- **TASK 1**: Como usuário, não posso adicionar um TODO sem uma descrição.
- **TASK 2**: Como usuário, posso marcar um TODO como concluído.
  - Escreva um script de migração de banco de dados em `resources/`.
- **TASK 3**: Como usuário, posso visualizar um TODO em formato JSON.
  - Ex: /todo/{id}/json => {id: 1, user_id: 1, description: "Lorem Ipsum"}
- **TASK 4**: Como usuário, posso ver uma mensagem de confirmação ao adicionar/excluir um TODO.
- **TASK 5**: Como usuário, posso ver minha lista de TODOs paginada.
- **TASK 6**: Implementar uma camada de acesso ao banco de dados ORM para evitar SQL no código do controlador.

## Como Executar o Projeto

Siga os passos abaixo para executar localmente:

1. Clone este repositório.
2. Crie um ambiente virtual usando o virtualenv.
3. Instale as dependências usando `pip install -r requirements.txt`.
4. Execute o script de inicialização do banco de dados: `python main.py initdb`.
5. Inicie o aplicativo: `python main.py`.
6. Acesse a aplicação no navegador utilizando as credenciais fornecidas.

Observação: Certifique-se de ter o Python, virtualenv e sqlite3 instalados.
