from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str
    password_hash: str
    role: str  # comprador, comercio, admin

class Product(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    price: float
    commerce_id: int
    approved: bool = False

class Order(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int
    products: str  # comma-separated product ids

