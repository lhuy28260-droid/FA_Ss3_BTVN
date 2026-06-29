
from fastapi import FastAPI

app = FastAPI(title="Hệ thống Quản lý Thư viện - Phân loại trạng thái")

books = [
    {"id": 1, "title": "Python Basic", "author": "Nguyen Van A", "category": "programming", "year": 2022, "is_available": True},
    {"id": 2, "title": "Web API Design", "author": "Tran Van B", "category": "web", "year": 2021, "is_available": False},
    {"id": 3, "title": "Database System", "author": "Lê Minh Huyền", "category": "database", "year": 2020, "is_available": True},
    {"id": 4, "title": "Clean Code", "author": "Lê Ánh Linh", "category": "programming", "year": 2008, "is_available": False},
    {"id": 5, "title": "FastAPI Beginner", "author": "Nguyễn Văn An", "category": "web", "year": 2026, "is_available": True}
]

@app.get("/books/available")
def get_available_books():
    result = []
    
    for book in books:
        if book["is_available"] is True:
            result.append(book)
            
    return result


@app.get("/books/borrowed")
def get_borrowed_books():
    result = []
    
    for book in books:
        if book["is_available"] is False:
            result.append(book)
            
    return result