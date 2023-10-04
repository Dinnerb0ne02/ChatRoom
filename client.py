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
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from threading import Thread
from datetime import datetime
from lib.client import get_config_from_file
from lib.client import determine_language

# Only for ipv6

def main(host, port):
    root = Tk()
    root.title(determine_language.main_root_title())
    client_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    nickname = get_config_from_file.get_nickname()
    chat_box = ScrolledText(root, state=DISABLED)  # 创建 chat_box 全局变量
    create_ui(root, client_socket, nickname, chat_box)  # 传递 chat_box 参数

    receive_thread = Thread(target=receive_messages, args=(client_socket, root, chat_box))  # 传递 chat_box 参数
    receive_thread.start()

    root.mainloop()

def create_ui(root, client_socket, nickname, chat_box):
    chat_box.pack(fill=BOTH, expand=True)

    input_frame = Frame(root)
    input_frame.pack(fill=X)

    input_entry = Entry(input_frame)
    input_entry.pack(side=LEFT, fill=BOTH, expand=True)
    input_entry.bind("<Return>", lambda event: send_message(event, input_entry, client_socket, nickname, chat_box))

    send_button = Button(input_frame, text=str(determine_language.send_button()), command=lambda: send_message(None, input_entry, client_socket, nickname, chat_box))
    send_button.pack(side=RIGHT)


def send_message(event, input_entry, client_socket, nickname, chat_box):
    message = input_entry.get()
    if message.strip():
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_message = f"{timestamp} {nickname}: {message}"
        append_message(chat_box, formatted_message)  # 使用 chat_box 变量显示消息
        client_socket.send(formatted_message.encode())
    input_entry.delete(0, END)
    
def append_message(chat_box, message):
    chat_box.config(state=NORMAL)
    chat_box.insert(END, message + "\n")
    chat_box.see(END)
    chat_box.config(state=DISABLED)

def receive_messages(client_socket, root):
    chat_box = ScrolledText(root, state=DISABLED)
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode()
            append_message(chat_box, message)
        except ConnectionResetError:
            break

        client_socket.close()



if __name__ == '__main__':
    host = str(get_config_from_file.get_host())
    port = int(get_config_from_file.get_port())
    
    main(host, port)