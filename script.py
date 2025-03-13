import json
import random
from twilio.rest import Client
import os
from dotenv import load_dotenv
import time


load_dotenv()

# Credenciais Twilio
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
twilio_number = os.getenv('TWILIO_NUMBER')


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

        with open('sorteios.json', 'w', encoding='utf-8') as json_file:
            json.dump(sorteios, json_file, ensure_ascii=False, indent=4)
    
    return sorteios


sorteios = None
while sorteios is None:
    sorteios = sorteio_amigos(amigos)


client = Client(account_sid, auth_token)


for pessoa, amigo in sorteios.items():
    numero = amigos[pessoa]
    mensagem = f"Olá {pessoa}, seu amigo oculto é {amigo}!"

    client.messages.create(
        body=mensagem,
        from_=twilio_number,
        to=f'whatsapp:+55{numero}'
    )

    time.sleep(2)

    print(f"Mensagem enviada para {pessoa} com sucesso!")

print("Sorteio concluído e mensagens enviadas automaticamente!")
