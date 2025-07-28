import streamlit as st
from passlib.hash import bcrypt
from db import get_session
from models import User

def show_login():
    st.subheader("Ingresar")
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    if st.button("Ingresar"):
        with get_session() as session:
            user = session.query(User).filter(User.username == username).first()
            if user and bcrypt.verify(password, user.password_hash):
                st.session_state["username"] = user.username
                st.session_state["role"] = user.role
                st.success(f"Bienvenido, {user.username} ({user.role})")
            else:
                st.error("Credenciales incorrectas")

def show_register():
    st.subheader("Registro")
    username = st.text_input("Usuario nuevo")
    password = st.text_input("Contraseña nueva", type="password")
    role = st.selectbox("Rol", ["comprador", "comercio"])
    if st.button("Registrar"):
        with get_session() as session:
            exists = session.query(User).filter(User.username == username).first()
            if exists:
                st.error("Usuario ya existe")
            else:
                hashed = bcrypt.hash(password)
                user = User(username=username, password_hash=hashed, role=role)
                session.add(user)
                session.commit()
                st.success("Usuario registrado correctamente")





