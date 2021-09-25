#!/usr/bin/env python3

import socket
import json
import os
import sys

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = int(sys.argv[1])       # The port used by the server

def encode(message):
  return json.dumps(message).encode('utf-8')

def decode(message):
  return json.loads(message)

def clear_screen():
  if os.name == 'posix':
    os.system('clear')
  else:
    os.system('cls')

def send_socket_message(opt, payload):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message = {'opt': opt, 'payload': payload}
    s.sendall(encode(message))
    data = s.recv(1024)
    return decode(data)

while True:
  clear_screen()
  candidatos = send_socket_message(1, '')
  print("Lista de Candidatos:")
  for candidato in candidatos:
    print(candidato)
  voto = input("\nDigite o nome do candidato:\n")
  valido = send_socket_message(2, voto)
  if valido:
    print("\nVoto registrado com sucesso.")
    break
  else:
    while True:
      clear_screen()
      print("Por favor digite o nome do candidato corretamente.\n")
      voto = input("Digite o nome do candidato:\n")
      valido = send_socket_message(2, voto)
      if valido:
        print("\nVoto registrado com sucesso.")
        break
    break