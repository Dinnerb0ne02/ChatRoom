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



class get_config_from_file:
    global lines
    with open("server.cfg", "r", encoding='utf-8') as cfg:
        lines = cfg.readlines()
        
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
    def main_entry_print():
        if str(get_config_from_file.get_region()) == "zh-cn":
            print("""
   _____ _           _   _____                                         
  / ____| |         | | |  __ \                                        
 | |    | |__   __ _| |_| |__) |___   ___  _ __ ___                    
 | |    | '_ \ / _` | __|  _  // _ \ / _ \| '_ ` _ \                   
 | |____| | | | (_| | |_| | \ \ (_) | (_) | | | | | |                  
  \_____|_| |_|\__,_|\__|_|  \_\___/ \___/|_| |_| |_|           v0.3.1_beta """)
            print("由d1nn3rb0ne开发，欢迎使用 聊天室 版本v0.3_beta , "+ get_config_from_file.get_IP())
            if str(get_config_from_file.get_port()) == "45001":
                print("服务器已在默认端口45001上启用")
            else:
                print("服务器已在端口" + get_config_from_file.get_port() + "上启用")
    
 
 
        if str(get_config_from_file.get_region()) == "en-us":
            
            print("""
   _____ _           _   _____                                         
  / ____| |         | | |  __ \                                        
 | |    | |__   __ _| |_| |__) |___   ___  _ __ ___                    
 | |    | '_ \ / _` | __|  _  // _ \ / _ \| '_ ` _ \                   
 | |____| | | | (_| | |_| | \ \ (_) | (_) | | | | | |                  
  \_____|_| |_|\__,_|\__|_|  \_\___/ \___/|_| |_| |_|           v0.3.1_beta """)
            print("developed by d1nn3rb0ne\nwelcome to ChatRoom-v0.3_beta, "+ get_config_from_file.get_IP())
            if str(get_config_from_file.get_port()) == "45001":
                print("The server is already enabled on the default port 45001")
            else:
                print("The server is already enabled on the port "+ get_config_from_file.get_port())
    
    def start_server_print():
        if str(get_config_from_file.get_region()) == "zh-cn":
            print("服务端已启动，等待连接...\n")
        if str(get_config_from_file.get_region()) == "en-us":
            print("The server has started, waiting for connection...\n")
        
    def handle_client_connect_print_a():
        if str(get_config_from_file.get_region()) == "zh-cn":
            handle_client_connect_print_a = "昵称为"
            return handle_client_connect_print_a
        if str(get_config_from_file.get_region()) == "en-us":
            handle_client_connect_print_a = "client with nickname"
            return handle_client_connect_print_a
    def handle_client_connect_print_b():
        if str(get_config_from_file.get_region()) == "zh-cn":
            handle_client_connect_print_b = "的客户端与"
            return handle_client_connect_print_b
        if str(get_config_from_file.get_region()) == "en-us":
            handle_client_connect_print_b = "establishes contact with"
            return handle_client_connect_print_b
    def handle_client_connect_print_c():
        if str(get_config_from_file.get_region()) == "zh-cn":
            handle_client_connect_print_c = "建立联系"
            return handle_client_connect_print_c
        if str(get_config_from_file.get_region()) == "en-us":
            handle_client_connect_print_c = ""
            return handle_client_connect_print_c
            
    def handle_client_disconnect_print_a():
        if str(get_config_from_file.get_region()) == "zh-cn":
            handle_client_disconnect_print_a = "与"
            return handle_client_disconnect_print_a
        if str(get_config_from_file.get_region()) == "en-us":
            handle_client_disconnect_print_a = "The connection to the client with nickname"
            return handle_client_disconnect_print_a
    def handle_client_disconnect_print_b():
        if str(get_config_from_file.get_region()) == "zh-cn":
            handle_client_disconnect_print_b = "的连接已断开"
            return handle_client_disconnect_print_b
        if str(get_config_from_file.get_region()) == "en-us":
            handle_client_disconnect_print_b = "has been disconnected"
            return handle_client_disconnect_print_b
            
        

