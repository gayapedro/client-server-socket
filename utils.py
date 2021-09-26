import json
import os

def encode(message):
  return json.dumps(message).encode('utf-8')

def decode(message):
  return json.loads(message.decode('utf-8'))

def clear_screen():
  if os.name == 'posix':
    os.system('clear')
  else:
    os.system('cls')