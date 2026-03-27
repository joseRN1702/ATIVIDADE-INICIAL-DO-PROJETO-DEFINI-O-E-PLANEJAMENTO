import requests

def buscar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        
        if "erro" in dados:
            print("CEP não encontrado!")
        else:
            print("CEP:", dados["cep"])
            print("Rua:", dados["logradouro"])
            print("Bairro:", dados["bairro"])
            print("Cidade:", dados["localidade"])
            print("Estado:", dados["uf"])
    else:
        print("Erro na requisição!")

# Testando
cep = input("Digite o CEP: ")
buscar_cep(cep)