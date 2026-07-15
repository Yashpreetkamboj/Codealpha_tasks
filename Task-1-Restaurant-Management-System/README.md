# Restaurant Management System

A simple backend project built with Django and Django REST Framework for managing restaurant operations.

## Features

- Manage menu items
- Manage restaurant tables
- Place customer orders
- Reserve tables with availability checking
- Manage inventory
- Automatically reduce inventory when an order is placed
- Django admin panel

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite

## API Endpoints

- `/api/menu/` - View and manage menu items
- `/api/tables/` - View and manage tables
- `/api/orders/` - Place and view orders
- `/api/reservations/` - Create and view reservations
- `/api/inventory/` - View and update inventory
- `/admin/` - Django admin panel

## How to Run

1. Clone the repository.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Run the server:

```bash
python manage.py runserver
```

5. Open `http://127.0.0.1:8000/api/menu/` in your browser.

## Admin Panel

Create an admin account:

```bash
python manage.py createsuperuser
```

Then visit `http://127.0.0.1:8000/admin/`.

## Author

Yash Kamboj
