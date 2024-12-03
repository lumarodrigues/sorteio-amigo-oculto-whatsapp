# Sorteio de Amigo Oculto via WhatsApp
Este projeto permite realizar um sorteio de amigo oculto e enviar as mensagens automaticamente via WhatsApp utilizando a API do Twilio.

## Requisitos
Antes de rodar o projeto, é necessário configurar alguns pré-requisitos:

Criar uma conta gratuita no Twilio (é possível entrar com Google Account)
Python 3.x
Ambiente virtual (opcional, mas recomendado)

### Passo 1: Criar uma conta no Twilio

#### 1.1. Criar uma conta Twilio
Acesse o site Twilio e clique em Sign Up para criar uma conta.
Preencha os campos obrigatórios para registrar sua conta.
Após o cadastro, você será redirecionado ao painel de controle.

#### 1.2. Verificação da conta
Para validar a conta do Twilio, você precisará verificar o seu número de telefone.
No painel de controle, insira o número do telefone para o qual deseja enviar mensagens do WhatsApp (esse será o número utilizado como "remetente").

#### 1.3. Obter SID e Auth Token
Após a criação da conta, você terá acesso ao Account SID e Auth Token. Eles são fundamentais para autenticação na API do Twilio.
Acesse o painel do Twilio e anote o Account SID e o Auth Token na seção de Dashboard.

#### 1.4. Obter número de WhatsApp do Twilio
O Twilio oferece um número de WhatsApp para testes em sua conta gratuita.
Para obter o número de WhatsApp do Twilio, vá até a seção Programmable Messaging e, em seguida, Try it Out > Send a WhatsApp message.
Você receberá um número de WhatsApp associado à sua conta Twilio.

#### 1.5. Ativar o Sandbox do WhatsApp (opcional)
Para usar o WhatsApp com o Twilio, você precisa configurar o "WhatsApp Sandbox" no painel do Twilio:

Vá até a seção Messaging no painel do Twilio.
Em Sandbox, siga as instruções para enviar uma mensagem de adesão do WhatsApp para o número fornecido pelo Twilio.
Você receberá uma mensagem no WhatsApp confirmando que o número do Twilio foi ativado para uso.
Atenção: Durante o período de teste com a conta gratuita, o Twilio só permitirá o envio de mensagens para números que estejam na lista de verificados.

### Passo 2: Clonar o projeto

bash
git clone git@github.com:lumarodrigues/sorteio-amigo-oculto-whatsapp.git

### Passo 3: Preencher o arquivo amigos.json
O arquivo amigos.json deve conter como chave o nome do amigo e como valor, o telefone do mesmo. Exemplo:

{
    "Amigo 1": "21990000000",
    "Amigo 2": "21990000000",
    "Amigo 3": "21990000000",
    "Amigo 4": "21990000000",
    "Amigo 5": "21990000000",
    "Amigo 6": "21990000000",
    "Amigo 7": "21990000000",
    "Amigo 8": "21990000000",
    "Amigo 9": "21990000000"
}

Sendo os 2 primeiros números nos valores, o DDD do telefone do amigo.

### Passo 4: Criar o ambiente virtual

bash
python3 -m venv .venv

### Passo 5: Ativar o ambiente virtual

bash
source .venv/bin/activate

### Passo 6: Instalar dependências

bash
pip install -r requirements.txt

### Passo 7: Configurar as variáveis de ambiente
Criar um arquivo .env na raiz do projeto, com as seguintes variáveis:

ACCOUNT_SID=seu_account_sid_aqui
AUTH_TOKEN=seu_auth_token_aqui
TWILIO_NUMBER=whatsapp:+1415500000

Substitua seu_account_sid_aqui e seu_auth_token_aqui pelos valores obtidos no painel do Twilio.

Importante: O número whatsapp:+1415500000 é um exemplo de número de WhatsApp fornecido pelo Twilio no Sandbox.

### Passo 8: Rodar o script

bash
python script.py
