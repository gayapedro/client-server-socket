#!/usr/bin/env python3

import json
import os
import socket

def transformarEmBinario(message):
  return json.dumps(message).encode('utf-8')

def recuperarMensagem(message):
  return json.loads(message.decode('utf-8'))

def limpar_tela():
  if os.name == 'posix':
    os.system('clear')
  else:
    os.system('cls')
    
def enviar_mensagem(opt, payload, HOST, PORT):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message = {'opt': opt, 'payload': payload}
    s.sendall(transformarEmBinario(message))
    data = s.recv(1024)
    return recuperarMensagem(data)