import requests


def get_address_zip_code(zip_code:str):
    url = f"https://viacep.com.br/ws/{zip_code}/json/"
    return requests.get(url).json()
