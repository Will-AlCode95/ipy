import sys
import random

numero_secreto = random.randrange(0,10)

def mostrar_numero(numero):
    print(f"listando {numero}...")

def listar():
    print("listando registros")

def ajuda():
    print("esse é o programa interface.py")

try:
  comando = sys.argv[1]
except IndexError:
  ajuda()
  sys.exit(0)

if comando == 'listar':
    listar()
elif comando == "nsecreto":
    mostrar_numero(numero_secreto)
elif comando == "ajuda":
    ajuda()
