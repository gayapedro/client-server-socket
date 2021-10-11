#!/usr/bin/env python3

import sys
from utils import transformarEmBinario, recuperarMensagem, limpar_tela, enviar_mensagem

HOST = sys.argv[1]
PORT = int(sys.argv[2])

while True:
  limpar_tela()
  candidatos = enviar_mensagem(1, '', HOST, PORT)
  print("Lista de Candidatos:")
  for candidato in candidatos:
    print(candidato)
  voto = input("\nDigite o nome do candidato:\n")
  valido = enviar_mensagem(2, voto, HOST, PORT)
  if valido:
    print("\nVoto registrado com sucesso.")
    break
  else:
    while True:
      limpar_tela()
      print("Por favor digite o nome do candidato corretamente.\n")
      voto = input("Digite o nome do candidato:\n")
      valido = enviar_mensagem(2, voto, HOST, PORT)
      if valido:
        print("\nVoto registrado com sucesso.")
        break
    break
    