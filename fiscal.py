#!/usr/bin/env python3

import socket
import json
import os
import sys

HOST = '127.0.0.1'
PORT = int(sys.argv[1])

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
  print("Escolha a opção:")
  print("1 - Resultado parcial")
  print("2 - Adicionar candidato")
  print("3 - Encerrar votação")
  opt = input("Opção escolhida: ")
  clear_screen()
  if opt == '1':
    data = send_socket_message(3, '')
    for k, v in data.items():
      print(k, v)
    input("\nAperte qualquer tecla para continuar...")
  elif opt == '2':
    nome = input("Digite o nome do candidato: ")
    valido = send_socket_message(4,nome)
    if valido:
      input("\nAperte qualquer tecla para continuar...")
    else:
      print("Candidato já adicionado.")
      input("\nAperte qualquer tecla para continuar...")
  elif opt == '3':
    data = send_socket_message(5,'')
    print("Votação encerrada!")
    print("Resultado:\n")
    for k, v in data.items():
      print(k, v)
    break
