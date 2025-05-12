#  E-commerce Admin API (FastAPI + PostgreSQL)

A modular, production-ready API built with **FastAPI** and **PostgreSQL** to power an admin dashboard for e-commerce platforms like Amazon & Walmart. It supports sales analysis, inventory tracking, and product management.

---

## Task Objectives

This project fulfills the following requirements from the task brief:

* [x] Retrieve and analyze sales data
* [x] Revenue reporting: daily, weekly, monthly, annual
* [x] Revenue comparison across timeframes and categories
* [x] Inventory tracking with stock updates and alerts
* [x] New product registration
* [x] RESTful API using FastAPI
* [x] PostgreSQL database schema
* [x] Seed script for demo data
* [x] Clear setup and database documentation

---

## Project Structure

```
E-commerce-admin-api/
├── alembic/                # DB migration versions
├── app/
│   ├── controllers/        # Business logic (CRUD)
│   ├── db/                 # DB connection & session
│   ├── models/             # SQLAlchemy ORM models (Product, Sale, Inventory, Category)
│   ├── routes/             # API route definitions
│   ├── schemas/            # Pydantic request/response schemas
│   ├── services/           # Revenue & inventory services
│   ├── utils/              # Seed scripts or helpers
│   └── __init__.py
├── main.py                 # App entry point
├── .env                    # Environment variables
├── alembic.ini             # Alembic config
├── requirements.txt        # Dependencies
└── README.md
```

---

## Setup Instructions

### 1. Environment Setup

Make sure you have **PostgreSQL**, **Python 3.9+**, and **virtualenv**.

```bash
# Clone project
git clone https://github.com/yourname/ecommerce-admin-api.git
cd ecommerce-admin-api

# Setup virtual environment
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate on Mac/Linux

# Install packages
pip install -r requirements.txt
```
### 2. Run Demo Data Seeder (Optional)

```bash
python app/utils/seed.py
```

### 3. Start the Server

```bash
uvicorn main:app --reload
```

---

## API Endpoints

### Products

| Method | Endpoint         | Description            |
| ------ | ---------------- | ---------------------- |
| POST   | `/products/`     | Register a new product |
| GET    | `/products/`     | List all products      |
| GET    | `/products/{id}` | View a product         |

### Sales

| Method | Endpoint        | Description                     |
| ------ | --------------- | ------------------------------- |
| GET    | `/sales/`       | Retrieve all sales              |
| GET    | `/sales/filter` | Filter by date/product/category |

### Revenue

| Method | Endpoint           | Description                       |
| ------ | ------------------ | --------------------------------- |
| GET    | `/revenue/summary` | View revenue by period            |
| GET    | `/revenue/compare` | Compare across periods/categories |

### Inventory

| Method | Endpoint                  | Description                 |
| ------ | ------------------------- | --------------------------- |
| GET    | `/inventory/`             | Current inventory levels    |
| PUT    | `/inventory/{product_id}` | Update inventory stock      |
| GET    | `/inventory/low-stock`    | Products with low inventory |

---

## Database Schema

### Tables

* `products`: Product info (name, SKU, category)
* `categories`: Product category (normalized)
* `sales`: Transaction data (product, quantity, date, price)
* `inventory`: Stock count per product

### Relationships

* `products.id` → `sales.product_id`
* `products.id` → `inventory.product_id`
* `categories.id` → `products.category_id`

### Normalization & Indexing

* 3NF compliant: categories and products separated
* Indexed: `product_id`, `sale_date`, `category_id`
* Designed to scale with real time analytics and inventory updates

---

## 🧪 Demo Data

Run `app/utils/seed.py` to insert:

* 10 products
* Sales spread over 12 months
* Inventory levels & low-stock edge cases

---

## 📊 API Docs

* Swagger: `http://localhost:8000/docs`
---

## ✉️ Contact

Email: [khanyamaan1@gmail.com](mailto:khanyamaan1@gmail.com)
