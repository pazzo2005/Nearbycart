

from api_fetch import fetch_fake_store_data, fetch_amazon_data, fetch_flipkart_data

def combine_data():
    """Combine data from multiple APIs"""
    fake_store_data = fetch_fake_store_data()
    amazon_data = fetch_amazon_data()
    flipkart_data = fetch_flipkart_data()

    
    combined_data = fake_store_data + amazon_data + flipkart_data
    
    return combined_data
