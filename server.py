#!/usr/bin/env python3

import socket
import sys
from utils import transformarEmBinario, recuperarMensagem

HOST = sys.argv[1]
PORT = int(sys.argv[2])

candidatos = {'Clovis': 0, 'Pedro' : 0, 'Washington': 0}

def lista_candidatos():
  lista_candidatos = []
  for candidato in candidatos:
    lista_candidatos.append(candidato)
  return transformarEmBinario(lista_candidatos)

def votar(opt, payload):
  try:
    candidatos[payload] = candidatos[payload] + 1
    return True
  except:
    return False

def adicionar_candidato(candidato):
  if candidato in candidatos.keys():
    return False
  else:
    candidatos[candidato] = 0
    return True

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Servidor iniciado em", HOST, PORT)
    while True:
      conn, addr = s.accept()
      with conn:
          data = conn.recv(1024)
          if(data):
            message = recuperarMensagem(data)
            if message['opt'] == 1:
              print("Lista de candidatos solicitada por", addr)
              conn.sendall(lista_candidatos())
            elif message['opt'] == 2:
              valido = votar(message['opt'], message['payload'])
              if valido:
                print("Voto registrado em "+message['payload']+" por", addr)
              conn.sendall(transformarEmBinario(valido))
            elif message['opt'] == 3:
              print("Resultado parcial solicitado por", addr)
              conn.sendall(transformarEmBinario(candidatos))
            elif message['opt'] == 4:
              valido = adicionar_candidato(message['payload'])
              if valido:
                print("Candidato " + message['payload'] + " adicionado por", addr)
              conn.sendall(transformarEmBinario(valido))
            elif message['opt'] == 5:
              print("Finalização solicitada por", addr)
              conn.sendall(transformarEmBinario(candidatos))
              break
