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
    
