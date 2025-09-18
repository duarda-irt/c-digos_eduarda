import streamlit as st 
### coloca um titulo
st.title("testantando site")

###Escreve
st.write("testando...direita, esquerda")

###cria uma barra lateral
st.sidebar.title("barra lateral")

###criando uma lista
nomes = ["julias", " duda", " elana"]

###cria uma caixinha na barra lateral
st.sidebar._selectbox("escolha um nome:", nomes)

###coloca o video na pagina do site 
st.video("link")



st.sidebar.title("aluguel de carros")
st.sidebar.image("logo.png")
st.sidebar.write("escolha um carro ideal para voce ")
carros = ["gol", " BMW","toro", "jeep"]
st.sidebar.selectbox("escolha o modelo do carro :", carros)