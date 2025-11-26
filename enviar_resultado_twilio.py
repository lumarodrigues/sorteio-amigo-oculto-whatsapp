import json
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

with open('sorteios.json', 'r') as file:
    sorteios = json.load(file)


client = Client(account_sid, auth_token)


for pessoa, amigo in sorteios.items():
    numero = amigos[pessoa]
    mensagem = f"Olá {pessoa}, seu amigo oculto é {amigo}!"

    try:
        message = client.messages.create(
            body=mensagem,
            from_=twilio_number,
            to=f'whatsapp:+55{numero}'
        )

        print(f"[{pessoa}] SID: {message.sid} | Status: {message.status}")
        
        # Aguarda um pouco e verifica o status atualizado
        time.sleep(3)
        updated_message = client.messages(message.sid).fetch()
        print(f"[{pessoa}] Status atualizado: {updated_message.status}")
        
        if updated_message.error_code:
            print(f"[{pessoa}] ⚠️  ERRO {updated_message.error_code}: {updated_message.error_message}")
        
    except Exception as e:
        print(f"[{pessoa}] ❌ Falha ao enviar: {e}")

    print("-" * 50)

print("\n✅ Processo finalizado!")
print("\nLegenda de status:")
print("  queued    = Na fila para envio")
print("  sent      = Enviado ao WhatsApp")
print("  delivered = Entregue ao destinatário")
print("  failed    = Falhou (verifique se a pessoa está no Sandbox)")

