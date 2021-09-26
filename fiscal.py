#!/usr/bin/env python3

import socket
import sys
from utils import encode, decode, clear_screen

HOST = sys.argv[1]
PORT = int(sys.argv[2])

def enviar_mensagem(opt, payload):
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
    data = enviar_mensagem(3, '')
    for k, v in data.items():
      print(k, v)
    input("\nAperte qualquer tecla para continuar...")
  elif opt == '2':
    nome = input("Digite o nome do candidato: ")
    valido = enviar_mensagem(4,nome)
    if valido:
      input("\nAperte qualquer tecla para continuar...")
    else:
      print("Candidato já adicionado.")
      input("\nAperte qualquer tecla para continuar...")
  elif opt == '3':
    data = enviar_mensagem(5,'')
    print("Votação encerrada!")
    print("Resultado:\n")
    for k, v in data.items():
      print(k, v)
    break
