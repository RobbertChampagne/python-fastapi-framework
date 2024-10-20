# python FastAPI/main.py
from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, create_engine, Session, select
from sqlalchemy.sql import text
from models import Author, Book

app = FastAPI()

# SQLite setup
DATABASE_URL = "sqlite:///./orm.db"
engine = create_engine(DATABASE_URL)

# Function to execute raw SQL query
def get_item_by_id_raw_sql(item_id: int):
    with Session(engine) as session:
        result = session.execute(text(f"SELECT * FROM book WHERE id = {item_id}"))
        item = result.fetchone()
        return item


'''
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    with Session(engine) as session:
        session.add(item)
        session.commit()
        session.refresh(item)
        return item

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    with Session(engine) as session:
        item = session.exec(select(Item).where(Item.id == item_id)).first()
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return item

@app.get("/items/", response_model=list[Item])
def read_items():
    with Session(engine) as session:
        items = session.exec(select(Item)).all()
        return items

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    with Session(engine) as session:
        db_item = session.exec(select(Item).where(Item.id == item_id)).first()
        if db_item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        db_item.name = item.name
        db_item.description = item.description
        session.add(db_item)
        session.commit()
        session.refresh(db_item)
        return db_item

@app.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int):
    with Session(engine) as session:
        item = session.exec(select(Item).where(Item.id == item_id)).first()
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        session.delete(item)
        session.commit()
        return item
'''
# Run the application
if __name__ == "__main__":
     # Fetch the item using raw SQL
    item_raw_sql = get_item_by_id_raw_sql(1)
    print("Raw SQL:", item_raw_sql)
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)