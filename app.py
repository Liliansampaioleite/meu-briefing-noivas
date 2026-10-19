import streamlit as st
import glob

st.set_page_config(page_title="Casamento Ideal", page_icon="💍")

st.markdown("""
<style>
.stApp, body, html {
    background: white !important;
}
p, label, span, div {
    color: black !important;
}
input, textarea {
    background: white !important;
    color: black !important;
    border: 1px solid #ccc !important;
}
</style>
""", unsafe_allow_html=True)

imgs = glob.glob("*.png") + glob.glob("*.jpg") + glob.glob("*.jpeg") + glob.glob("*.webp")
if imgs:
    st.image(imgs[0], width=150)

st.title("Casamento Ideal Noivas e Festas")

with st.form("form"):
    nome = st.text_input("Nome completo")
    data = st.date_input("Data do evento", value=None)
    horario = st.time_input("Horario do evento", value=None)
    medidas = st.text_input("Numero da calca / manequim / altura")
    transmitir = st.text_area("O que quer transmitir nesse dia?")
    cerimonial = st.text_input("Tem cerimonial? Nome")
    orquestracao = st.text_input("Seu puxando")
    insta = st.text_input("Seu Instagram @")
    loja = st.text_input("Como conheceu a loja? Ja provou seu vestido? Se sim, qual loja?")
    nao_faltar = st.text_area("O que NAO pode faltar?")
    ok = st.form_submit_button("Enviar 💍")

if ok:
    st.success(f"Obrigada {nome}! Recebi! 💍")
    st.balloons()
