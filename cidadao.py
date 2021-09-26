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
  candidatos = enviar_mensagem(1, '')
  print("Lista de Candidatos:")
  for candidato in candidatos:
    print(candidato)
  voto = input("\nDigite o nome do candidato:\n")
  valido = enviar_mensagem(2, voto)
  if valido:
    print("\nVoto registrado com sucesso.")
    break
  else:
    while True:
      clear_screen()
      print("Por favor digite o nome do candidato corretamente.\n")
      voto = input("Digite o nome do candidato:\n")
      valido = enviar_mensagem(2, voto)
      if valido:
        print("\nVoto registrado com sucesso.")
        break
    break