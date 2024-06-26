import requests
import json

urlDolar = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
urlEuro = 'https://economia.awesomeapi.com.br/json/last/EUR-BRL'
urlBtc = 'https://economia.awesomeapi.com.br/json/last/BTC-BRL'
urlArs = 'https://economia.awesomeapi.com.br/json/last/ARS-BRL'

cotacaoDolar = requests.get(urlDolar).content
cotacaoEuro = requests.get(urlEuro).content
cotacaoBtc = requests.get(urlBtc).content
cotacaoArs = requests.get(urlArs).content

dicDolar = json.loads(cotacaoDolar)
dicEuro = json.loads(cotacaoEuro)
dicBtc = json.loads(cotacaoBtc)
dicArs = json.loads(cotacaoArs)

valor = float(input("Digite um valor em reais: "))

conversaoDolar = valor / float(dicDolar['USDBRL']['bid'])
conversaoEuro = valor / float(dicEuro['EURBRL']['bid'])
conversaoBtc = valor / float(dicBtc['BTCBRL']['bid'])
conversaoArs = valor / float(dicArs['ARSBRL']['bid'])
print(f"R$ {valor} é {conversaoDolar} em dolar")
print(f"R$ {valor} é {conversaoEuro} em Euro")
print(f"R$ {valor} é {conversaoBtc} em Bit coin")
print(f"R$ {valor} é {conversaoArs} em peso argentino")
