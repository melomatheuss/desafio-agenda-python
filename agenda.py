contacts = []

def add_contact(contacts, name, phone, email):
    new_contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "favorite": False
    }
    contacts.append(new_contact)
    print("\nNovo contato adicionado com sucesso!")
    return

def show_contacts(contacts):
    print("Lista de contatos:")
    for i, contact in enumerate(contacts, start=1):
        favorite_marker = "♡" if contact["favorite"] else " "
        print(f"\n{i}. {contact['name']} {favorite_marker}\nTelefone: {contact['phone']}\nEmail: {contact['email']}")
    return

def edit_contact(contacts, contact_index, name, phone, email):
    index = int(contact_index) - 1
    if 0 <= index < len(contacts):
        contacts[index]["name"] = name
        contacts[index]["phone"] = phone
        contacts[index]["email"] = email
        print(f"Contato {contact_index} atualizado para\n Nome: {name}\nTelefone: {phone}\nEmail: {email}")
    else:
        print("Por favor, digite um número de contato válido.")
    return

def add_favorite(contacts, contact_index):
    index = int(contact_index) - 1
    if 0 <= index < len(contacts):
        contacts[index]["favorite"] = True
        print(f"O contato '{contacts[index]['name']}' foi adicionado aos favoritos.")
    else:
        print("Por favor, digite um número de contato válido.")
    return

def remove_favorite(contacts, contact_index):
    index = int(contact_index) - 1
    if 0 <= index < len(contacts):
        contacts[index]["favorite"] = False
        print(f"O contato '{contacts[index]['name']}' foi removido dos favoritos.")
    else:
        print("Por favor, digite um número de contato válido.")
    return

def show_favorites(contacts):
    print("\nContatos favoritos:\n")
    has_favorites = False
    for i, contact in enumerate(contacts, start=1):
        if contact.get("favorite") == True:
            print(f"{i}. {contact['name']}\nTelefone: {contact['phone']}\nEmail: {contact['email']}\n")
            has_favorites = True
    if not has_favorites:
        print("Você não possui nenhum favorito.")
    return

def delete_contact(contacts, contact_index):
    index = int(contact_index) - 1
    if 0 <= index < len(contacts):
        removed = contacts.pop(index)
        print(f"\nContato '{removed['name']}' removido com sucesso!")
    else:
        print("Por favor, digite um número de contato válido.")
    return


while True:
    print("\nSUA AGENDA PESSOAL")

    print("\n1. VISUALIZAR LISTA DE CONTATOS")
    print("2. ADICIONAR UM CONTATO")
    print("3. EDITAR UM CONTATO")
    print("4. ADICIONAR AOS FAVORITOS")
    print("5. REMOVER DOS FAVORITOS")
    print("6. VER LISTA DE FAVORITOS")
    print("7. APAGAR CONTATO")
    print("8. FECHAR AGENDA")

    choice = input("\nEscolha o número da opção desejada: ")

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= 8:
            if choice == 1:
                show_contacts(contacts)
            elif choice == 2:
                name = input("Nome do contato: ")
                phone = input("Telefone do contato: ")
                email = input("Email do contato: ")
                add_contact(contacts, name, phone, email)
            elif choice == 3:
                show_contacts(contacts)
                contact_index = input("Digite o número do contato que deseja atualizar: ")
                name = input("Novo nome do contato: ")
                phone = input("Novo telefone do contato: ")
                email = input("Novo email do contato: ")
                edit_contact(contacts, contact_index, name, phone, email)
            elif choice == 4:
                show_contacts(contacts)
                contact_index = input("Qual contato deseja adicionar aos favoritos? ♡ ")
                add_favorite(contacts, contact_index)
            elif choice == 5:
                show_contacts(contacts)
                contact_index = input("Qual contato deseja remover dos favoritos? ♡ ")
                remove_favorite(contacts, contact_index)
            elif choice == 6:
                show_favorites(contacts)
            elif choice == 7:
                show_contacts(contacts)
                contact_index = input("Qual contato deseja apagar? ")
                delete_contact(contacts, contact_index)
            elif choice == 8:
                print("Programa finalizado.")
                break
        else:
            print("\nPor favor, digite um número válido.")
    else:
        print("\nPor favor, digite apenas os números listados.")
