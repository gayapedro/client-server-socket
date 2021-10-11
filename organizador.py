#!/usr/bin/env python3

import sys
from utils import transformarEmBinario, recuperarMensagem, limpar_tela, enviar_mensagem

HOST = sys.argv[1]
PORT = int(sys.argv[2])

while True:
  limpar_tela()
  print("Escolha a opção:")
  print("1 - Resultado parcial")
  print("2 - Adicionar candidato")
  print("3 - Encerrar votação")
  opt = input("Opção escolhida: ")
  limpar_tela()
  if opt == '1':
    data = enviar_mensagem(3, '', HOST, PORT)
    for k, v in data.items():
      print(k, v)
    input("\nAperte qualquer tecla para continuar...")
  elif opt == '2':
    nome = input("Digite o nome do candidato: ")
    valido = enviar_mensagem(4,nome, HOST, PORT)
    if valido:
      input("\nAperte qualquer tecla para continuar...")
    else:
      print("Candidato já adicionado.")
      input("\nAperte qualquer tecla para continuar...")
  elif opt == '3':
    data = enviar_mensagem(5,'', HOST, PORT)
    print("Votação encerrada!")
    print("Resultado:\n")
    for k, v in data.items():
      print(k, v)
    break
