from dotenv import load_dotenv
import os
import requests

datos = {"id":117,
        "name":"John"}

load_dotenv()

alpha_vantage_key = os.getenv("API_KEY_ALPHA_VANTAGE")


ASSETS = {"BTC":{"name":"Bitcoin (N/A)","price":"N.A."},
          "ETH":{"name":"Ethereum (N/A)","price":"N.A."}
          }


def fetch_asset_data(from_currency):
    """Obtiene nombre y precio de un activo desde la API"""
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency=USD&apikey={alpha_vantage_key}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        exchange_data = data['Realtime Currency Exchange Rate']
        # Devolver un diccionario cuyas key sean correspondientes a las key de los diccionarios
        # contenidos en las key del diccionario ASSETS
        return {
            "name": exchange_data['2. From_Currency Name'],
            "price": f"{float(exchange_data['5. Exchange Rate']):,.2f}"
        }

    except Exception as e:
        print(f"Error al obtener {from_currency}: {str(e)}")
        return None


def update_assets():
    """ Actualizacion de la informacion contenida en el diccionario ASSETS """
    # Por cada key del diccionario ASSETS se llama a la función fetch
    for asset in ASSETS:
        new_data = fetch_asset_data(asset)
        # Luego de obtener el return de la función fetch
        # se asigna los valores correspondientes a las key name y price del diccionario ASSET
        if new_data:
            ASSETS[asset].update(new_data)


# update_assets()
# print(ASSETS)