import requests
import json
"""
import time # для выполнения бесконечного цикла
"""

def mining():
    data = requests.get("https://blockchain.info/ru/ticker").text
    json_string = json.dumps(data)
    return json_string


"""
# результаты запроса
dictionary = json.loads(mining())
print("ALL DATA", dictionary)
"""
"""
# результаты запроса только с валютой RUB
dictionary = json.loads(mining())
dictionary_sub = json.loads(dictionary)
print("RUB", dictionary_sub.get('RUB'))
"""
"""
# выполнение бесконечного цикла запросов только с валютой RUB
while True:
    dictionary = json.loads(mining())
    dictionary_sub = json.loads(dictionary)
    print("RUB", dictionary_sub.get('RUB'))
    time.sleep(5)
"""
"""
# выбор валюты пользователем и вывод данных о биткоине
while True:
    print("Выберете валюту:")
    choice = input().upper()
    dictionary = json.loads(mining())
    dictionary_sub = json.loads(dictionary)
    print(choice, dictionary_sub.get(choice))
"""
"""
# выбор валюты пользователем и вывод цены покупки биткоина
while True:
    print("Выберете валюту:")
    choice = input().upper()
    dictionary = json.loads(mining())
    dictionary_sub = json.loads(dictionary)
    dictionary_currency = dictionary_sub.get(choice)
    print(choice, "Price:", dictionary_currency.get('buy'))
"""