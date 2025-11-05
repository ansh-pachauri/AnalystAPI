# Django Analytics API

A Django REST Framework application that provides analytics endpoints for sales data, customer insights, and product performance.

## Setup Instructions

1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv env
```

3. Activate the virtual environment:
   - Windows:
   ```powershell
   .\env\Scripts\Activate.ps1
   ```
   - Unix/MacOS:
   ```bash
   source env/bin/activate
   ```

4. Install dependencies:
```bash
pip install django djangorestframework
```

5. Navigate to the project directory:
```bash
cd analyst
```

6. Run migrations:
```bash
python manage.py migrate
```

7. Create a superuser (for admin access):
```bash
python manage.py createsuperuser
```

8. Run the development server:
```bash
python manage.py runserver
```

## API Endpoints

### Analytics Endpoints

#### 1. Sales Summary
- **URL:** `/api/analytics/sales-summary/`
- **Method:** GET
- **Description:** Returns overall sales statistics
- **Sample Response:**
```json
{
    "total_sales": 1250.50,
    "total_customers": 25,
    "total_products_sold": 100
}
```

#### 2. Top Customers
- **URL:** `/api/analytics/top-customers/`
- **Method:** GET
- **Description:** Returns top 5 customers by spending
- **Sample Response:**
```json
[
    {
        "order__customer__id": 1,
        "order__customer__name": "John Doe",
        "total_spent": 500.00
    }
]
```

#### 3. Top Products
- **URL:** `/api/analytics/top-products/`
- **Method:** GET
- **Description:** Returns top 5 products by quantity sold
- **Sample Response:**
```json
[
    {
        "product__id": 1,
        "product__name": "Product A",
        "total_sold": 50
    }
]
```

### CRUD Endpoints

#### Customers
- List/Create: `GET/POST /api/customers/`
- Retrieve/Update/Delete: `GET/PUT/DELETE /api/customers/{id}/`

#### Products
- List/Create: `GET/POST /api/products/`
- Retrieve/Update/Delete: `GET/PUT/DELETE /api/products/{id}/`

#### Orders
- List/Create: `GET/POST /api/orders/`
- Retrieve/Update/Delete: `GET/PUT/DELETE /api/orders/{id}/`

## Postman Collection

Here are example requests you can import into Postman:

```json
{
  "info": {
    "name": "Django Analytics API",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [
    {
      "name": "Analytics",
      "item": [
        {
          "name": "Sales Summary",
          "request": {
            "method": "GET",
            "url": "http://localhost:8000/api/analytics/sales-summary/",
            "header": []
          }
        },
        {
          "name": "Top Customers",
          "request": {
            "method": "GET",
            "url": "http://localhost:8000/api/analytics/top-customers/",
            "header": []
          }
        },
        {
          "name": "Top Products",
          "request": {
            "method": "GET",
            "url": "http://localhost:8000/api/analytics/top-products/",
            "header": []
          }
        }
      ]
    },
    {
      "name": "Customers",
      "item": [
        {
          "name": "Create Customer",
          "request": {
            "method": "POST",
            "url": "http://localhost:8000/api/customers/",
            "header": [
              {
                "key": "Content-Type",
                "value": "application/json"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n    \"name\": \"John Doe\",\n    \"email\": \"john@example.com\"\n}"
            }
          }
        }
      ]
    },
    {
      "name": "Products",
      "item": [
        {
          "name": "Create Product",
          "request": {
            "method": "POST",
            "url": "http://localhost:8000/api/products/",
            "header": [
              {
                "key": "Content-Type",
                "value": "application/json"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n    \"name\": \"Product A\",\n    \"price\": 29.99\n}"
            }
          }
        }
      ]
    },
    {
      "name": "Orders",
      "item": [
        {
          "name": "Create Order",
          "request": {
            "method": "POST",
            "url": "http://localhost:8000/api/orders/",
            "header": [
              {
                "key": "Content-Type",
                "value": "application/json"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n    \"customer\": 1,\n    \"items\": [\n        {\n            \"product\": 1,\n            \"quantity\": 2\n        }\n    ]\n}"
            }
          }
        }
      ]
    }
  ]
}
```

## Testing

To run the test suite:

```bash
python manage.py test
```

To run specific tests:

```bash
python manage.py test api.tests.SalesSummaryTest
```

## Data Models

- **Customer**: Stores customer information (name, email)
- **Product**: Stores product information (name, price)
- **Order**: Represents an order made by a customer
- **OrderItem**: Represents items within an order (product, quantity)