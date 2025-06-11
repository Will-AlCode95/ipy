#dicionario = {
#    "william" : "bill"
#}

#palavra = input("digite sua busca...")
#print(dicionario[palavra])

compras = [
    "açucar",
    "leite",
    "maça",
    "maça",
    "danoninho"
    
]

#compras.remove("leite")
print(compras)

indice_altera = compras.index("maça")
compras[indice_altera] = "uva"
print(compras)

compras.append("laranja")
print(compras)


def guardar(item):
    if len(mochila)<3:
         mochila.append(item)

mochila = []

guardar("i1")
guardar("i2")
guardar("i3")

