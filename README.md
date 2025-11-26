# Sorteio de Amigo Oculto via WhatsApp

Este projeto permite realizar um sorteio de amigo oculto e enviar as mensagens automaticamente via WhatsApp.

## Métodos de Envio

O projeto oferece **duas formas** de enviar os resultados:

| Método | Vantagens | Desvantagens |
|--------|-----------|--------------|
| **WhatsApp Web** (recomendado) | Simples, sem cadastro, sem limites | Organizador não pode olhar a tela durante envio |
| **Twilio API** | Totalmente automático | Requer conta Twilio, limite de 24h, configuração complexa |

---

## Método 1: WhatsApp Web (Recomendado)

Este método usa o navegador do organizador para enviar as mensagens automaticamente pelo WhatsApp Web.

### Requisitos
- Python 3.x
- Google Chrome instalado
- Conta no WhatsApp

### Passo 1: Clonar o projeto

```bash
git clone git@github.com:lumarodrigues/sorteio-amigo-oculto-whatsapp.git
cd sorteio-amigo-oculto-whatsapp
```

### Passo 2: Preencher o arquivo amigos.json

O arquivo `amigos.json` deve conter como chave o nome do amigo e como valor, o telefone (DDD + número):

```json
{
    "Amigo 1": "21990000000",
    "Amigo 2": "21990000000",
    "Amigo 3": "21990000000"
}
```

### Passo 3: Criar e ativar o ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Passo 4: Instalar dependências

```bash
pip install -r requirements.txt
```

### Passo 5: Realizar o sorteio

```bash
python sorteio.py
```

Este comando gera o arquivo `sorteios.json` com o resultado do sorteio.

### Passo 6: Enviar os resultados via WhatsApp Web

```bash
python enviar_whatsapp_web.py
```

**Como funciona:**

1. O navegador Chrome abre automaticamente
2. Escaneie o QR Code do WhatsApp Web com seu celular
3. Após logar, aperte Enter no terminal
4. **VIRE DE COSTAS** - o script vai enviar as mensagens automaticamente
5. Aguarde até o script finalizar (você verá a mensagem no terminal)

> ⚠️ **Importante:** Como organizador, você NÃO deve olhar para a tela durante o envio, pois as mensagens com os resultados aparecerão na tela. A mensagem enviada possui espaçamento para que o nome do amigo secreto não apareça na pré-visualização do WhatsApp.

---

## Método 2: Twilio API (Alternativo)

Este método usa a API do Twilio para enviar mensagens via WhatsApp de forma totalmente automática.

### Requisitos
- Conta gratuita no [Twilio](https://www.twilio.com)
- Python 3.x
- Todos os participantes devem aderir ao Sandbox do Twilio

### Limitações do Twilio (conta gratuita)
- Janela de 24 horas: participantes precisam enviar mensagem ao Twilio no mesmo dia
- Limite de 50 mensagens por dia
- Todos precisam escanear QR Code do Sandbox

### Configuração do Twilio

#### 1. Criar conta e obter credenciais
1. Acesse [Twilio](https://www.twilio.com) e crie uma conta
2. No painel, anote o **Account SID** e **Auth Token**
3. Vá em **Messaging > Try it Out > Send a WhatsApp message**
4. Obtenha o número do WhatsApp Sandbox

#### 2. Configurar Sandbox
1. Vá em **Messaging > Sandbox**
2. Cada participante deve enviar a mensagem de adesão (ex: `join codigo`) para o número do Twilio
3. Isso deve ser feito **no mesmo dia** do envio das mensagens

#### 3. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```bash
ACCOUNT_SID=seu_account_sid_aqui
AUTH_TOKEN=seu_auth_token_aqui
TWILIO_NUMBER=whatsapp:+14155238886
```

#### 4. Realizar o sorteio

```bash
python sorteio.py
```

#### 5. Enviar os resultados

```bash
python enviar_resultado_twilio.py
```

O script mostrará o status de cada mensagem (queued, sent, delivered, failed).

---

## Estrutura dos Scripts

| Script | Descrição |
|--------|-----------|
| `sorteio.py` | Realiza o sorteio e salva em `sorteios.json` |
| `enviar_whatsapp_web.py` | Envia resultados via WhatsApp Web (Chrome) |
| `enviar_resultado_twilio.py` | Envia resultados via Twilio API |

---

## Dicas

- **Teste antes:** Crie um `sorteios_teste.json` com uns 2 participantes para testar o envio
- **Backup:** O sorteio fica salvo em `sorteios.json`, então se o envio falhar, não precisa sortear novamente
- **Privacidade:** As mensagens têm espaçamento para esconder o nome do amigo secreto na pré-visualização
