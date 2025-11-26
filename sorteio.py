import json
import random


with open('amigos.json', 'r') as file:
    amigos = json.load(file)


def sorteio_amigos(amigos):
    amigos_lista = list(amigos.keys())
    random.shuffle(amigos_lista)
    sorteios = {}
    amigos_sorteados = set()
    
    for pessoa in amigos_lista:
        amigos_possiveis = [amigo for amigo in amigos_lista if amigo != pessoa and amigo not in amigos_sorteados]

        if not amigos_possiveis:
            return None

        amigo_sorteado = random.choice(amigos_possiveis)
        sorteios[pessoa] = amigo_sorteado
        amigos_sorteados.add(amigo_sorteado)
    
    return sorteios


sorteios = None
while sorteios is None:
    sorteios = sorteio_amigos(amigos)

with open('sorteios.json', 'w', encoding='utf-8') as json_file:
    json.dump(sorteios, json_file, ensure_ascii=False, indent=4)

print("Sorteio concluído! Resultado salvo em sorteios.json")

