from time import sleep
from style import COLORS as c
import screenspace as ss
from screenspace import Terminal
import os
import networking
import stock_market as sm
from socket import socket

module_name = "Chat"
module_command = "chat"


def module(socket: socket, active_terminal: Terminal, pid: int, name: str):
    """
    Stocks Module
    Author: Hiral Shukla (github.com/hiralshukla)
    Author: Shan Sundal (github.com/ssundal)
    Version: 1.0 - attempting to create a chat feature

    """
    active_terminal.update("\033[0m     chats loading...", padding=False)


