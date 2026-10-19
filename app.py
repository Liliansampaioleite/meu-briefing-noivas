import streamlit as st

st.set_page_config(page_title="Briefing Noivas e Festas", page_icon="👰")

st.title("Briefing - Noivas e Festas 👰")
st.write("Preencha com carinho para eu preparar sua seleção")

nome = st.text_input("Nome completo")
data = st.date_input("Data do evento")
horario = st.time_input("Horário do evento")
voce_e = st.selectbox("Você é:", ["Noiva", "Mãe da noiva", "Mãe do noivo", "Irmã", "Madrinha", "Convidada"])
manequim = st.text_input("Número da calça / manequim / altura")
objetivo = st.text_area("O que você quer transmitir nesse dia?")

if st.button("Enviar meu briefing ✨"):
    st.success(f"Perfeito, {nome}! Recebi para o dia {data}. Já vou preparar sua seleção!")
    st.balloons()
