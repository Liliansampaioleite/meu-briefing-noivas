import streamlit as st
import glob

st.set_page_config(page_title="Casamento Ideal Noivas e Festas", page_icon="💍")

st.markdown("""
<style>
.stApp {
    background: white !important;
}
@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');
h1 {
    font-family: 'Great Vibes', cursive !important;
    font-size: 60px !important;
    color: #c08a90 !important;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

imagens = glob.glob("*.png") + glob.glob("*.jpg") + glob.glob("*.jpeg") + glob.glob("*.webp")
if imagens:
    st.image(imagens[0], width=150)

st.title("Casamento Ideal Noivas e Festas")

with st.form("forma"):
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
    botao = st.form_submit_button("Enviar 💍")

if botao:
    st.success(f"Obrigada {nome}! Recebi seu briefing! 💍")
    st.balloons()
