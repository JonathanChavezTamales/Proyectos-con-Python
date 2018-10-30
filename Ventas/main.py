"""
CRUD Para ventas hecho con Python
Jonathan de Jesús Chávez Tabares
"""


clients = 'pablo,ricardo,'

def create_client(client_name):
    global clients

    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print("Client already in the list")

def list_clients():
    global clients

    print(clients)

def _add_comma():
    global clients
    clients += ','

def _get_client_name():
    return input("What is the client name? ")

def _print_welcome():
    print("CompuVentas.net")
    print(50*"*")
    print("[C]reate client")
    print("[U]pdate client")
    print("[D]elete client")

def update_client(client_name, updated_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name, updated_client_name)
    else:
        print("Client not in clients list")

if __name__ == '__main__':

    _print_welcome()
    command = input().upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()

    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input("What is the upadated client name? ")
        update_client(client_name, updated_client_name)
        list_clients()

    elif command == 'D':
        client_name = _get_client_name()
        update_client(client_name+",", '')
        list_clients()

    else:
        print("Invalid command")
