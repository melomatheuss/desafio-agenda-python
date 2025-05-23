# Agenda Pessoal em Python

Este projeto é uma aplicação simples de agenda de contatos desenvolvida em Python. Permite ao usuário adicionar, editar, visualizar, favoritar e remover contatos de forma prática via terminal.

---

## Funcionalidades

- Adicionar contatos com nome, telefone e email  
- Visualizar lista completa de contatos  
- Editar dados de um contato existente  
- Marcar ou remover contatos como favoritos  
- Visualizar lista somente com os contatos favoritos  
- Apagar contatos da agenda  
- Interface de menu interativa via terminal  

---

## Como usar

1. Clone este repositório:  
   ```bash
   git clone https://github.com/melomatheuss/desafio-agenda-python
   
Navegue até a pasta do projeto:

cd seu_repositorio

Execute o script Python:

python3 agenda.py

Siga as instruções do menu para gerenciar seus contatos.

Estrutura do código

    contacts: lista que armazena os contatos, onde cada contato é um dicionário com as chaves: name, phone, email e favorite.

    Funções principais:

        add_contact: adiciona um novo contato

        show_contacts: exibe todos os contatos

        edit_contact: altera informações de um contato existente

        add_favorite: marca um contato como favorito

        remove_favorite: remove um contato dos favoritos

        show_favorites: exibe somente os contatos favoritos

        delete_contact: apaga um contato da lista
        
Requisitos

    Python 3.x

Possíveis melhorias futuras

    Validação mais robusta de entradas (ex: email válido, telefone numérico)

    Persistência dos dados em arquivo (ex: JSON ou banco de dados)

    Interface gráfica para facilitar uso

    Uso de classes para melhor organização do código (POO)
