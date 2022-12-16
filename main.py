import requests
import json

cotacoes = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
dolar = cotacoes['USDBRL']['bid']
print("dolar today: " + dolar)
