import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime

fake = Faker()

# Reproducibility
np.random.seed(42)
Faker.seed(42)


# ============================================================
# CONFIGURATION
# ============================================================

NUM_CUSTOMERS = 10000
NUM_PRODUCTS = 2000
NUM_STORES = 500


# ============================================================
# MASTER DATA
# ============================================================

REGIONS = [
    "North",
    "South",
    "East",
    "West",
    "Central"
]

CATEGORIES = [
    "Electronics",
    "Home Appliances",
    "Furniture",
    "Groceries",
    "Beauty",
    "Sports",
    "Clothing",
    "Footwear",
    "Books",
    "Toys"
]

SUBCATEGORIES = {
    "Electronics": ["Mobiles", "Laptops", "Accessories", "Cameras"],
    "Home Appliances": ["Refrigerators", "Washing Machines", "Microwaves", "Fans"],
    "Furniture": ["Sofas", "Tables", "Chairs", "Beds"],
    "Groceries": ["Beverages", "Snacks", "Staples", "Packaged Food"],
    "Beauty": ["Skincare", "Haircare", "Makeup", "Fragrance"],
    "Sports": ["Fitness", "Outdoor", "Cricket", "Football"],
    "Clothing": ["Shirts", "T-Shirts", "Jeans", "Dresses"],
    "Footwear": ["Sneakers", "Formal", "Sandals", "Sports Shoes"],
    "Books": ["Fiction", "Non-Fiction", "Academic", "Children"],
    "Toys": ["Educational", "Action Figures", "Puzzles", "Games"]
}

STATES = [
    "Odisha",
    "Maharashtra",
    "Karnataka",
    "Tamil Nadu",
    "West Bengal",
    "Telangana",
    "Gujarat",
    "Rajasthan",
    "Delhi",
    "Uttar Pradesh"
]

CITIES = [
    "Bhubaneswar",
    "Cuttack",
    "Mumbai",
    "Pune",
    "Bengaluru",
    "Chennai",
    "Kolkata",
    "Hyderabad",
    "Ahmedabad",
    "Jaipur",
    "Delhi",
    "Lucknow"
]


# ============================================================
# 1. CUSTOMER DATA
# ============================================================

def generate_customers():

    customers = []

    for i in range(1, NUM_CUSTOMERS + 1):

        signup_date = fake.date_between(
            start_date="-3y",
            end_date="today"
        )

        customer = {
            "customer_id": f"CUST{i:05d}",
            "customer_name": fake.name(),
            "gender": np.random.choice(
                ["Male", "Female", "Other"],
                p=[0.48, 0.48, 0.04]
            ),
            "age": np.random.randint(18, 70),
            "city": np.random.choice(CITIES),
            "state": np.random.choice(STATES),
            "region": np.random.choice(REGIONS),
            "signup_date": signup_date,
            "customer_segment": np.random.choice(
                ["Regular", "Premium", "VIP"],
                p=[0.70, 0.25, 0.05]
            )
        }

        customers.append(customer)

    return pd.DataFrame(customers)


# ============================================================
# 2. PRODUCT DATA
# ============================================================

def generate_products():

    products = []

    for i in range(1, NUM_PRODUCTS + 1):

        category = np.random.choice(CATEGORIES)

        subcategory = np.random.choice(
            SUBCATEGORIES[category]
        )

        cost_price = round(
            np.random.uniform(50, 50000),
            2
        )

        selling_price = round(
            cost_price * np.random.uniform(1.1, 1.8),
            2
        )

        product = {
            "product_id": f"PROD{i:05d}",
            "product_name": f"{fake.word().title()} {subcategory}",
            "category": category,
            "subcategory": subcategory,
            "brand": fake.company(),
            "cost_price": cost_price,
            "selling_price": selling_price
        }

        products.append(product)

    return pd.DataFrame(products)


# ============================================================
# 3. STORE DATA
# ============================================================

def generate_stores():

    stores = []

    for i in range(1, NUM_STORES + 1):

        opening_date = fake.date_between(
            start_date="-8y",
            end_date="-6m"
        )

        store = {
            "store_id": f"STORE{i:04d}",
            "store_name": f"{fake.city()} Retail Store",
            "city": np.random.choice(CITIES),
            "state": np.random.choice(STATES),
            "region": np.random.choice(REGIONS),
            "store_type": np.random.choice(
                ["Mall", "High Street", "Standalone"],
                p=[0.35, 0.40, 0.25]
            ),
            "opening_date": opening_date
        }

        stores.append(store)

    return pd.DataFrame(stores)


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    print("Generating customer data...")
    customers = generate_customers()

    print("Generating product data...")
    products = generate_products()

    print("Generating store data...")
    stores = generate_stores()

    # Save raw data
    customers.to_csv(
        "data/raw/customers.csv",
        index=False
    )

    products.to_csv(
        "data/raw/products.csv",
        index=False
    )

    stores.to_csv(
        "data/raw/stores.csv",
        index=False
    )

    print("\nData generation completed!")

    print(f"Customers: {len(customers):,}")
    print(f"Products: {len(products):,}")
    print(f"Stores: {len(stores):,}")