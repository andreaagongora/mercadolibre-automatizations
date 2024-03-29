import requests
from src import config

def create_session():
    session = requests.Session()

    url = "https://api.mercadolibre.com/oauth/token"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "refresh_token",
        "client_id": config.client_id,
        "client_secret": config.client_secret,
        "refresh_token": config.refresh_token
    }
    r = requests.post(url, headers=headers, data=data).json()
    access_token = r['access_token']
    session.headers.update(headers)
    session.headers.update({'Authorization': f'Bearer {access_token}'})
    return session

def get_categories(site_id, session):
    res = session.get(f'https://api.mercadolibre.com/sites/{site_id}/categories').json()
    return res

def get_highlights_by_category(category_id, session):
    res = session.get(f'https://api.mercadolibre.com/highlights/MLM/category/{category_id}').json()
    return res

def get_item(item_id, session):
    res = session.get(f'https://api.mercadolibre.com/items/{item_id}').json()
    return res
