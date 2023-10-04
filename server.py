'''
    ChatRoom - develop by D1nn3rb0ne, is able to open a private server chat software
    Copyright (C) 2023  d1nn3rb0ne (D1nn3rb0ne)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.    
    The Auther's email: tomma_2022@outlook.coms

'''


import socket
import threading
from datetime import datetime
from lib.server import get_config_from_file
from lib.server import determine_language

def handle_client(client_socket, client_address, clients):
    nickname = client_socket.recv(1024).decode()
    print(str(determine_language.handle_client_connect_print_a()) + f" {nickname} " + str(determine_language.handle_client_connect_print_b()) + f" {client_address} " + str(determine_language.handle_client_connect_print_c()))

    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode()
            broadcast_message = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {nickname}: {message}"
            print(broadcast_message)
            broadcast_message_to_all(clients, broadcast_message)
        except ConnectionResetError:
            break

    client_socket.close()
    print(str(determine_language.handle_client_disconnect_print_a()) + f" {client_address} " +str(determine_language.handle_client_disconnect_print_b()))

def broadcast_message_to_all(clients, message):
    for client in clients:
        client_socket = client[0]
        client_socket.send(message.encode())

def start_server():
    host = str(get_config_from_file.get_host())
    port = int(get_config_from_file.get_port())
    
    server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    determine_language.start_server_print()

    clients = []

    while True:
        client_socket, client_address = server_socket.accept()
        clients.append((client_socket, client_address))
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address, clients))
        client_thread.start()

determine_language.main_entry_print()
start_server()