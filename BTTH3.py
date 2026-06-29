from fastapi import FastAPI

app = FastAPI(title="Hệ thống Thống kê Thư viện Nâng cao")

books = [
    {
        "id": 1,
        "title": "Python Basic",
        "author": "Nguyen Van A",
        "category": "programming",
        "year": 2022,
        "is_available": True
    },
    {
        "id": 2,
        "title": "Web API Design",
        "author": "Tran Van B",
        "category": "web",
        "year": 2021,
        "is_available": False
    },
    {
        "id": 3,
        "title": "Database System",
        "author": "Lê Minh Huyền",
        "category": "database",
        "year": 2020,
        "is_available": True
    },
    {
        "id": 4,
        "title": "Clean Code",
        "author": "Lê Ánh Linh",
        "category": "programming",
        "year": 2008,
        "is_available": False
    },
    {
        "id": 5,
        "title": "FastAPI Beginner",
        "author": "Nguyễn Văn An",
        "category": "web",
        "year": 2026,
        "is_available": True
    }
]


@app.get("/books/statistics")
def get_books_statistics():
    total_books = len(books)
    
    available_books = 0
    borrowed_books = 0
    
    for book in books:
        if book["is_available"] is True:
            available_books += 1
        else:
            borrowed_books += 1
            
    return {
        "total_books": total_books,
        "available_books": available_books,
        "borrowed_books": borrowed_books
    }


@app.get("/books/categories")
def get_books_categories():
    categories_set = set()
    for book in books:
        categories_set.add(book["category"])
        
    return {
        "categories": list(categories_set)
    }


@app.get("/books/latest")
def get_latest_book():
    if not books:
        return {
            "message": "No books available"
        }
        
    newest_book = books[0]
    for book in books:
        if book["year"] > newest_book["year"]:
            newest_book = book
            
    return newest_book