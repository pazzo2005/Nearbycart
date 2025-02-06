

import requests

FAKE_STORE_API_URL = "https://fakestoreapi.com/products"
AMAZON_API_URL = "https://api.amazon.com/products"  
FLIPKART_API_URL = "https://affiliate-api.flipkart.net/products"  

def fetch_fake_store_data():
    """Fetch data from Fake Store API"""
    response = requests.get(FAKE_STORE_API_URL)
    if response.status_code == 200:
        return response.json()  
    else:
        print("Error fetching data from Fake Store API")
        return []

def fetch_amazon_data():
    """Fetch data from Amazon API (Example)"""
    headers = {
        'Authorization': 'Bearer YOUR_AMAZON_API_KEY',  
    }
    params = {
        'category': 'electronics', 
    }
    response = requests.get(AMAZON_API_URL, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()  
    else:
        print("Error fetching data from Amazon API")
        return []

def fetch_flipkart_data():
    """Fetch data from Flipkart API (Example)"""
    headers = {
        'Authorization': 'Bearer YOUR_FLIPKART_API_KEY',  
    }
    params = {
        'category': 'electronics',  
    }
    response = requests.get(FLIPKART_API_URL, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()  
    else:
        print("Error fetching data from Flipkart API")
        return []
