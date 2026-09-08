from sqladmin import ModelView
from models import User, Book, Order, CartItem, Favorite


class BookAdmin(ModelView, model=Book):
    column_list = [Book.id, Book.title, Book.author, Book.price, Book.category]
    search_fields = [Book.title, Book.author]
    form_fields = [Book.title, Book.author, Book.price, Book.old_price, Book.image, Book.category, Book.description]

    column_details_exclude_list = [Book.cart_items, Book.favorites]

class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.login, User.name, User.email, User.age]
    exclude_fields = [User.password_hash]

class OrderAdmin(ModelView, model=Order):
    column_list = [Order.id, Order.user_id, Order.total_sum, Order.status, Order.created_at]

class CartItemAdmin(ModelView, model=CartItem):
    column_list = [CartItem.id, CartItem.user_id, CartItem.book_id, CartItem.quantity]

class FavoriteAdmin(ModelView, model=Favorite):
    column_list = [Favorite.id, Favorite.user_id, Favorite.book_id]