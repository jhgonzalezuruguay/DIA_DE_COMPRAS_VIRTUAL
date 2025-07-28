import streamlit as st
from passlib.hash import bcrypt
from db import get_session
from models import User

def show_login():
    st.subheader("Login")
    # Implementar formulario de login...

def show_register():
    st.subheader("Registro")
    # Implementar formulario de registro...
