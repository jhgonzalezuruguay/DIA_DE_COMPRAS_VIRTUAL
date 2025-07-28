import streamlit as st
from db import get_session
from models import Product, Order, User

def show_catalog():
    st.subheader("Catálogo de productos")
    with get_session() as session:
        products = session.query(Product).filter(Product.approved == True).all()
        if not products:
            st.info("No hay productos aprobados.")
            return
        selected = []
        for prod in products:
            st.write(f"**{prod.name}** - ${prod.price}")
            if st.button(f"Agregar '{prod.name}' al carrito", key=prod.id):
                if "cart" not in st.session_state:
                    st.session_state["cart"] = []
                st.session_state["cart"].append(prod.id)
                st.success(f"{prod.name} agregado al carrito")
        if "cart" in st.session_state and st.session_state["cart"]:
            st.write("### Carrito actual")
            cart_product_ids = st.session_state["cart"]
            for pid in cart_product_ids:
                prod = session.query(Product).filter(Product.id == pid).first()
                if prod:
                    st.write(f"{prod.name} - ${prod.price}")
            if st.button("Generar Pedido"):
                if "username" in st.session_state:
                    user = session.query(User).filter(User.username == st.session_state["username"]).first()
                    order = Order(user_id=user.id, products=",".join(map(str, cart_product_ids)))
                    session.add(order)
                    session.commit()
                    st.success("¡Pedido generado!")
                    st.session_state["cart"] = []
                else:
                    st.error("Debes iniciar sesión para generar pedidos.")

