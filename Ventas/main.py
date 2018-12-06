"""
CRUD Para ventas hecho con Python
Jonathan de Jesús Chávez Tabares
"""
import sys
import csv
import os

CLIENT_TABLE = 'clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []


def initialize_clients_from_storage():
    """Carga los clientes de disco a memoria en 'clients'"""

    with open(CLIENT_TABLE, 'r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)
        for row in reader:
            clients.append(row)


def save_clients_to_storage():
    """Genera una tabla temporal y al final escribe en el archivo lo que se hizo en 'clients'"""

    tmp_table = f"{CLIENT_TABLE}.tmp"
    with open(tmp_table, 'w+') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
        os.rename(tmp_table, CLIENT_TABLE)


def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print("Client already in the list")


def list_clients():
    global clients
    for i, client in enumerate(clients):
        print(f"{i} | {client['name']} | {client['company']} | {client['email']}"
              + f" | {client['position']}")


def _get_client_field(field_name):
    field = None

    while not field:
        field = input(f"What is the new client's {field_name}?")
    return field


def _get_client_name():
    client = None

    while not client:
        client = input("What is the client's name? ")

        if client == 'exit':
            client = None
            break

    if not client:
        sys.exit()

    return client


def _print_welcome():
    print("CompuVentas.net")
    print(50*"*")
    print("[C]reate client")
    print("[U]pdate client")
    print("[D]elete client")
    print("[S]earch client")


def update_client(client_id, updated_client):
    global clients

    if client_id <= len(clients)-1:
        clients[client_id] = updated_client
    else:
        print("Client not in clients list")


def delete_client(client_id):
    global clients

    if client_id <= len(clients)-1:
        clients.remove(clients[client_id-1])
    else:
        print("Client not in clients list")


def search_client(client_name):
    global clients
    for client in clients:
        if client_name != client['name']:
            continue
        else:
            return True


def _get_client():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position')
    }
    return client


if __name__ == '__main__':

    initialize_clients_from_storage()
    _print_welcome()
    command = input().upper()

    if command == 'C':
        client = _get_client()
        create_client(client)
        list_clients()

    elif command == 'U':
        client_id = int(_get_client_field('id'))
        updated_client = _get_client()
        update_client(client_id, updated_client)
        list_clients()

    elif command == 'D':
        client = int(_get_client_field('id'))
        delete_client(client)
        list_clients()

    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print("El cliente sigue vivo!!")
        else:
            print("Client not found")

    else:
        print("Invalid command")

    save_clients_to_storage()
