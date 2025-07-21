import requests

datos = {"id":117,
        "name":"John"}



key = "F0HRZFT75QRL8N5W"

url_btc = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey={key}'
url_eth = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=ETH&to_currency=USD&apikey={key}'

try:
    response = requests.get(url_btc)
    response.raise_for_status()
    data = response.json()
    print(data)

except requests.exceptions.HTTPError as http_err:
    # Manejar errores HTTP (4xx, 5xx)
    print(f"Error HTTP: {http_err}")
except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")