# 📚 Django Gutendex API with & Swagger

This project provides a **REST API** for accessing books from the Gutenberg database with:
✔ **Django Rest Framework (DRF)**
✔ **Django Filters**
✔ **DataTables AJAX Pagination**
✔ **Swagger API Documentation**

DB Dumb also attached in this source code (Name:ignite.dump)
---

## 🚀 Features
- **Retrieve books** with pagination & filters.
- **Sortable DataTable UI** (frontend).
- **API supports:**  
  - **Filter by:** Title, Author, Language, Bookshelves, Subjects
  - **Sorting by:** Popularity (Downloads)
  - **Paginated response** (25 books per page)
- **Built-in Swagger UI** 📜 for easy API testing.

---

## 📌 Installation Steps
Create a Virtual Environment (Recommended):
-  python -m venv venv
-  source venv/bin/activate  # On Windows: venv\Scripts\activate

Required things before execute :
-  pip install django==3.2 djangorestframework==3.12 psycopg2 django-filter drf-yasg==1.20.0

Edit settings.py

Modify the DATABASES section to connect to PostgreSQL:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'gutendex',  # Change this to your actual DB name
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


### 1️⃣ Clone Repository


### 2️⃣ Install Dependencies By using requirements.txt file from root

### 3️⃣ If need Run Database Migrations


### 4️⃣ Start the Development Server


---

## 🔗 API Endpoints
| **Method** | **Endpoint**      | **Description** |
|-----------|-----------------|----------------|
| `GET`    | `/api/books/`     | Get books (pagination, search, filters) |
| `GET`    | `/books/`         | HTML Page (Restframework UI) |
| `GET`    | `/swagger/`       | API Documentation |

---

## 🎯 Example API Call (Using cURL)
    Run by using the follwing urls,
    Swagger UI → http://127.0.0.1:8000/swagger/
    Restframework UI → http://127.0.0.1:8000/books/
    API JSON Response → http://127.0.0.1:8000/api/books/?page=1
---

## 🛠 Technologies Used
- **Python version 3.6**
- **Django 3.2**
- **Django REST Framework**
- **Django Filters**
- **PostgreSQL**
- **DataTables.js**
- **Swagger UI**



---
### 📞 Need Help?
Contact me at `vijay.viswanath87@gmail.com`

