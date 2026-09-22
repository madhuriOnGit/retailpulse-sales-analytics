import pandas as pd
import numpy as np
from faker import Faker


# ============================================================
# INITIALIZATION
# ============================================================

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
NUM_TRANSACTIONS = 100000

START_DATE = "2024-01-01"
END_DATE = "2025-12-31"


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
    "Electronics": [
        "Mobiles",
        "Laptops",
        "Accessories",
        "Cameras"
    ],
    "Home Appliances": [
        "Refrigerators",
        "Washing Machines",
        "Microwaves",
        "Fans"
    ],
    "Furniture": [
        "Sofas",
        "Tables",
        "Chairs",
        "Beds"
    ],
    "Groceries": [
        "Beverages",
        "Snacks",
        "Staples",
        "Packaged Food"
    ],
    "Beauty": [
        "Skincare",
        "Haircare",
        "Makeup",
        "Fragrance"
    ],
    "Sports": [
        "Fitness",
        "Outdoor",
        "Cricket",
        "Football"
    ],
    "Clothing": [
        "Shirts",
        "T-Shirts",
        "Jeans",
        "Dresses"
    ],
    "Footwear": [
        "Sneakers",
        "Formal",
        "Sandals",
        "Sports Shoes"
    ],
    "Books": [
        "Fiction",
        "Non-Fiction",
        "Academic",
        "Children"
    ],
    "Toys": [
        "Educational",
        "Action Figures",
        "Puzzles",
        "Games"
    ]
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

PAYMENT_METHODS = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Cash",
    "Net Banking"
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

            "age": np.random.randint(
                18,
                70
            ),

            "city": np.random.choice(
                CITIES
            ),

            "state": np.random.choice(
                STATES
            ),

            "region": np.random.choice(
                REGIONS
            ),

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

        category = np.random.choice(
            CATEGORIES
        )

        subcategory = np.random.choice(
            SUBCATEGORIES[category]
        )

        # Different product categories have different
        # typical price ranges.

        if category == "Groceries":
            cost_price = np.random.uniform(
                20,
                1000
            )

        elif category == "Books":
            cost_price = np.random.uniform(
                100,
                2000
            )

        elif category in ["Clothing", "Footwear", "Beauty"]:
            cost_price = np.random.uniform(
                200,
                5000
            )

        elif category in ["Sports", "Toys"]:
            cost_price = np.random.uniform(
                200,
                5000
            )

        elif category == "Furniture":
            cost_price = np.random.uniform(
                2000,
                30000
            )

        else:
            cost_price = np.random.uniform(
                500,
                50000
            )

        cost_price = round(
            cost_price,
            2
        )

        selling_price = round(
            cost_price * np.random.uniform(
                1.10,
                1.80
            ),
            2
        )

        product = {
            "product_id": f"PROD{i:05d}",

            "product_name": (
                f"{fake.word().title()} "
                f"{subcategory}"
            ),

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

            "store_name": (
                f"{fake.city()} Retail Store"
            ),

            "city": np.random.choice(
                CITIES
            ),

            "state": np.random.choice(
                STATES
            ),

            "region": np.random.choice(
                REGIONS
            ),

            "store_type": np.random.choice(
                [
                    "Mall",
                    "High Street",
                    "Standalone"
                ],
                p=[
                    0.35,
                    0.40,
                    0.25
                ]
            ),

            "opening_date": opening_date
        }

        stores.append(store)

    return pd.DataFrame(stores)


# ============================================================
# 4. TRANSACTION DATA
# ============================================================

def generate_transactions(
    customers,
    products,
    stores
):

    print("\nGenerating transactions...")

    # --------------------------------------------------------
    # Create transaction dates
    # --------------------------------------------------------

    dates = pd.date_range(
        start=START_DATE,
        end=END_DATE,
        freq="D"
    )

    # --------------------------------------------------------
    # Product popularity
    #
    # Some products will naturally sell more than others.
    # --------------------------------------------------------

    product_weights = np.random.exponential(
        scale=1.0,
        size=len(products)
    )

    product_weights = (
        product_weights /
        product_weights.sum()
    )

    # --------------------------------------------------------
    # Customer purchase frequency
    #
    # Some customers will make more purchases.
    # --------------------------------------------------------

    customer_weights = np.random.exponential(
        scale=1.0,
        size=len(customers)
    )

    customer_weights = (
        customer_weights /
        customer_weights.sum()
    )

    # --------------------------------------------------------
    # Generate IDs
    # --------------------------------------------------------

    transaction_ids = [
        f"TXN{i:06d}"
        for i in range(1, NUM_TRANSACTIONS + 1)
    ]

    selected_customers = np.random.choice(
        customers["customer_id"],
        size=NUM_TRANSACTIONS,
        p=customer_weights
    )

    selected_products = np.random.choice(
        products["product_id"],
        size=NUM_TRANSACTIONS,
        p=product_weights
    )

    selected_stores = np.random.choice(
        stores["store_id"],
        size=NUM_TRANSACTIONS
    )

    selected_dates = np.random.choice(
        dates,
        size=NUM_TRANSACTIONS
    )

    # --------------------------------------------------------
    # Build transaction dataframe
    # --------------------------------------------------------

    transactions = pd.DataFrame({

        "transaction_id":
            transaction_ids,

        "transaction_date":
            selected_dates,

        "customer_id":
            selected_customers,

        "product_id":
            selected_products,

        "store_id":
            selected_stores,

        "quantity":
            np.random.choice(
                [1, 2, 3, 4, 5, 6],
                size=NUM_TRANSACTIONS,
                p=[
                    0.35,
                    0.25,
                    0.18,
                    0.10,
                    0.07,
                    0.05
                ]
            ),

        "payment_method":
            np.random.choice(
                PAYMENT_METHODS,
                size=NUM_TRANSACTIONS,
                p=[
                    0.40,
                    0.25,
                    0.15,
                    0.10,
                    0.10
                ]
            )
    })

    # --------------------------------------------------------
    # Add product pricing
    # --------------------------------------------------------

    product_prices = products[
        [
            "product_id",
            "selling_price",
            "cost_price"
        ]
    ]

    transactions = transactions.merge(
        product_prices,
        on="product_id",
        how="left"
    )

    # --------------------------------------------------------
    # Add discount
    # --------------------------------------------------------

    transactions["discount_percent"] = np.random.choice(
        [0, 5, 10, 15, 20, 25],
        size=NUM_TRANSACTIONS,
        p=[
            0.30,
            0.20,
            0.20,
            0.15,
            0.10,
            0.05
        ]
    )

    # --------------------------------------------------------
    # Calculate sales
    # --------------------------------------------------------

    transactions["gross_sales"] = (
        transactions["quantity"]
        * transactions["selling_price"]
    )

    transactions["discount_amount"] = (
        transactions["gross_sales"]
        * transactions["discount_percent"]
        / 100
    )

    transactions["net_sales"] = (
        transactions["gross_sales"]
        - transactions["discount_amount"]
    )

    # --------------------------------------------------------
    # Calculate cost and profit
    # --------------------------------------------------------

    transactions["total_cost"] = (
        transactions["quantity"]
        * transactions["cost_price"]
    )

    transactions["profit"] = (
        transactions["net_sales"]
        - transactions["total_cost"]
    )

    transactions["profit_margin"] = (
        transactions["profit"]
        / transactions["net_sales"]
        * 100
    )

    # --------------------------------------------------------
    # Round monetary columns
    # --------------------------------------------------------

    monetary_columns = [
        "selling_price",
        "cost_price",
        "gross_sales",
        "discount_amount",
        "net_sales",
        "total_cost",
        "profit",
        "profit_margin"
    ]

    transactions[monetary_columns] = (
        transactions[monetary_columns]
        .round(2)
    )

    return transactions


# ============================================================
# 5. MAIN
# ============================================================

if __name__ == "__main__":

    print("========================================")
    print("       RETAILPULSE DATA GENERATOR")
    print("========================================")

    # --------------------------------------------------------
    # Generate master datasets
    # --------------------------------------------------------

    print("\nGenerating customer data...")

    customers = generate_customers()

    print("Generating product data...")

    products = generate_products()

    print("Generating store data...")

    stores = generate_stores()

    # --------------------------------------------------------
    # Generate transactions
    # --------------------------------------------------------

    transactions = generate_transactions(
        customers,
        products,
        stores
    )

    # --------------------------------------------------------
    # Save datasets
    # --------------------------------------------------------

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

    transactions.to_csv(
        "data/raw/transactions.csv",
        index=False
    )

    # --------------------------------------------------------
    # Summary
    # --------------------------------------------------------

    print("\n========================================")
    print("       DATA GENERATION COMPLETED")
    print("========================================")

    print(
        f"\nCustomers    : {len(customers):,}"
    )

    print(
        f"Products     : {len(products):,}"
    )

    print(
        f"Stores       : {len(stores):,}"
    )

    print(
        f"Transactions : {len(transactions):,}"
    )

    print(
        "\nFiles created inside data/raw/"
    )

    print("customers.csv")
    print("products.csv")
    print("stores.csv")
    print("transactions.csv")