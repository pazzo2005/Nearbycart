

import csv

def save_to_csv(data):
    """Save combined data to CSV file"""
    if not data:
        print("No data to save.")
        return

   
    fieldnames = ["id", "title", "price", "description", "category", "image", "rating_rate", "rating_count"]

    with open("combined_products.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for item in data:
            writer.writerow({
                "id": item.get("id", ""),
                "title": item.get("title", ""),
                "price": item.get("price", ""),
                "description": item.get("description", ""),
                "category": item.get("category", ""),
                "image": item.get("image", ""),
                "rating_rate": item.get("rating", {}).get("rate", ""),
                "rating_count": item.get("rating", {}).get("count", ""),
            })

    print(f"Data saved to 'combined_products.csv'")
