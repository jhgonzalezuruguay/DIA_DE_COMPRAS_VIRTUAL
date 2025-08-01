import streamlit as st
from auth import show_login, show_register
from catalog import show_catalog
from commerce_panel import show_commerce_panel
from admin_panel import show_admin_panel
from db import create_db_and_tables

create_db_and_tables()  # crea tablas si no existen

st.title("Día Virtual de Compras")

menu = st.sidebar.selectbox("Menú", ["Catálogo", "Login", "Registro", "Comercio", "Admin"])
if menu == "Login":
    show_login()
elif menu == "Registro":
    show_register()
elif menu == "Catálogo":
    show_catalog()
elif menu == "Comercio":
    show_commerce_panel()
elif menu == "Admin":
    show_admin_panel()

if st.sidebar.button("Cerrar sesión"):
    st.session_state.clear()
    st.success("Sesión cerrada.")



