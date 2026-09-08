import os
from sqladmin import Admin
from fastapi import FastAPI
from database import engine
from admin_sql.auth import AdminAuth
from admin_sql.views import (
    BookAdmin,
    UserAdmin,
    OrderAdmin,
    CartItemAdmin,
    FavoriteAdmin,
)

def setup_admin(app: FastAPI):
    authentication_backend = AdminAuth(secret_key=os.getenv("SECRET_KEY"))
    admin = Admin(
        app,
        engine,
        title="Bookstore Admin",
        authentication_backend=authentication_backend,
        base_url="/admin",
    )
    admin.add_view(BookAdmin)
    admin.add_view(UserAdmin)
    admin.add_view(OrderAdmin)
    admin.add_view(CartItemAdmin)
    admin.add_view(FavoriteAdmin)
    return admin

__all__=["setup_admin"]