import streamlit as st
from db import get_session
from models import Product, User

def show_commerce_panel():
    st.subheader("Panel de Comercio")
    if "role" not in st.session_state or st.session_state["role"] != "comercio":
        st.error("Debes ingresar como comercio para acceder a este panel.")
        return
    with get_session() as session:
        user = session.query(User).filter(User.username == st.session_state["username"]).first()
        st.write("### Agregar nuevo producto")
        name = st.text_input("Nombre del producto")
        price = st.number_input("Precio", min_value=0.0)
        if st.button("Agregar producto"):
            prod = Product(name=name, price=price, commerce_id=user.id, approved=False)
            session.add(prod)
            session.commit()
            st.success("Producto enviado para aprobación")
        st.write("### Tus productos")
        products = session.query(Product).filter(Product.commerce_id == user.id).all()
        for prod in products:
            st.write(f"{prod.name} - ${prod.price} (Aprobado: {'Sí' if prod.approved else 'No'})")
            new_name = st.text_input(f"Editar nombre ({prod.id})", value=prod.name, key=f"edit_name_{prod.id}")
            new_price = st.number_input(f"Editar precio ({prod.id})", value=prod.price, key=f"edit_price_{prod.id}")
            if st.button(f"Guardar ({prod.id})"):
                prod.name = new_name
                prod.price = new_price
                session.commit()
                st.success("Producto actualizado")


