import streamlit as st
from lcivil.civil import Volume 

st.title("App de Calculo de Volume de Viga")

st.write("Por favor digite as informações nescessarias")

altura = st.text_input("Altura da viga")
largura = st.text_input("Largura da viga")
base = st.text_input("Base da viga")

if st.button("Calcule Volume"):
  volume = Volume(float(altura),float(largura),float(base))
  st.subheader("Volume da Viga : [%s] " % volume.calcule())
 
