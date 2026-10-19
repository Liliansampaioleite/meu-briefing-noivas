import streamlit as st
import glob

st.set_page_config(page_title="Casamento Ideal Noivas e Festas", page_icon="👰")

# ESSE TRECHO ACHA QUALQUER IMAGEM SOZINHO, NÃO IMPORTA O NOME
imagens = glob.glob("*.png") + glob.glob("*.jpg") + glob.glob("*.jpeg") + glob.glob("*.webp")
if imagens:
    st.image(imagens[0], width=300)

st.title("Casamento Ideal Noivas e Festas 👰")

with st.form("form"):
    nome = st.text_input("Nome completo")
    data = st.date_input("Data do evento", value=None)
    horario = st.time_input("Horário do evento", value=None)
    medidas = st.text_input("Número da calça / manequim / altura")
    transmitir = st.text_area("O que quer transmitir nesse dia?")
    cerimonial = st.text_input("Tem cerimonial? Nome")
    orcamento = st.text_input("Seu orçamento")
    instagram = st.text_input("Seu Instagram @")
    conheceu_loja = st.text_input("Como conheceu a loja? Já provou seu vestido? Se sim, qual loja?")
    nao_faltar = st.text_area("O que NÃO pode faltar?")
    botao = st.form_submit_button("Enviar 💌")

if botao:
    st.success(f"Obrigada {nome}! Recebi! 💖")
    st.balloons()

