from fastapi import FastAPI

app = FastAPI(title="Hệ thống Quản lý Thư viện")

books = [
    {
        "id": 1,
        "title": "Python Basic",
        "author": "Lê Minh Thư",
        "category": "programming",
        "year": 2022
    },
    {
        "id": 2,
        "title": "Web API Design",
        "author": "Phạm Lan Hồng",
        "category": "web",
        "year": 2021
    },
    {
        "id": 3,
        "title": "Database System",
        "author": "Lê Minh Huyền",
        "category": "database",
        "year": 2020
    },
    {
        "id": 4,
        "title": "Clean Code",
        "author": "Lê Ánh Linh",
        "category": "programming",
        "year": 2008
    },
    {
        "id": 5,
        "title": "FastAPI Beginner",
        "author": "Nguyễn Văn An",
        "category": "web",
        "year": 2026
    }
]

@app.get("/health")
def check_health():
    return {
        "message": "Library API is running"
    }

@app.get("/books")
def get_all_books():
    return books

# (Mở Swagger UI kiểm tra): Truy cập vào địa chỉ http://127.0.0.1:8000/docs.
