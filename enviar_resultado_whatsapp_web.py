import json
import time
import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

with open('amigos.json', 'r') as file:
    amigos = json.load(file)

# TESTE: usando sorteios_teste.json
with open('sorteios.json', 'r') as file:
    sorteios = json.load(file)

print("=" * 50)
print("⚠️  ATENÇÃO: NÃO OLHE PARA A TELA!")
print("=" * 50)
print("\n⚠️  MODO TESTE: usando sorteios_teste.json")
print("\nO navegador vai abrir. Escaneie o QR Code do WhatsApp Web.")
print("Depois de logar, vire de costas e aperte Enter.\n")

# Abre o navegador (baixa o driver automaticamente)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://web.whatsapp.com")

input("\n✅ Logou no WhatsApp Web? Aperte Enter e VIRE DE COSTAS...")

print("\n🚀 Iniciando envio em 3 segundos...\n")
time.sleep(3)

for pessoa, amigo in sorteios.items():
    numero = amigos[pessoa]
    mensagem = f"""Olá {pessoa}! 🎄

Seu amigo oculto é...
⬇️ Role para baixo ⬇️







.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.







🎁 {amigo} 🎁







.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.







⚠️ APAGUE ESSA MENSAGEM DEPOIS DE LER!"""

    # Codifica a mensagem para URL
    mensagem_encoded = urllib.parse.quote(mensagem)
    
    # Abre o chat com a mensagem
    url = f"https://web.whatsapp.com/send?phone=55{numero}&text={mensagem_encoded}"
    driver.get(url)
    
    print(f"⏳ Aguardando carregar para {pessoa}...")
    
    try:
        # Espera o botão de enviar aparecer (até 30 segundos)
        send_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Enviar"], button[aria-label="Send"], span[data-icon="send"]'))
        )
        
        # Clica no botão de enviar
        send_button.click()
        print(f"✅ Mensagem enviada para {pessoa}")
        
    except Exception as e:
        # Se não achar o botão, tenta apertar Enter na caixa de texto
        try:
            input_box = driver.find_element(By.CSS_SELECTOR, 'div[contenteditable="true"][data-tab="10"]')
            input_box.send_keys(Keys.ENTER)
            print(f"✅ Mensagem enviada para {pessoa} (via Enter)")
        except:
            print(f"❌ Erro ao enviar para {pessoa}: {e}")
    
    time.sleep(3)

print("\n" + "=" * 50)
print("🎉 Todas as mensagens foram enviadas!")
print("=" * 50)

input("\nAperte Enter para fechar o navegador...")
driver.quit()
