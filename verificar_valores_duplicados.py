import json


def verificar_valores_unicos():
    try:
        with open('sorteios.json', 'r') as f:
            dados = json.load(f)

        valores = list(dados.values())
        """
        O set retorna somente valores diferentes, logo,
        se len() for igual, todos os valores sao diferentes entre si
        """
        return len(valores) == len(set(valores))
    
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")
        return False


resultado = verificar_valores_unicos()

if resultado:
    print("Todos os valores são diferentes.")
else:
    print("Há valores duplicados.")
