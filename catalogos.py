import requests
import json

# Para configuração do terminal aceitar caracteres ABNT
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Definição dos parâmetros
cnpj = 2025  
ano = 2025  
sequencial = 1  

# URL base e endpoint
base_url = "https://pncp.gov.br/api"
endpoint = "/consulta/v1/catalogos"

# Construção da URL
url = f"{base_url}{endpoint}"

# Cabeçalhos da requisição
headers = {
    "Accept": "application/json"
}

# Enviando a requisição GET
response = requests.get(url, headers=headers)

# Verificando a resposta
if response.status_code == 200:
    data = response.json()  # Convertendo a resposta para JSON
    print(json.dumps(data, indent=4, ensure_ascii=False))
    
else:
    print(f"❌ Erro na requisição: {response.status_code}, {response.text}")




