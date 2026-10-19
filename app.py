import streamlit as st
st.title("Briefing -CASAMENTO IDEAL-NOIVAS  👰")
with st.form("form"):
    nome = st.text_input("Nome completo: ")
    data = st.date_input("Data do evento: ")
    horario = st.time_input("Horário do evento: ")
    voce = st.selectbox("Você é:", ["Noiva", "Festa", "Noivo"])
    medidas = st.text_input("Número da calça / manequim : ")
    transmitir = st.text_area("O que quer transmitir nesse dia?")
    cerimonial = st.text_input("Tem cerimonial? Nome")
    orcamento = st.text_input("Seu orçamento")
    instagram = st.text_input("Seu Instagram @")
    nao_faltar = st.text_area("O que NÃO pode faltar?")
    botao = st.form_submit_button("Enviar 💌")
if botao:
    st.success(f"Obrigada {nome}! Recebi! 💖")
    st.balloons()
