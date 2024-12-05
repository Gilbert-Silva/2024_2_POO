import streamlit as st
from retanguloUI import RetanguloUI
from equacaoUI import EquacaoUI

op = st.sidebar.selectbox("Menu", ["Retângulo", "Equação"])
if op == "Retângulo": RetanguloUI.main()
if op == "Equação": EquacaoUI.main()


#st.header("POO em Python com Streamlit")
#if st.button("Clique aqui"):
#    st.write("Bem-vindo(a) ao Streamlit")
