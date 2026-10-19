importar fluxo de luz como rua
importar globo

rua.definir_configuração_da_página(título_da_página="Casamento Ideal Noivas e Festas", ícone_da_página="💍")

rua.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');
h1 {
    font-family: 'Great Vibes', cursive !important;
    font-size: 60px !important;
    color: white !important;
    text-align: center;
}
</style>
""", unsafe_allow_html=Verdadeiro)

# ESSE TRECHO ACHA QUALQUER IMAGEM SOZINHO, NÃO IMPORTA O NOME
imagens = globo.globo("*.png")+ globo.globo("*.jpg")+ globo.globo("*.jpeg")+ globo.globo("*.webp")
se imagens:
    rua.imagem(imagens[0], largura=150)

rua.título("Casamento Ideal Noivas e Festas")

com rua.forma("forma"):
    nome = rua.entrada_de_texto("Nome completo")
    dados = rua.entrada_de_data("Dados do evento", valor=Nenhum)
    horário = rua.entrada_de_tempo("Horário do evento", valor=Nenhum)
    medidas = rua.entrada_de_texto("Número da calça / manequim / altura")
    transmitir = rua.área_de_texto("O que quer transmitir nesse dia?")
    cerimonial = rua.entrada_de_texto("Tem cerimonial? Nome")
    orquestração = rua.entrada_de_texto("Seu puxando")
    Instagram = rua.entrada_de_texto("Seu Instagram @")
    Loja = rua.entrada_de_texto("Como conheceu a loja? Já provou seu vestido? Se sim, qual loja?")
    nao_faltar = rua.área_de_texto("O que pode faltar?")
    botao = rua.botão_enviar_formulário("Enviar 💍")

se botao:
    rua.sucesso(f"Obrigada {nome}! Recebi! 💍")
    
import streamlit as st
import glob

st.set_page_config(page_title="Casamento Ideal Noivas e Festas", page_icon="💍")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');
h1 {
    font-family: 'Great Vibes', cursive !important;
    font-size: 60px !important;
    color: white !important;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

imagens = glob.glob("*.png")+ glob.glob("*.jpg")+ glob.glob("*.jpeg")+ glob.glob("*.webp")
if imagens:
    st.image(imagens[0], width=150)

st.title("Casamento Ideal Noivas e Festas")

with st.form("forma"):
    nome = st.text_input("Nome completo")
    dados = st.date_input("Dados do evento", value=None)
    horario = st.time_input("Horario do evento", value=None)
    medidas = st.text_input("Numero da calca / manequim / altura")
    transmitir = st.text_area("O que quer transmitir nesse dia?")
    cerimonial = st.text_input("Tem cerimonial? Nome")
    orquestracao = st.text_input("Seu puxando")
    Instagram = st.text_input("Seu Instagram @")
    Loja = st.text_input("Como conheceu a loja? Ja provou seu vestido? Se sim, qual loja?")
    nao_faltar = st.text_area("O que NAO pode faltar?")
    botao = st.form_submit_button("Enviar 💍")

if botao:
    st.success(f"Obrigada {nome}! Recebi! 💍")
