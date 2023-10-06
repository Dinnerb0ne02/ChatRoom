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
import tkinter.messagebox
from tkinter.scrolledtext import ScrolledText
from threading import Thread
from datetime import datetime


class get_config_from_file:
    global lines
    with open("client.cfg", "r", encoding='utf-8') as cfg:
        lines = cfg.readlines()
        
        def get_nickname():
            nickname = lines[3].strip()[9:]
            return nickname
         
        def get_host():
            host = lines[4].strip()[5:]
            return host
    
        def get_port():
            port = lines[5].strip()[5:]
            return port
        
        def get_IP():
            IP = lines[6].strip()[3:]
            return IP
        
        def get_region():
            region = lines[7].strip()[9:]
            return region
            


class determine_language:
    def main_root_title():
        if str(get_config_from_file.get_region()) == "zh-cn":
            if str(get_config_from_file.get_IP()) == "ipv4":
                main_root_title = "聊天室 - 客户端 , 使用ipv4"
            if str(get_config_from_file.get_IP()) == "ipv6":
                main_root_title = "聊天室 - 客户端 , 使用ipv6"
            return main_root_title
        if str(get_config_from_file.get_region()) == "en-us":
            if str(get_config_from_file.get_IP()) == "ipv4":
                main_root_title = "ChatRoom - client , ipv4"
            if str(get_config_from_file.get_IP()) == "ipv6":
                main_root_title = "ChatRoom - client , ipv6"
            return main_root_title
            
    def send_button():
        if str(get_config_from_file.get_region()) == "zh-cn":
            send_button = "发送"
            return send_button
        if str(get_config_from_file.get_region()) == "en-us":
            send_button = "send"
            return send_button
    
    def ShowError_ConnectionResetError():
        if str(get_config_from_file.get_region()) == "zh-cn":
            tkinter.messagebox.showerror(title='连接重置错误',message='连接重置错误,\n服务器关闭了一个现有的连接')
        if str(get_config_from_file.get_region()) == "en-us":
            tkinter.messagebox.showerror(title='ConnectionResetError',message='ConnectionResetError,\nThe server has closed an existing connection')
            
        
    