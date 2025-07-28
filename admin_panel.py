import streamlit as st
from db import get_session
from models import Product, User

def show_admin_panel():
    st.subheader("Panel de Administración")
    if "role" not in st.session_state or st.session_state["role"] != "admin":
        st.error("Debes ingresar como admin para acceder a este panel.")
        return
    with get_session() as session:
        st.write("### Aprobar productos")
        products = session.query(Product).filter(Product.approved == False).all()
        for prod in products:
            st.write(f"{prod.name} - ${prod.price} (Comercio: {prod.commerce_id})")
            if st.button(f"Aprobar producto {prod.id}"):
                prod.approved = True
                session.commit()
                st.success(f"Producto {prod.name} aprobado")
        st.write("### Lista de comercios")
        commerces = session.query(User).filter(User.role == "comercio").all()
        for u in commerces:
            st.write(f"{u.username} (ID: {u.id})")


